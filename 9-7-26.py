print("="*40)
print(" Q1 Set operations")
print("="*40)

numbers = {1 , 2 , 3 , 4 , 5}
print(numbers)
print(type(numbers))

list_1 = [1 , 1 , 2 , 2 , 3 , 4 , 4, 5 , 6 , 6 , 6]
set_1 = set(list_1)
list_2 = list(set_1)
print(list_2)

numbers.add(6)
numbers.remove(3)
print(numbers)

print(2 in numbers)
print(numbers)




print("="*40)
print(" Q2 Union , interaction and difference")
print("="*40)
set_a = {1,2,3,4}
set_b = {3,4,5,6}
print("Union :", set_a . union(set_b))
print("Intersection :", set_a . intersection (set_b))
print("Difference :", set_a . difference (set_b ))




print("="*40)
print("Q3 Dictionary Operation")
print("="*40)
student = {
    "name" :"Drashti",
    "age":18,
    "grade" :"A",
   }
print(student)
print(type(student))
print(student['name'])
for key in student.keys():
    print(key)
    
for value in student.values():
    print(value)
    
for key in student.keys():
    print(f"{key}:{student[key]}")
    
student["city"]="Delhi"
print(student)
student['age']=18
print(student)
del student['grade']
print(student)





print("="*40)
print("Q4 Dictionary from list")
print("="*40)

keys=['id','name','email']
values=[101,'Drashti','drashtipatel7999@gmail.com']
print(len(keys))
user ={}
for i in range(len(keys)):
    user[keys[i]] = values[i]
    print(user)





print("="*40)
print("Q5 Type conversion")
print("="*40)

num='123'
print(type(num))
num_1 = int(num)
print(num_1)
print(type(num_1))

list_1 =[1,2,3,4,5]
tuple_1 =tuple(list_1)
print(type(tuple_1))

list_2 = list(tuple_1)
print(type(tuple_1))
print(type(list_2))

pairs = [(1,'A'),(2,'B')]
dict_1=dict(pairs)
print(dict_1)






print("="*40)
print("Q6 Delete list item using del keyword")
print("="*40)
numbers =[10,20,30,40,50]
print(numbers)
del numbers[0]
print(numbers)





















    

    






    





