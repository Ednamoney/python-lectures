# Propose a function to check a number even and odd

def check_number(num):
    if num%2==0:
        return True
    else:
        return False
# call function
print(check_number(10))



# Local Variables in Function
# A local variable is a variable that is declared inside a function and is not accessible out of that function

def edna():
    a=12
    print('this is a local variable',a) # concatination
def emma():
    b=10
    print('the value is', b)
    
edna() # this is calling the function
emma()

# Global Variables
# A global variable is a variable that is declared outside a function and is accessible anywhere
y1=600
def acha():
    print(y1)
    
acha()

def blaise():
    y2=y1+20
    print(y2-4)
blaise()


# Write a Python function called calculate_factorial that takes a positive integer as input and calculates 
# its factorial using a loop. 
#The factorial of a number n is the product of all positive integers from 1 to n.

def calculate_factorial(n): # a recursive function i.e the function calls itself
    if n==0:
        return 1
    else:
        return n*calculate_factorial(n-1)
print(calculate_factorial(4))

# OR Using procedural programming or iterative procedure (loop)




# Deployment Script with Environment Selection

# The idea is for you to develop a Python script that allows users to select the deployment (e.g development, 
# staging, or production) and performs different actions based on their choices

#use the conditionals to check the selected environment and execute specific deployment tasks accordingly

#This exercise will allow you to practice conditionals, function calls that we studied in the las lecture and code
#organization to automate the deployment process based on user inputs

# propese a function to deply to development environment
def deploy_to_development():
    print('deploying to development')
    
# propse a function to deploy to staging environment
def deploy_to_staging():
    print('deploy to staging environment')

# propose a function to deploy to production environment
def deploy_to_production():
    print('deploy to production environment') 
    
def deploy(environment):
    if environment=='development':
          deploy_to_development()
    elif environment=='staging':
        deploy_to_staging
    elif environment=='production':
        deploy_to_production()
    else:
        print('Its an invalid environment. Please choose either staging, production, or development')
        
# prompt the user for the deployment environment
user_environment=input('enter the deployment environment (development, staging, deployment)')

# call the function with user's choice
deploy(user_environment)


# Assignment Excercise     
# Write a Python script that prompts the user to enter a password and then checks the strength of the password 
# based on predefined criteria. 

# The script should provide feedback on the strength of the password using a combination of conditions and loops.   