import pandas as pd
import re
from sqlalchemy import create_engine
from datetime import datetime

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
# Update these values as per your setup
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"   # 3306 for MySQL
DB_NAME = "fleximart"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# -----------------------------
# DATA QUALITY METRICS
# -----------------------------
report = {
    "customers": {"processed": 0, "duplicates_removed": 0, "missing_handled": 0},
    "products": {"processed": 0, "duplicates_removed": 0, "missing_handled": 0},
    "sales": {"processed": 0, "duplicates_removed": 0, "missing_handled": 0},
}

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def standardize_phone(phone):
    if pd.isna(phone):
        return None
    phone = re.sub(r"\D", "", str(phone))
    phone = phone[-10:]
    return f"+91-{phone}"

def parse_date(date_val):
    if pd.isna(date_val):
        return None
    return pd.to_datetime(date_val, errors="coerce").date()

# -----------------------------
# EXTRACT
# -----------------------------
customers = pd.read_csv("data/customers_raw.csv")
products = pd.read_csv("data/products_raw.csv")
sales = pd.read_csv("data/sales_raw.csv")

# -----------------------------
# TRANSFORM: CUSTOMERS
# -----------------------------
report["customers"]["processed"] = len(customers)

customers_before = len(customers)
customers = customers.drop_duplicates(subset=["customer_id"])
report["customers"]["duplicates_removed"] = customers_before - len(customers)

customers["email"] = customers["email"].fillna(None)
customers["phone"] = customers["phone"].apply(standardize_phone)
customers["registration_date"] = customers["registration_date"].apply(parse_date)
customers["city"] = customers["city"].str.title()

report["customers"]["missing_handled"] = customers.isna().sum().sum()

customers = customers.drop(columns=["customer_id"])

# -----------------------------
# TRANSFORM: PRODUCTS
# -----------------------------
report["products"]["processed"] = len(products)

products_before = len(products)
products = products.drop_duplicates(subset=["product_id"])
report["products"]["duplicates_removed"] = products_before - len(products)

products["category"] = products["category"].str.strip().str.lower().str.capitalize()
products = products.dropna(subset=["price"])
products["stock_quantity"] = products["stock_quantity"].fillna(0)

report["products"]["missing_handled"] = products.isna().sum().sum()

products = products.drop(columns=["product_id"])

# -----------------------------
# TRANSFORM: SALES → ORDERS + ORDER_ITEMS
# -----------------------------
report["sales"]["processed"] = len(sales)

sales_before = len(sales)
sales = sales.drop_duplicates(subset=["transaction_id"])
report["sales"]["duplicates_removed"] = sales_before - len(sales)

sales = sales.dropna(subset=["customer_id", "product_id"])
sales["transaction_date"] = sales["transaction_date"].apply(parse_date)

report["sales"]["missing_handled"] = sales.isna().sum().sum()

# -----------------------------
# LOAD
# -----------------------------
customers.to_sql("customers", engine, if_exists="append", index=False)
products.to_sql("products", engine, if_exists="append", index=False)

# Reload IDs for mapping
db_customers = pd.read_sql("SELECT customer_id, email FROM customers", engine)
db_products = pd.read_sql("SELECT product_id, product_name FROM products", engine)

orders = sales.groupby(
    ["customer_id", "transaction_date", "status"], as_index=False
).apply(
    lambda x: (x["quantity"] * x["unit_price"]).sum()
).reset_index()

orders.columns = ["customer_id", "order_date", "status", "total_amount"]

orders = orders.merge(db_customers, how="left", left_on="customer_id", right_on="email")
orders = orders[["customer_id_y", "order_date", "total_amount", "status"]]
orders.columns = ["customer_id", "order_date", "total_amount", "status"]

orders.to_sql("orders", engine, if_exists="append", index=False)

order_items = sales.copy()
order_items = order_items.merge(db_products, how="left", left_on="product_id", right_on="product_name")

order_items["subtotal"] = order_items["quantity"] * order_items["unit_price"]
order_items = order_items[["product_id_y", "quantity", "unit_price", "subtotal"]]
order_items.columns = ["product_id", "quantity", "unit_price", "subtotal"]

order_items.to_sql("order_items", engine, if_exists="append", index=False)

# -----------------------------
# DATA QUALITY REPORT
# -----------------------------
with open("data_quality_report.txt", "w") as f:
    for table, stats in report.items():
        f.write(f"{table.upper()} DATA\n")
        for k, v in stats.items():
            f.write(f"{k}: {v}\n")
        f.write("\n")

print("ETL Pipeline executed successfully.")
