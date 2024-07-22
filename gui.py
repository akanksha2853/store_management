import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class OnlineStoreManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Store Management System")
        self.root.geometry("1100x600")
        self.root.configure(bg="#ffffff")

        # Database connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ak@28",
            database="online_store"
        )
        self.cursor = self.conn.cursor()

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg="#ffffff")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Notebook for tabbed interface
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Product management tab
        product_frame = tk.Frame(notebook, bg="#ffffff")
        notebook.add(product_frame, text="Product Management")

        # Customer management tab
        customer_frame = tk.Frame(notebook, bg="#ffffff")
        notebook.add(customer_frame, text="Customer Management")

        # Order management tab
        order_frame = tk.Frame(notebook, bg="#ffffff")
        notebook.add(order_frame, text="Order Management")

        # Product Management Widgets
        tk.Label(product_frame, text="Product Name", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.product_name_var = tk.StringVar()
        tk.Entry(product_frame, textvariable=self.product_name_var, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(product_frame, text="Price", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.product_price_var = tk.DoubleVar()
        tk.Entry(product_frame, textvariable=self.product_price_var, font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(product_frame, text="Category", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.product_category_var = tk.StringVar()
        tk.Entry(product_frame, textvariable=self.product_category_var, font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(product_frame, text="Stock", bg="#ffffff", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.product_stock_var = tk.IntVar()
        tk.Entry(product_frame, textvariable=self.product_stock_var, font=("Arial", 12)).grid(row=3, column=1, padx=10, pady=10)

        tk.Button(product_frame, text="Add Product", command=self.add_product, bg="#4CAF50", fg="#ffffff", font=("Arial", 10, "bold")).grid(row=4, column=0, pady=10, padx=5)
        tk.Button(product_frame, text="Update Product", command=self.update_product, bg="#2196F3", fg="#ffffff", font=("Arial", 10, "bold")).grid(row=4, column=1, pady=10, padx=5)
        tk.Button(product_frame, text="Delete Product", command=self.delete_product, bg="#f44336", fg="#ffffff", font=("Arial", 10, "bold")).grid(row=4, column=2, pady=10, padx=5)
        tk.Button(product_frame, text="View Products", command=self.view_products, bg="#FFC107", fg="#ffffff", font=("Arial", 10, "bold")).grid(row=4, column=3, pady=10, padx=5)

        # Treeview for Product Management
        self.product_tree = ttk.Treeview(product_frame, columns=("ID", "Name", "Price", "Category", "Stock"), show="headings")
        self.product_tree.heading("ID", text="ID")
        self.product_tree.heading("Name", text="Name")
        self.product_tree.heading("Price", text="Price")
        self.product_tree.heading("Category", text="Category")
        self.product_tree.heading("Stock", text="Stock")
        self.product_tree.grid(row=5, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

        # Customer Management Widgets
        tk.Label(customer_frame, text="Customer Name", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.customer_name_var = tk.StringVar()
        tk.Entry(customer_frame, textvariable=self.customer_name_var, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(customer_frame, text="Email", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.customer_email_var = tk.StringVar()
        tk.Entry(customer_frame, textvariable=self.customer_email_var, font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(customer_frame, text="Phone", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.customer_phone_var = tk.StringVar()
        tk.Entry(customer_frame, textvariable=self.customer_phone_var, font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(customer_frame, text="Address", bg="#ffffff", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.customer_address_var = tk.StringVar()
        tk.Entry(customer_frame, textvariable=self.customer_address_var, font=("Arial", 12)).grid(row=3, column=1, padx=10, pady=10)

        tk.Button(customer_frame, text="Add Customer", command=self.add_customer, bg="#4CAF50", fg="#ffffff", font=("Arial", 10, "bold")).grid(row=4, column=0, pady=10, padx=5)
        tk.Button(customer_frame, text="Update Customer", command=self.update_customer, bg="#2196F3", fg="#ffffff", font=("Arial", 10, "bold")).grid(row=4, column=1, pady=10, padx=5)
        tk.Button(customer_frame, text="Delete Customer", command=self.delete_customer, bg="#f44336", fg="#ffffff", font=("Arial", 10, "bold")).grid(row=4, column=2, pady=10, padx=5)
        tk.Button(customer_frame, text="View Customers", command=self.view_customers, bg="#FFC107", fg="#ffffff", font=("Arial", 10, "bold")).grid(row=4, column=3, pady=10, padx=5)

        # Treeview for Customer Management
        self.customer_tree = ttk.Treeview(customer_frame, columns=("ID", "Name", "Email", "Phone", "Address"), show="headings")
        self.customer_tree.heading("ID", text="ID")
        self.customer_tree.heading("Name", text="Name")
        self.customer_tree.heading("Email", text="Email")
        self.customer_tree.heading("Phone", text="Phone")
        self.customer_tree.heading("Address", text="Address")
        self.customer_tree.grid(row=5, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

        # Order Management Widgets
        tk.Label(order_frame, text="Customer ID", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.order_customer_id_var = tk.StringVar()
        tk.Entry(order_frame, textvariable=self.order_customer_id_var, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(order_frame, text="Product ID", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.order_product_id_var = tk.StringVar()
        tk.Entry(order_frame, textvariable=self.order_product_id_var, font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(order_frame, text="Quantity", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.order_quantity_var = tk.IntVar()
        tk.Entry(order_frame, textvariable=self.order_quantity_var, font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(order_frame, text="Status", bg="#ffffff", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.order_status_var = tk.StringVar()
        tk.Entry(order_frame, textvariable=self.order_status_var, font=("Arial", 12)).grid(row=3, column=1, padx=10, pady=10)

        tk.Button(order_frame, text="Place Order", command=self.place_order, bg="#4CAF50", fg="#ffffff", font=("Arial", 10, "bold")).grid(row=4, column=0, pady=10, padx=5)
        tk.Button(order_frame, text="Update Order", command=self.update_order, bg="#2196F3", fg="#ffffff", font=("Arial", 10, "bold")).grid(row=4, column=1, pady=10, padx=5)
        tk.Button(order_frame, text="View Orders", command=self.view_orders, bg="#FFC107", fg="#ffffff", font=("Arial", 10, "bold")).grid(row=4, column=2, pady=10, padx=5)

        # Treeview for Order Management
        self.order_tree = ttk.Treeview(order_frame, columns=("ID", "Customer ID", "Product ID", "Quantity", "Status"), show="headings")
        self.order_tree.heading("ID", text="ID")
        self.order_tree.heading("Customer ID", text="Customer ID")
        self.order_tree.heading("Product ID", text="Product ID")
        self.order_tree.heading("Quantity", text="Quantity")
        self.order_tree.heading("Status", text="Status")
        self.order_tree.grid(row=5, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

    # CRUD Operations for Product Management
    def add_product(self):
        name = self.product_name_var.get()
        price = self.product_price_var.get()
        category = self.product_category_var.get()
        stock = self.product_stock_var.get()

        if not name or not price or not category or not stock:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            query = "INSERT INTO products (name, price, category, stock) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (name, price, category, stock))
            self.conn.commit()
            messagebox.showinfo("Success", "Product added successfully!")
            self.view_products()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def update_product(self):
        selected_item = self.product_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a product to update!")
            return

        product_id = self.product_tree.item(selected_item)["values"][0]
        name = self.product_name_var.get()
        price = self.product_price_var.get()
        category = self.product_category_var.get()
        stock = self.product_stock_var.get()

        if not name or not price or not category or not stock:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            query = "UPDATE products SET name=%s, price=%s, category=%s, stock=%s WHERE id=%s"
            self.cursor.execute(query, (name, price, category, stock, product_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Product updated successfully!")
            self.view_products()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def delete_product(self):
        selected_item = self.product_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a product to delete!")
            return

        product_id = self.product_tree.item(selected_item)["values"][0]

        try:
            query = "DELETE FROM products WHERE id=%s"
            self.cursor.execute(query, (product_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Product deleted successfully!")
            self.view_products()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def view_products(self):
        for row in self.product_tree.get_children():
            self.product_tree.delete(row)

        try:
            query = "SELECT * FROM products"
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                self.product_tree.insert("", tk.END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    # CRUD Operations for Customer Management
    def add_customer(self):
        name = self.customer_name_var.get()
        email = self.customer_email_var.get()
        phone = self.customer_phone_var.get()
        address = self.customer_address_var.get()

        if not name or not email or not phone or not address:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            query = "INSERT INTO customers (name, email, phone, address) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (name, email, phone, address))
            self.conn.commit()
            messagebox.showinfo("Success", "Customer added successfully!")
            self.view_customers()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def update_customer(self):
        selected_item = self.customer_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a customer to update!")
            return

        customer_id = self.customer_tree.item(selected_item)["values"][0]
        name = self.customer_name_var.get()
        email = self.customer_email_var.get()
        phone = self.customer_phone_var.get()
        address = self.customer_address_var.get()

        if not name or not email or not phone or not address:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            query = "UPDATE customers SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
            self.cursor.execute(query, (name, email, phone, address, customer_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Customer updated successfully!")
            self.view_customers()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def delete_customer(self):
        selected_item = self.customer_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a customer to delete!")
            return

        customer_id = self.customer_tree.item(selected_item)["values"][0]

        try:
            query = "DELETE FROM customers WHERE id=%s"
            self.cursor.execute(query, (customer_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Customer deleted successfully!")
            self.view_customers()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def view_customers(self):
        for row in self.customer_tree.get_children():
            self.customer_tree.delete(row)

        try:
            query = "SELECT * FROM customers"
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                self.customer_tree.insert("", tk.END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    # CRUD Operations for Order Management
    def place_order(self):
        customer_id = self.order_customer_id_var.get()
        product_id = self.order_product_id_var.get()
        quantity = self.order_quantity_var.get()
        status = self.order_status_var.get()

        if not customer_id or not product_id or not quantity:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            query = "INSERT INTO orders (customer_id, product_id, quantity, status) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (customer_id, product_id, quantity, status))
            self.conn.commit()
            messagebox.showinfo("Success", "Order placed successfully!")
            self.view_orders()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def update_order(self):
        selected_item = self.order_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select an order to update!")
            return

        order_id = self.order_tree.item(selected_item)["values"][0]
        customer_id = self.order_customer_id_var.get()
        product_id = self.order_product_id_var.get()
        quantity = self.order_quantity_var.get()
        status = self.order_status_var.get()

        if not customer_id or not product_id or not quantity :
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            query = "UPDATE orders SET customer_id=%s, product_id=%s, quantity=%s, status=%s WHERE id=%s"
            self.cursor.execute(query, (customer_id, product_id, quantity, status, order_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Order updated successfully!")
            self.view_orders()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def view_orders(self):
        for row in self.order_tree.get_children():
            self.order_tree.delete(row)

        try:
            query = "SELECT * FROM orders"
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                self.order_tree.insert("", tk.END, values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineStoreManagementSystem(root)
    root.mainloop()