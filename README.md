# Online Store Management System

## Description
A simple online store management system implemented in Python with Tkinter and MySQL.

## Files
- `config.py`: Configuration for database connection.
- `db.py`: Database operations.
- `gui.py`: GUI layout and functionality.
- `main.py`: Main entry point of the application.
- `store_management_system.sql`: SQL script for setting up the database.

## Technologies Used

- **Python**: Programming language for the application logic.
- **Tkinter**: Library for creating the graphical user interface.
- **MySQL**: Database management system for storing and managing data.
- **mysql-connector-python**: Python library for connecting to the MySQL database.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-link.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd your-repo-link
   ```

3. **Install Required Packages:**
   Make sure you have Python installed. You can install the required Python packages using pip:

   ```bash
   pip install mysql-connector-python
   ```

4. **Setup MySQL Database:**
   Create a MySQL database named `online_store` and set up the necessary tables. Use the provided SQL scripts in the `sql` directory to create tables and populate initial data.

5. **Run the Application:**
   Execute the main application file:

   ```bash
   python main.py
   ```

## Usage
1. **Product Management Tab:**
   - Add a new product with details including name, price, category, and stock.
   - Update existing product details.
   - Delete a product.
   - View all products in a tabular format.

2. **Customer Management Tab:**
   - Add a new customer with details including name, email, phone, and address.
   - Update existing customer details.
   - Delete a customer.
   - View all customers in a tabular format.

3. **Order Management Tab:**
   - Place a new order specifying product ID, quantity, and status.
   - Update existing order details.
   - View all orders in a tabular format.

Replace `your-username` and `your-repo-link` with your actual GitHub username and repository link. Adjust the instructions and details as needed based on your specific project setup.
