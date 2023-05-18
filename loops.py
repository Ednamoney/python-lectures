#Loops in Python
#for loop
for num in range(1,11): # this will print from 0 to 9 and (1,10) will print 1 to 9 and (1,11) will print 1 to 10
    print(num)
    
#example2 for loop with strings
name="Edna"
for i in name:
    print(i)
        
#looping with list
students=["akum","edna","elizabeth","happiness", "richard","mary"]
ages=[1,2,3,4,5]
for i in students:
            print(i)
for i in ages:
    if i==4:
     print("hey welcome") # only 4 will print 'hey welcome' cos 4==4 (equality operator)
    else:
     print("welcome") # 1,2,3, and 5 will print 'welcome' cos they are not equal to 4
                
#example3
for num in range(1,21): # this will print from number 1 to 20
    print(num)
    
#performing sum of first 10 number using for loop (0 to 9)
sum=0 # start counting from zero
for i in range(1,10):
    sum=sum+i # or + 1 #adds 0+0, 1+2+3+4+5+6+7+8+9
print('the sum of the numbers is',sum)

#performing sum of the 20 numbers using for loop (1,21)
sum=1
for i in range(1,21):
    sum=sum+i
print('the sum of the number is',sum)


#python program to illustrate while loop
count=1 #means it starts printing from 1 and if count is 0, it will start printing from zero
#while(count<3):
    #count=count+1
    #print('Hey Edna') # this will print twice cos 1 is less than 3 and 2 is also less than 3 and you start count from 1
while(count<5): count+=1; print('Hey Edna Welcome') # another way of using a while loop in a straight line 

eddy=1
while(eddy<5):
    print('hello')
    eddy=eddy+1
    
#printing in decending order in while loop e.g from 10 to 1 instead of 1 to 10 we have to use - instead of +
count=10
while count>=1:
    count-=1
    print(count)
        
#Excesise 
#print odd and even numbers between 0 to 10 using for loop
for i in range(1,11):
 if i %2==0:
    print('even number:',i)
 else:
    print('odd number:',i)   
         
#use a while loop to print odd and even numbers from 10 to 0 
num=11
while num>0:
    if num%2==0:
        print(num, "is even")
    else:
        print(num, "is odd")
    num=num-1

# Write a program that takes a list of numbers and returns the sum of all the even numbers in the list.
num=[1,2,3,4,5,6,7,8,9,10] #number lists
sum=0 # initialize the sum variable
for i in range(1,11):#loop through the list of 10 numbers, add all even numbers and assign their sum to the sum variable
    if i %2==0:
        sum=sum+i
print('The sum of all even numbers is',sum)
    

 # Write a Python program that uses a while loop to repeatedly prompt the user to enter positive numbers, 
 # and stops when the user enters -1
sum=0
while True:
    num=int(input('Enter a positive numer or enter -1 to exit:'))
    if num==-1:
        break
    if num>0:
        sum=sum+num
    else:
        print('Invalid input, enter a positive number')
    print('The sum of the positive number is:', sum)
        
     
 
 
 #Write a program in python that takes a list of numbers and returns the maximum number in the list