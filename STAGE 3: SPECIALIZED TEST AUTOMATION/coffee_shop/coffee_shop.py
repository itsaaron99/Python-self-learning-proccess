class Coffee:

    def __init__(self, name: str, size: str, price: float):
        self.name = name
        self.size = size
        self.price = price

    def __repr__(self) -> str:
        return f"<Coffee: {self.size} {self.name}, ${self.price}>"


class CoffeeShop:
    """ 
    represent a coffee shop, with shop name and coffee menu
    """
    def __init__(self, name):
        self.name = name
        self.menu = []
    
    def add_to_menu(self, coffee: Coffee) -> None:
        self.menu.append(coffee)

    def display_menu(self) -> None:
        print(f"--- Welcome to {self.name}! ---")
        print("--- Menu ---")
        if not self.menu:
            print("Sorry, the menu is empty right now.")
            return
        for item in self.menu:
            print(f"- {item.size} {item.name}: ${item.price:.2f}")
        print("------------")

    def take_order(self, coffee_name: str, quantity: int) -> float | None:
        for order in self.menu:
            if order.name == coffee_name:
                total_price = order.price * quantity
                print(f"Order confirmed: {quantity} x {order.name}. Total is ${total_price:.2f}")
                return total_price
        print(f"Sorry, we don't have '{coffee_name}' on our menu.")
        return None

if __name__ == "__main__":
    #add objects of coffee
    latte_m = Coffee("Latte", "Medium", 4.50)
    latte_l = Coffee("Latte", "Large", 5.50)
    americano = Coffee("Americano", "Medium", 3.75)

    #create a coffee shop
    my_shop = CoffeeShop("Gemini's Cafe")

    #adding coffe into menu
    my_shop.add_to_menu(latte_m)
    my_shop.add_to_menu(latte_l)
    my_shop.add_to_menu(americano)

    #test methods
    my_shop.display_menu()

    print("\n--- Taking Orders ---")
    my_shop.take_order("Latte", 2)       # should success
    my_shop.take_order("Mocha", 1)       # should fail
    my_shop.take_order("Americano", 3)   # should success
