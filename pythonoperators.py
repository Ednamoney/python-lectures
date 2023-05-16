#python assignment operators (checking if it is true or false)
w=10
s=3
print(w)
s+=13 #s=s+13
print(s)
q=10
q-=20 #q=q-20
print(q)
z=9
z/=3
print(z)
p=32
p%=7
print(p)
u=20
u//=3
print(u)

#Python Comparison Operator
x=10
y=4
#equality operator ie use to compare 2 values
print(x==y)

#greater than operator
print(x>y) #is true cos x is greater than y

#greater than or equal to operator
print(x>=y) #is true cos x is 10 and y is 4

#less than operator
print(y<x) #is true y is 4 and x is 10

#less than or equal to operator
print(x<=y) #is false

#Logical Operator (used to combine conditional statements)
foncho=45
richie=30
clovis=10
miriam=20
lizy=5

#the and operator (it returns true only if/when both conditions are true) 
print(richie>foncho and miriam>lizy) #is false cos richie is 30 while foncho is 45 

#the or operator (either one or the other is true)
print(clovis<miriam or lizy>foncho) # is true cos the first condition is true

# the not operator (it negates your statement ie if statement is true it negates/returns to false and vise versa)
print(not(clovis<miriam or lizy>foncho)) #is false. it returns false