import mysql.connector
from config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            category VARCHAR(255) NOT NULL,
            stock INT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL,
            address TEXT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT NOT NULL,
            product_id INT NOT NULL,
            quantity INT NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status VARCHAR(255) NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
    """)
    connection.commit()
    cursor.close()
    connection.close()

def add_product(name, price, category, stock):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (%s, %s, %s, %s)", (name, price, category, stock))
    connection.commit()
    cursor.close()
    connection.close()

def view_products():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def update_product(product_id, name, price, category, stock):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET name=%s, price=%s, category=%s, stock=%s WHERE id=%s", (name, price, category, stock, product_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_product(product_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
    connection.commit()
    cursor.close()
    connection.close()

def add_customer(name, email, phone, address):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customers (name, email, phone, address) VALUES (%s, %s, %s, %s)", (name, email, phone, address))
    connection.commit()
    cursor.close()
    connection.close()

def view_customers():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def update_customer(customer_id, name, email, phone, address):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE customers SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s", (name, email, phone, address, customer_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_customer(customer_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM customers WHERE id=%s", (customer_id,))
    connection.commit()
    cursor.close()
    connection.close()

def place_order(customer_id, product_id, quantity, status):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO orders (customer_id, product_id, quantity, status) VALUES (%s, %s, %s, %s)", (customer_id, product_id, quantity, status))
    connection.commit()
    cursor.close()
    connection.close()

def view_orders():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def update_order(order_id, status):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE orders SET status=%s WHERE id=%s", (status, order_id))
    connection.commit()
    cursor.close()
    connection.close()
