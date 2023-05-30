# check if the number is a prime number or not
# a prime number have two factors i.e is greater than 1 cannot be divided by any whole number but itself but less than 2
def is_prime(num): 
    if num<2:
        return False
    elif num>1:
        for i in range(2, num):
            if num%i==0:
                print('the numer', num, 'is NOT a Prime number')
                break
        else: 
             print('The number', num, 'is a Prime number')
number=is_prime(
    int(input('Enter a number to check if its prime or not:')))
print(number)

# OR
def is_prime(num):
    if num<2:
        return False
    for i in range (2, num):
        if num%i==0:
            return False
    return True