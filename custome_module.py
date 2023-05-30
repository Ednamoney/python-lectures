# user define module. this is imported to the test_module
def my_name(name):
    print('My name is', name)
    
# Custome module to check if the number is odd or even
def odd_even(num):
    if num%2==0:
        print(num, 'is an even number')
    else: 
        print(num, 'is an odd number')