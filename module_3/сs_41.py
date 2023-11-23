price_bread = 20
price_butter = 70
price_sugar = 40


def actual_price(item, discount: float = 0):
    return item * (1 - discount)


def percent_value(discount):
    return discount * 100


print(f"Previous price on bread {price_bread}, new price {actual_price(price_bread)}, "
      f"with {percent_value()}% discount")
print(f"Previous price on butter {price_butter}, new price {actual_price(price_butter, 0.35)}, "
      f"with {percent_value(0.35)}%discount")
print(f"Previous price on sugar {price_sugar}, new price {actual_price(price_sugar, 0.05)}, "
      f"with {percent_value(0.05)}%discount")
