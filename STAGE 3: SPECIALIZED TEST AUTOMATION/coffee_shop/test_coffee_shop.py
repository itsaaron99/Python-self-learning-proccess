from coffee_shop import Coffee, CoffeeShop

def test_take_order_successfully():

    """
    test if take_order can return the price
    setup:
    1. create a Coffee object, e,g large latte, $5.50
    2. create a CoffeeShop object
    3. append the large lattee in to CoffeeShop

    """
    latte = Coffee("Latte", "Large", 5.50)
    my_shop = CoffeeShop("Test cafe")
    my_shop.add_to_menu(latte)

    """
    Test the target method take_order
    """
    total_price = my_shop.take_order("Latte", 2)

    assert total_price == 11.0

def test_take_order_fails_for_nonexistent_item():
    """
    test if ordered non-exist coffee, it will return none
    """
    my_shop = CoffeeShop("Test Cafe")

    result = my_shop.take_order("Mocha", 1)

    assert result is None
    
