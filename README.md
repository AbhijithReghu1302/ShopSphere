# ShopSphere – E-Commerce Order Management System

**An Oracle PL/SQL-Based E-Commerce Application with Python Flask Integration**

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.3-black)
![Oracle](https://img.shields.io/badge/Database-Oracle%2026ai-red)
![PL/SQL](https://img.shields.io/badge/Language-PL%2FSQL-orange)
![Status](https://img.shields.io/badge/Status-Developed-success)

## Project Overview

ShopSphere is an E-Commerce Order Management System developed as an academic mini project. The project demonstrates the practical implementation of Oracle Database, SQL, and PL/SQL concepts in an online shopping environment.

The system manages customer information, product categories, product details, orders, payments, and inventory records through a relational database.

A web-based interface is developed using HTML, CSS, and JavaScript, while Python Flask acts as the backend to connect the website with Oracle Database.

The application retrieves live product information from Oracle and provides a discount calculator that invokes a PL/SQL function stored in the database.


## Technologies Used

### Backend
- Python 3.10.11
- Flask 3.1.3
- python-oracledb 26.1.0

### Database
- Oracle Database 26ai Free
- SQL
- PL/SQL
- Oracle SQL Developer 26.2

### Frontend
- HTML5
- CSS3
- JavaScript

### Development Tools
- Visual Studio Code
- Oracle SQL Developer
- Git and GitHub

## System Architecture

ShopSphere follows a three-tier architecture:

1. **Frontend:** HTML, CSS, and JavaScript provide the user interface and handle browser interactions.
2. **Backend:** Python Flask receives requests, retrieves database records, and communicates with Oracle using the python-oracledb driver.
3. **Database:** Oracle Database stores application records and executes the PL/SQL business logic.

The architecture separates presentation, application processing, and data management.

## Database Design

The project uses an Oracle schema named `SHOPSPHERE`, containing eight relational tables.

| Table | Description |
|---|---|
| CUSTOMERS | Stores customer information. |
| CATEGORIES | Stores product category details. |
| PRODUCTS | Stores product names, prices, stock quantities, and reorder levels. |
| ORDERS | Stores order header information. |
| ORDER_ITEMS | Stores products and quantities associated with each order. |
| PAYMENTS | Stores payment information and payment status. |
| INVENTORY_TRANSACTIONS | Records inventory movements, including product sales. |
| STOCK_AUDIT | Maintains a record of changes in product stock. |

## PL/SQL Implementation

The project demonstrates several important PL/SQL programming concepts.

### 1. Discount Calculation Function

`CALCULATE_DISCOUNT` calculates the discount amount based on the purchase value.

Discount slabs:

| Purchase Amount | Discount |
|---|---:|
| Below ₹1,000 | 0% |
| ₹1,000 and above | 5% |
| ₹5,000 and above | 10% |
| ₹10,000 and above | 15% |

The function is called from the Flask backend using the Oracle Python driver.

### 2. Explicit Cursor – Low Stock Report

An explicit cursor retrieves products whose available stock is below their reorder level.

It demonstrates cursor declaration, opening, fetching, checking `%NOTFOUND`, and closing.

### 3. Stored Procedure – PROCESS_ORDER

The `PROCESS_ORDER` procedure handles the main order-processing operations.

Its responsibilities include:

- Validating customer and product IDs.
- Checking requested quantity.
- Verifying available stock.
- Calculating subtotal and discount.
- Creating order and order-item records.
- Updating product stock.
- Recording inventory transactions.
- Inserting payment records.

### 4. Exception Handling

The order-processing procedure handles different error conditions using application errors.

Tested cases include:

- Invalid quantity.
- Invalid customer ID.
- Invalid product ID.
- Insufficient stock.

### 5. Database Trigger – STOCK_AUDIT_TRIGGER

The stock audit trigger automatically records changes to product stock quantities.

It stores the product ID, previous stock quantity, updated stock quantity, timestamp, and database user in the `STOCK_AUDIT` table.

## Website Features

The current web application provides:

- ShopSphere homepage and navigation.
- Live product catalogue retrieved from Oracle Database.
- Product names and prices.
- Available stock information.
- Oracle-powered discount calculator.
- Responsive layout for different screen sizes.
- About section and project information.

**Note:** The order-processing procedure, exception handling, low-stock cursor, and stock audit trigger have been implemented and tested in Oracle SQL Developer. Direct website checkout integration with `PROCESS_ORDER` is a planned enhancement.

## Project Structure

```text
ShopSphere/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── database/
    └── [Oracle SQL and PL/SQL scripts, if included]
```

## Installation and Setup

### Prerequisites

- Python 3.10 or later.
- Oracle Database 26ai Free.
- Oracle SQL Developer.
- Visual Studio Code.
- Git.

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ShopSphere.git
```

Navigate into the project folder:

```bash
cd ShopSphere
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Oracle Database

Create and configure the Oracle `SHOPSPHERE` schema and execute the project's SQL and PL/SQL scripts.

The application uses the following connection configuration:

| Setting | Value |
|---|---|
| Host | localhost |
| Port | 1521 |
| Service Name | FREEPDB1 |
| Username | SHOPSPHERE |

Set your database password through an environment variable in PowerShell:

```powershell
$env:ORACLE_PASSWORD="YOUR_ORACLE_PASSWORD"
```

Do not commit your actual password to GitHub.

### Step 5: Run the Application

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

The ShopSphere homepage will display product records retrieved from Oracle Database.

## Testing and Verification

The following operations were tested during development:

1. Successful Python connection to Oracle Database.
2. Retrieval of product records from the PRODUCTS table.
3. Discount calculation using the Oracle PL/SQL function.
4. Low-stock reporting through an explicit cursor.
5. Order processing through the PROCESS_ORDER stored procedure.
6. Exception handling for invalid inputs and insufficient stock.
7. Automatic stock audit record creation through a database trigger.

## Learning Outcomes

The project provided practical experience in:

- Relational database design and table relationships.
- SQL queries and data manipulation.
- PL/SQL functions and stored procedures.
- Explicit cursor operations.
- Exception handling and transaction control.
- Database triggers and auditing.
- Python Flask web development.
- Python and Oracle Database integration.
- HTML, CSS, and JavaScript development.
- Debugging and testing a database-backed application.

## Future Enhancements

The following features can extend ShopSphere:

- Customer registration and login.
- Shopping cart functionality.
- Website-based checkout connected to `PROCESS_ORDER`.
- Customer order history.
- Administrator dashboard.
- Product search and category filtering.
- Payment gateway integration.
- Advanced inventory management.
- Improved application security and deployment.

## Author

**Abhijith Reghu**  
UID: 26MCA20043  
Master of Computer Applications (MCA)  
Chandigarh University

Faculty Guide: **Mr. Shruti**

---

*ShopSphere – E-Commerce Order Management System | MCA Mini Project*