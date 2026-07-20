#Array
#1.Homogenous Array - contain element of same datatype
#Example
numbers =[10 , 20 , 30 , 40 , 50]
print(numbers)
#2.Heterogenous Array - contain element of multiple data type
#Example
mixed =[10 , 20 ,"Drashti",True]
print(mixed)

#Common Typecodes
'''
"i"= int
"f"= float
"d"= duplicate
"u"= unicode character
'''
'''
#Syntax
#arrayidentifiername = array[typecode , [intialize]]
from array import*
numbers = array["i",[10 , 20 , 30 , 40 ,50]]
print(numbers)
'''
'''
#Using for loop + appened()
#Ask the users to enter all element in one of the array defined by user
#Ask the user how many element they want to enter
#Create an empty list
#Use a for loop to take user input
#Store each element using appened()

size = int(input("Enter size of array :"))
numbers = []
for i in range (size):
    value = int(input(f"Enter element {i + 1}:"))
    numbers.append(value)
    print(numbers)
    '''
'''
#Using Map() + split()
numbers = list(map(int,input("Enter array elements :").split()))
print(numbers)
'''
#List Comprehension
size = int(input("Enter size of array :"))
numbers =[int(input("Enter array element "))for  i in range(size)]
print(numbers)





























