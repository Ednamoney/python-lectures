# Calculate total cost
def calculate_total_cost(product_cost,location):
    if location == "US":
        shipping_cost = 5
    elif location == "EUROPE":
        shipping_cost = 7
    elif location == "CANADA":
        shipping_cost = 3
    else:
        shipping_cost = 9
    total_cost = product_cost + shipping_cost
    return total_cost