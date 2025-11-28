order = ["ram", "ssd", "monitor"]

stock = {
    "ram": 6,
    "ssd": 0,
    "monitor": 32,
    "power_supply": 15,
    "keyboard": 20
}

prices = {
    "ram": 55,
    "ssd": 90,
    "monitor": 220,
    "power_supply": 35,
    "keyboard": 25
}

def compute_bill(order):
    """Calculates the total price for the given hardware list,
    only billing items that are in stock, and updates the stock accordingly."""
    total = 0
    for x in order:
        if x in prices and x in stock and stock[x] > 0:  # Check validity
            total += prices[x]
            stock[x] -= 1
    return total
