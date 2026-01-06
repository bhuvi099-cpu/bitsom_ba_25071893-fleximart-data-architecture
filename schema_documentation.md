# FlexiMart Database Schema Documentation

## ENTITY: customers
Purpose: Stores customer information.

Attributes:
- customer_id: Primary key, auto-incremented
- first_name: Customer first name
- last_name: Customer last name
- email: Unique customer email
- phone: Standardized Indian phone number
- city: Customer city
- registration_date: Registration date

Relationships:
- One customer can place many orders (1:M with orders)

---

## ENTITY: products
Purpose: Stores product catalog data.

Attributes:
- product_id: Primary key
- product_name: Name of the product
- category: Product category
- price: Product price
- stock_quantity: Available inventory

Relationships:
- One product can appear in many order items (1:M with order_items)

---

## ENTITY: orders
Purpose: Stores order-level information.

Attributes:
- order_id: Primary key
- customer_id: Foreign key referencing customers
- order_date: Date of order
- total_amount: Total order value
- status: Order status

Relationships:
- One order belongs to one customer
- One order has many order items

---

## ENTITY: order_items
Purpose: Stores line-level order details.

Attributes:
- order_item_id: Primary key
- order_id: Foreign key referencing orders
- product_id: Foreign key referencing products
- quantity: Quantity ordered
- unit_price: Price per unit
- subtotal: Calculated line total

---

## Normalization Explanation (3NF)

The database design follows Third Normal Form (3NF). Each table contains attributes that depend only on the primary key, eliminating partial and transitive dependencies. For example, customer details are stored exclusively in the customers table and are not duplicated in the orders table. Product attributes such as price and category are stored only in the products table, ensuring updates do not cause inconsistencies.

Functional dependencies are clearly defined: customer_id → customer attributes, product_id → product attributes, and order_id → order attributes. Order item details depend on order_item_id and reference both orders and products via foreign keys.

This design prevents update anomalies by isolating entity-specific data, avoids insert anomalies by allowing independent insertion of customers or products, and avoids delete anomalies by maintaining referential integrity through foreign keys.

---

## Sample Data

### Customers
| customer_id | first_name | email |
|------------|------------|-------|
| 1 | Rahul | rahul.sharma@gmail.com |
| 2 | Priya | priya.patel@yahoo.com |

### Products
| product_id | product_name | category |
|------------|--------------|----------|
| 1 | Samsung Galaxy S21 | Electronics |
| 2 | Nike Running Shoes | Fashion |

### Orders
| order_id | customer_id | total_amount |
|---------|-------------|--------------|
| 1 | 1 | 45999 |
| 2 | 2 | 5998 |

### Order Items
| order_item_id | order_id | product_id | subtotal |
|--------------|----------|------------|----------|
| 1 | 1 | 1 | 45999 |
| 2 | 2 | 4 | 5998 |
