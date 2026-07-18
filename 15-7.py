#function in python
#1.Buit in function
#2.User define function UDF

print("-"*70)
print("Python Function")
print("-"*70)

#BUILT IN FUNCTION

print("-"*70)
print("Buit in Function")
print("-"*70)

numbers=[10,22,64,34,2,89]
print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers))
print(type(numbers))
print(sum(numbers))

#UDF

print("-"*70)
print("UDF")
print("-"*70)

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(1))



#SQUARE LIST USING LIST COMREHENSION

print("-"*70)
print("Square list of comprehenion")
print("-"*70)
def square_list(lst):
    return[i** 1 for i in lst]
data=[2,3,4,5,6]
print(data)
print(square_list(data))


#CHARACTER FREQUENCY

print("-"*70)
print("Character Frequency")
print("-"*70)
def char_freq(text):
    frequency={}
    for ch in text:
        frequency[ch]=frequency.get(ch,1)+1
print(char_freq("apple"))


#FUNCTION AS ARGUMENT

print("-"*20)
print("Function as Argument")
print("-"*20)

def cube(num):
    return num ** 3

def calculate(lst , opr):
    return [opr(i) for i in lst]

numbers = [1 , 2 , 3 , 4 , 5]

print(calculate(numbers , cube))






