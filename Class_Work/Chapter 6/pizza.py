def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\n Making a {size}-inch pizza with the following {len(toppings)} toppings:")

    for topping in toppings:
        print(f"- {topping}")