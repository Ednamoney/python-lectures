#Create two variables x and y, and initially set them each to a different number. Write a python script that swaps both values.

#Example: x = 10, y = 20
#Output: x = 20, y = 10

# Solution

# Method 1:Using swap variables as a temporary value
x=int(input('Enter the value of x:'))
y=int(input('Enter the value of y:'))
print('The values of x and y before swapping is:', x,y)
s=x
x=y
y=s
print('The value of x is:', x)
print('The value of y is:',y)

# Method 2: without using swap variable

x=int(input('Enter the value of x for method 2:'))
y=int(input('Enter the value of y for method 2:'))

x,y=y,x

print('The value of xis:',x)
print('The value of y is:',y)

# Method 3: Using a Function
# swap=0
def swap_value(x,y):
    swap=x
    x=y
    y=swap
    return x,y
numbers=swap_value(
    int(input('Enter the value of x for method 3:')),
    int(input('Enter the value of y for method 3:'))
)
print(numbers)
