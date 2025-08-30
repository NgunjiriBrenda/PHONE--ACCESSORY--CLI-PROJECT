# PHONE ACCESSORY MANAGER CLI
A command-line interface (CLI) application for managing a phone accessory store inventory, customers, and sales operations.

## Features
### Accessory Management
List Accessories - View all available phone accessories

Add Accessory - Add new accessories to inventory

Update Accessory - Modify existing accessory details

Delete Accessory - Remove accessories from inventory

#### Customer Management
List Customers - View all registered customers

Add Customer - Register new customers

Update Customer - Modify customer information

Delete Customer - Remove customer records

##### Sales Management (Database Ready)
Sales table structure implemented and ready for future development

Relationship management between customers and accessories

###### Technology Stack
Python 3.8+

SQLAlchemy - ORM for database operations

Click - Beautiful command-line interface

SQLite - Lightweight database storage

 Installation
Clone the repository

bash
git clone <your-repo-url>
cd PHONE--ACCESSORY--CLI-PROJECT
Set up virtual environment

bash
pipenv install
pipenv shell
Install dependencies

bash
pip install sqlalchemy click
 Usage
Run the application:

bash
python main.py
Main Menu Options:

text
========================================
Welcome to Phone Accessory Manager!
1. Accessory Management
2. Customer Management  
3. Sale Management
4. Exit
========================================
Database Schema
Tables:
accessories - Phone accessory inventory

id, name, category, price, stock

customers - Customer information

id, name, phone, email

sales - Sales transactions (ready for implementation)

id, customer_id, accessory_id, quantity, date

 Project Structure
text
PHONE--ACCESSORY--CLI-PROJECT/
│
├── main.py              # Main application entry point
├── CRUD.py              # Database operations (Create, Read, Update, Delete)
├── accessory.db         # SQLite database (binary file)
├── seed.py              # Database seeding script
├── Pipfile              # Python dependencies
├── LICENSE              # MIT License
└── lib/
    └── models.py        # SQLAlchemy database models
 Key Features Implemented
   Full CRUD Operations for accessories and customers
   SQLite Database Integration with SQLAlchemy ORM
   Beautiful CLI Interface with Click library
   Error Handling and input validation
   Session Management with proper database connections
   Real-time Inventory Management with stock tracking

 CRUD Operations Available
For Accessories:
list_accessories() - Retrieve all accessories

add_accessory() - Create new accessory

view_accessory() - Get single accessory details

update_accessory() - Modify accessory information

delete_accessory() - Remove accessory

For Customers:
list_customers() - Retrieve all customers

add_customer() - Create new customer

view_customer() - Get single customer details

update_customer() - Modify customer information

delete_customer() - Remove customer

 Getting Started
First Run: The application will automatically create the database tables

Add Sample Data: Use the menu options to add accessories and customers

Manage Inventory: Use the intuitive menu system to manage your store

 Database Operations
The application uses SQLAlchemy for all database operations, providing:

Connection pooling and session management

Object-Relational Mapping (ORM) for easy data manipulation

Transaction support with commit/rollback capabilities

Automatic table creation and schema management

 Interface Features
Color-coded messages (green for success, red for errors)

Clear menu navigation with intuitive options

Input validation and error handling

Pause functionality to read messages before continuing

 Sample Data
The database comes pre-loaded with:

5 sample accessories (Phone cases, chargers, screen protectors)

5 sample customers with contact information

Ready-to-use sales table structure

 Future Enhancements
Complete sales management functionality

Inventory reporting and analytics

Customer purchase history





