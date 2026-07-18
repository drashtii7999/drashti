#Arbitrary Arguement(*args)

def addition(a,b,c):
    return a+b+c
print(addition(10,20,30))

def addition(*args):
    total=0
    for i in args:
        total +=i
        return total
print(addition(10,20,30,40))

#Keyword Arguments

def student(**kwargs):
    print("Student Details")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
student(name="Drashti", age=18,city="Surat",course="Python")


#Documetation string
def rectangle(length,width):
    """
function name=Rectangle
purpose:
       Calculate rectangle area
parameter:
length:int
width:int

result:
     Area of recatngle
     """
    return length * width
print("Area:", rectangle(10,20))
print("Document:", rectangle.__doc__)

#Lambda with map()

numbers =[10,15,20,25,30,35]
result=list(map(lambda x:x**2,numbers))
print(result)

#Lambda with filter()

#EVEN
numbers =[10,15,20,25,30,35]
even=list(filter(lambda x:x%2==0,numbers))
print(even)

#ODD
numbers =[10,15,20,25,30,35]
odd=list(filter(lambda x:x%2!=0,numbers))
print(odd)

#Global Keyword
count=0
def increment():
    global count
    count +=1
increment()
increment()
print(count)

#Multiple return values
 
def calculation(a,b,c):
    total=a + b + c
    average =total / 3
    maximum =max(a , b , c)
    minimum=min(a , b , c)
    return total, average, maximum, minimum
total, average, maximum, minimum = calculation(10 , 20 , 30)
print(total)
print(average)
print(maximum)
print(minimum)


#Lambda with reduce

from functools import reduce
numbers=[1 , 2 , 3 , 4 , 5]
product=reduce(lambda x  ,y:x+y  ,numbers)
print(product)










    











    
     

