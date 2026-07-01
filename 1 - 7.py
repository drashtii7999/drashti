#If statement
age = 20
if(age >= 18):
    print("Adult")

#if...else statement
    age = 20
    if(age >= 18):
        print("Adult")
    else:
        print("Minor")

#Voting programme
age = 18
card = True
if(age >= 18 and card == True):
     print("You are eligable for vote")

#if...elif...else statement

marks = 90
if (marks >= 90):
   print("Grade A")
elif(marks >= 75):
   print("Grade B")
elif(marks >= 60):
   print("Grade C")
else:
    print("Fail")

#Match case statement

day = 1
match(day):
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
'''
#Looping Control Flow
 #While condition:
 #code block

num = 1
while num <=10:
     print(f"while {num}")
     num +=1

num = 10
while num >= 1:
    print(f"while {num}")
num -=1
'''
#for loop

for i in range(1,11):
    print(f"for loop {i}")

for i in range(10):
    print(f"for loop {i}")

for i in range(1,11,2):
    print(f"for loop {i}")

#Break , Continue & Pass statement

for i in range(1,11):
    if i ==5:
        break;
    print(i)

for i in range(1,11):
    if i == 4:
        continue;
    print(i)

for i in range(1,11):
    if i == 3:
     pass;
    print(i)

    

    



















 

        




        

     
        
    
     
     
     
    
