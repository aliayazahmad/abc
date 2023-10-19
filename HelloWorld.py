# this the fisrt code
print("Hello World")

# this is if, elif, and else part
Affan_Age = 5
Age_at_kindergarten = 5

if Affan_Age < Age_at_kindergarten:
    print("Affan shuld be in pre-school")
elif Affan_Age == Age_at_kindergarten:
    print("Enjoy kindergarten")
else:
    print("Affan should be in another class")

# this is def part
def print_youtube():
    text = "I want to start my youtube channel"
    print(text)
    print(text)
    print(text)

print_youtube() 

def print_food(text):
    print(text)
    print(text)
    print(text)

print_food("I wnat to start food vlogging channel")

# def with if, elif, and else
def school_age_calculater(age,name):
    if age < 5:
        print("Enjoy the Time!", name, "is only", age)
    elif age == 5:
        print("enjoy kindergarten", name)
    else:
        print("they grow up so fast")

school_age_calculater(5, "Affan")                

# How to return the vlaue form a function
def add_ten_to_age(age):
    new_age = age + 10
    return new_age

How_Old_Will_I_Be = add_ten_to_age(5)
print(How_Old_Will_I_Be)

#while loop
x=0
while (x<5):
    print(x)
    x=x+1

#For loop
for x in range(5, 10):
    print(x)   

days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

for d in days:
    print(d)
    
for d in days:
    if(d=="Thu"):break
    print(d)

for d in days:
    if(d=="Thu"):continue
    print(d)

# library
import math
print("pi is", math.pi)