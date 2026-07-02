'''

#String manipulation in python

s1 ='Hellow'
s2 ='World'
s3 =''Multi line String''
s4 = r" Raw /n String"
print(s1)
print(s2)
print(s3)
print(s4)
'''
#Common string method
s = "    Hello  , World!   "
result = s.upper()
print(result)
result = s.lower()
print(result)
result = s.strip()
print(result)
result = s.lstrip()
print(result)
result = s.rstrip()
print(result)
result = s.replace("World ","Python")
print(result)
result = s.split(",")
print(result)
result = s.find("World")
print(result)
result = s.find("hello")
print(result)
result = s.count('Hello')
print(result)
result = s.startswith("    He")
print(result)
result = s.endswith("d!   ")
print(result)

#String formating
name = "drashti"
age = 18
#f string 
print(f"name : {name} , age : {age}")
#format()
print("name : %s , age : %d " % (name , age))

#Padding & Alignment
print(f"{name:<10}")
print(f"{name:>10}")
print(f"{name:^10}")
print(f"{3.143234:2f}")


#slicing
s = "Hellow world!"
print(s)
print(s [3] )
print(s [-1] )
print(s [0:5] )
print(s [:7])
print(s [:5] )
print(s [:2] )
print(s [::-1])

# Joining and spliting

words = ["Python","is","Programing","Language!" ]
print(" ".join(words))
print("_".join(words))

#spliting
s = "a,b,c,d"
result = s.split(" , ")
print(result)

















