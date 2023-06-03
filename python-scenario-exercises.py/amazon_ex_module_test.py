# Calculate total
from amazon_ex_module import calculate_total_cost
product_cost=float(input('Enter the product cost:'))
location=input('Enter your location (US, Europe, Canada, Other):')
total_cost=calculate_total_cost(product_cost, location)
print('You have to pay $',total_cost) 