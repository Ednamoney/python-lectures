"""
Exercise 3
You want to buy something from Amazon. The seller charges different prices for shipping cost
based on location. For US it's 5$ for Europe it's 7$ for Canada it's 3$ for other places it's 9$
Create a program that:
● Reads the cost of the product
● Reads your location
● Print the amount of money you have to pay
Ouput: "You have to pay 23$, 20$ for the product and 3$ for shipping cost
"""

product_cost=float(input('Enter the product cost:'))
location=input('Enter your location (US, Europe, Canada, Other):')
if location.upper()=='US': # the '.upper' does not limit the user form inputing lower/upper cases for the countries
    shipping_cost=5
elif location.upper()=='EUROPE': # you define a method within a class and invoke them on either a variable or data
    shipping_cost=7
elif location.upper()=='CANADA': # methods and functions are used interchangeably
    shipping_cost=3
else:
    shipping_cost=9
total_cost=product_cost+shipping_cost
print(total_cost)