#Excercise 1
#Propose a script that checks if a number is divisible by 2.
#If the number is divisible by 2 it should print “hey this number is divisible by 2”  otherwise it should print “hey this number is not divisible by 2”

#Solution

a=60
if(a/2):
    print(a,"is divisible by 2") #is true cos 60 can be divided by 2 evenly
else:
    print(a,"is not divisible by 2")

a=61
if(a%2==0): # % means modulus
    print(a,"is divisible by 2")
else:
    print(a,"is not divisible by 2") #is false 
    
    #Exercise 2
    #Write an if statement that asks for the user's name via input() function.
    #If the name is “Acha” make it print "Welcome on board Acha” Otherwise make it print "Good morning Engr. Akum”
    
    #Solution
    name=str(input("enter any name:"))
if(name=="Acha"):
    print("Welcome on board Acha")
else:
    print("Good morning Engr.", name)