class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity += quantity

class InventoryManagementSystem:
    def __init__(self):
        self.products = {}
        self.users = [
            User("admin", "admin123", "Admin"),
            User("user1", "user123", "User")
        ]
        self.current_user = None

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print(f"Logged in as {user.role}")
                return True
        print("Invalid login credentials.")
        return False

    def check_admin_privileges(self):
        return self.current_user and self.current_user.role == "Admin"

    def add_product(self):
        if not self.check_admin_privileges():
            print("Only admins can add products.")
            return

        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        category = input("Enter Product Category: ")
        price = float(input("Enter Product Price: "))
        stock_quantity = int(input("Enter Stock Quantity: "))

        if product_id in self.products:
            print("Product ID already exists.")
            return

        new_product = Product(product_id, name, category, price, stock_quantity)
        self.products[product_id] = new_product
        print("Product added successfully.")

    def edit_product(self):
        if not self.check_admin_privileges():
            print("Only admins can edit products.")
            return

        product_id = input("Enter Product ID to edit: ")
        if product_id not in self.products:
            print("Product not found.")
            return

        product = self.products[product_id]
        product.name = input(f"Enter new name (current: {product.name}): ") or product.name
        product.category = input(f"Enter new category (current: {product.category}): ") or product.category
        product.price = float(input(f"Enter new price (current: {product.price}): ") or product.price)
        product.stock_quantity = int(input(f"Enter new stock quantity (current: {product.stock_quantity}): ") or product.stock_quantity)
        print("Product updated successfully.")

    def delete_product(self):
        if not self.check_admin_privileges():
            print("Only admins can delete products.")
            return

        product_id = input("Enter Product ID to delete: ")
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def view_inventory(self):
        if not self.current_user:
            print("Login required to view inventory.")
            return

        for product_id, product in self.products.items():
            print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, "
                  f"Price: ${product.price}, Stock: {product.stock_quantity}")

    def search_product(self):
        if not self.current_user:
            print("Login required to search products.")
            return

        search_term = input("Enter product name or category to search: ").lower()
        for product_id, product in self.products.items():
            if search_term in product.name.lower() or search_term in product.category.lower():
                print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, "
                      f"Price: ${product.price}, Stock: {product.stock_quantity}")

    def adjust_stock(self):
        if not self.check_admin_privileges():
            print("Only admins can adjust stock.")
            return

        product_id = input("Enter Product ID for stock adjustment: ")
        if product_id not in self.products:
            print("Product not found.")
            return

        adjustment = int(input("Enter stock adjustment (positive to add, negative to remove): "))
        self.products[product_id].update_stock(adjustment)
        print("Stock adjusted successfully.")

    def run(self):
        print("Welcome to Inventory Management System!")
        if not self.login():
            return

        while True:
            print("\nOptions:")
            print("1. Add Product")
            print("2. Edit Product")
            print("3. Delete Product")
            print("4. View Inventory")
            print("5. Search Product")
            print("6. Adjust Stock")
            print("7. Logout")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.edit_product()
            elif choice == "3":
                self.delete_product()
            elif choice == "4":
                self.view_inventory()
            elif choice == "5":
                self.search_product()
            elif choice == "6":
                self.adjust_stock()
            elif choice == "7":
                print("Logging out.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ims = InventoryManagementSystem()
    ims.run()
