Grocery Store Management System (GSMS) - README
Overview
The Grocery Store Management System (GSMS) is a web-based application designed to manage products, orders, and inventory for a grocery store. It provides a user-friendly interface for store owners to add products, create orders, and track sales.

Features
1. Product Management
Add new products with name, unit of measure, and price

View all existing products in a table format

Delete products from the system

2. Order Management
Create new orders with customer details

Add multiple products to an order with quantities

Automatic calculation of order totals

View all past orders with details

3. Dashboard
Overview of recent orders

Quick access to product management and order creation

Technical Stack
Frontend
HTML5, CSS3, JavaScript

Bootstrap for responsive design

jQuery for DOM manipulation and AJAX calls

Material Design icons for UI elements

Backend
Python Flask framework

MySQL database

RESTful API endpoints

Database Schema
The system uses a relational database with the following tables:

products: Stores product information

uom: Stores units of measurement

orders: Stores order headers

order_details: Stores line items for each order

Installation Guide
Prerequisites
Python 3.x

MySQL Server

pip package manager

Setup Steps
Clone the repository

Install required Python packages:

pip install flask mysql-connector-python
Set up MySQL database:

Create a database named 'gs'

Import the SQL schema (not provided in current files)

Configure database connection in sql_connection.py:

python
__cnx = mysql.connector.connect(user='your_username', password='your_password', database='gs')
Start the Flask server:

python server.py
Open the application in a web browser by navigating to the HTML files

File Structure
├── index.html                # Main dashboard page
├── manage-product.html       # Product management interface
├── order.html                # Order creation interface
├── server.py                 # Flask backend server
├── sql_connection.py         # Database connection handler
├── products_dao.py           # Data access for products
├── orders_dao.py             # Data access for orders
├── uom_dao.py                # Data access for units of measurement
├── css/                      # Stylesheets
│   ├── bootstrap.min.css
│   ├── style.css
│   ├── sidebar-menu.css
│   ├── custom.css
└── js/                       # JavaScript files
    ├── packages/
    │   └── jquery.min.js
    └── custom/
        ├── common.js
        ├── dashboard.js
        ├── manage-product.js
        └── order.js
API Endpoints
Products
GET /getProducts - Get all products

POST /insertProduct - Add a new product

POST /deleteProduct - Delete a product

Orders
GET /getAllOrders - Get all orders

POST /insertOrder - Create a new order

Units of Measurement
GET /getUOM - Get all units of measurement

Usage Instructions
Dashboard (index.html)

View recent orders

Navigate to product management or create new orders

Manage Products (manage-product.html)

Click "Add New Product" to open the product form

Fill in product details and click "Save"

Products appear in the table below

Use the delete button to remove products

Create Order (order.html)

Enter customer name

Add products to the order by selecting from the dropdown

Adjust quantities as needed

The system automatically calculates totals

Click "Save" to complete the order

Future Enhancements
User authentication and authorization

Inventory management with stock levels

Reporting and analytics dashboard

Customer management system

Barcode scanning integration

Troubleshooting
If the application fails to connect to the database, verify credentials in sql_connection.py

Ensure all required Python packages are installed

Check browser console for JavaScript errors if the UI isn't working properly

Verify the Flask server is running on port 5000

License
This project is open-source and available for modification and distribution under the MIT License.
