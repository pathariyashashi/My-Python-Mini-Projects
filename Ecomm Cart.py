# Product Class
class Product:

    # Constructor
    def __init__(self, product_id, name, price):

        self.product_id = product_id
        self.name = name
        self.price = price

    # Magic Method
    def __str__(self):

        return f"{self.name} - ₹{self.price}"


# Cart Class
class Cart:

    # Constructor
    def __init__(self):

        self.products = []

    # Add Product
    def add_product(self, product):

        self.products.append(product)

        print(f"{product.name} added to cart.")

    # Remove Product
    def remove_product(self, product_name):

        for product in self.products:

            if product.name == product_name:

                self.products.remove(product)

                print(f"{product.name} removed from cart.")

                return

        print("Product not found!")

    # View Cart
    def view_cart(self):

        print("\n----- Your Cart -----")

        if len(self.products) == 0:

            print("Cart is empty!")

        else:

            for product in self.products:

                print(product)

    # Total Bill
    def total_bill(self):

        total = 0

        for product in self.products:

            total += product.price

        # Discount
        if total >= 5000:

            discount = total * 0.10

            total = total - discount

            print(f"10% Discount Applied: ₹{discount}")

        print(f"Total Bill: ₹{total}")


# Product Objects
p1 = Product(1, "Laptop", 45000)

p2 = Product(2, "Mouse", 500)

p3 = Product(3, "Keyboard", 1500)

p4 = Product(4, "Headphones", 3000)


# Cart Object
cart = Cart()

# Add Products
cart.add_product(p1)

cart.add_product(p2)

cart.add_product(p4)

# View Cart
cart.view_cart()

# Remove Product
cart.remove_product("Mouse")

# View Cart Again
cart.view_cart()

# Final Bill
cart.total_bill()