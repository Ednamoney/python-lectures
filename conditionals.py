#if statement
a=10
b=5
if(a==b):
    print("Edna is a big DevOps Engineer!")
else:
    print("Clovis is a bigger Engineer") #It is true cos the fisrt condition failed so it will print out this condition
if(a!=b):
    print("Edna is a big DevOps Engineer!") #is true and will print cos a!= means a is not equal to b (practorial) 
else:
    print("Clovis is a bigger Engineer")

#three statements with elif
x,y=20,40
if(x>y):
    print(x,"is greater than",y)
elif x==y:
    print("x and y are equal")
else:
    print("y is greater than x") # is true and will print this condition