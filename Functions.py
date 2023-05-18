# Fuction without a Parameter
# Example 1
def my_name():
    print('Welcome to Compudemy Edna')
my_name() # used to call the function
print(my_name()) # calling the function using the print statement (parameterless function)

# Example 2
def my_profession():
    print('My name is Edna, I am a DevOps Engineer')
my_profession()
print(my_profession())

# Function with Parameter
# Example 3
def course_func(name, age):
    print('My name is',name, 'I am' ,age, 'years old')
course_func('Edna', 10)

# Example 4
def course_func(name, address, age):
    print('My name is', 'I live in', 'I am 15 years old')
    
def my_credentials(name, address, birthday):
    print('Hello', name, 'Welcome to Compudemy')
    print('I live in', address)
    print('I was born', birthday)
my_credentials('Edna', 'Minnesota', 'December 20 1999')

# Example 5
# propose a function that takes 2 parameters that checks if a numbers are divisible by each other 
# i.e if the remainder is equal to zero (odd or even)
def check_odd_even(num):
    if num%2==0:
        print(num, 'is an even number')
    else:
        print(num, 'is odd')
check_odd_even(30)
def divisibility(x,y): # Check divisibility
    if x%y==0:
        print(x, 'is divisibleby', y)
    else:
        print(x, 'is not divisibly by', y)
divisibility(7456, 11)