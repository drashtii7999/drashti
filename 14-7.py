#list
#Student Management System

print("="*40)
print("Student Management System")
print("="*40)
students=[
{"id":101,"name":"Rahul","Score":78},
{"id":102,"name":"Raj","Score":65},
{"id":103,"name":"Rohan","Score":88},
{"id":104,"name":"Rohit","Score":55}
]
print(students[0]['name'])
print(students[1]['name'])
print(students[2]['name'])
print(students[3]['name'])
print(students)


print("="*40)
print("Print student name using loop")
print("="*40)
for student in students:
    print(student['name'])


print("="*40)
print("Average Score")
print("="*40)
sum=0
for student in students:
    sum += student['Score']
    print(sum)
    average = sum/len(students) 
    print("Average Score:",average)



   
    
