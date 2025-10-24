class Product:
    """ 
    Represents a single product with its details.

    Attributes:
        name (str): The name of the product.
        product_id (str): The unique identifier for the product.
        price (float): The price of the product.
        stock (int): The available quantity in stock.
    """
    def __init__(self, name: str, product_id: str, price: float, stock: int):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.stock = stock

    def __repr__(self) -> str:
        if self.stock > 0:
            return f"<Product: {self.name} (ID: {self.product_id}), Price: ${self.price}, Stock: {self.stock}>"
        else:
            return f"<Product: {self.name} (ID: {self.product_id}), Price: ${self.price} (Out of Stock)>"

class ShoppingCart:
    """     
    Attribute:
        Set "product_list" as a dict.
        example: product_list = {'P001': {'product': <Product Object>, 'quantity': 2}}

    Funtions of ShoppingCart:
        1. Add product
        2. Calculate total prices
        3. Remove and add products (if adding same products, should update its amount,
        instead of adding another product in list)
    """

    def __init__(self):
        self.product_list = {}

    def add_product(self, product: Product, quantity: int = 1) -> None:
        p_id = product.product_id

        if p_id in self.product_list:
            self.product_list[p_id]['quantity'] += quantity
            print(f"updated {product.name} quantity to {self.product_list[p_id]['quantity']}")
        else:
            self.product_list[p_id] = {'product': product, 'quantity': quantity}
            print(f"Added {quantity} {product.name}s into shopping cart successfully.")

    def remove_product(self, product_id: str, quantity: int = 1) -> None:
        if product_id in self.product_list:
            self.product_list.pop(product_id)
            print(f"{product_id} has been removed from shopping cart")
        else:
            print(f"{product_id} does not exist in the shopping cart")

    def calculate_total(self) -> float:
        total_price = 0
        for products in self.product_list.values():
            total_price += products['product'].price * products['quantity']
        return total_price

    def __repr__(self):
        num_items = sum(item_data['quantity'] for item_data in self.product_list.values())
        num_unique_products = len(self.product_list)
        total_value = self.calculate_total()
        return f"<ShoppingCart: {num_unique_products} unique products, {num_items} total items, Total: ${total_value:.2f}>"

if __name__ == "__main__":
    laptop = Product("laptop", "P001", 1200.00, 10)
    mouse = Product("mouse", "P002", 25.50, 50)
    keyboard = Product("keyboard", "P003", 75.00, 20)


    my_cart = ShoppingCart()

    print("--- 🧪 測試 add_product 方法 ---")
    my_cart.add_product(laptop, 1)
    my_cart.add_product(mouse, 2)
    my_cart.add_product(laptop, 1) # 再次加入筆電，應該更新數量
    my_cart.add_product(keyboard, 3)
    my_cart.add_product(mouse, 1) # 再次加入滑鼠，應該更新數量

    print(f"\n目前購物車狀態: {my_cart}")
    print(f"購物車總金額: ${my_cart.calculate_total():.2f}")

    print("\n--- 測試移除商品 ---")
    my_cart.remove_product("P001", 1)
    print(f"\n移除商品後購物車狀態: {my_cart}")
    print(f"移除商品後總金額: ${my_cart.calculate_total():.2f}")