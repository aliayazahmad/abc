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

#list
nums= [12, 13, 14, 15, 16]
print(nums)

# tupel
tup = (12, 13, 14, 15, 16 )
print(tup)
print(tup) #this will show error

#asining value
def inPutcat():
    a = input("")
    b = input("")
    c = input("")
print(a, b, c)

#swap asined value
a,b = eval(input())
b,a = a,b
print(a)
print(b)

#Volume
radius,length = eval(input())
ares_of_base  = radius * radius * 3.14
volume  =  ares_of_base * length
print(round(volume,2))   

#opretors
X, Y = eval(input())
print(X + Y)
print(X-Y)
print(X*Y)
print(X**Y)
print(Y//X)

#average speed in miles per hour
distance_in_km = 14
distance_in_miles = distance_in_km/1.6

time_in_min =  45.5
time_in_hr = time_in_min/60

avg_speed = distance_in_miles/time_in_hr

print(round(avg_speed,2))

#area and perimeter of a rectangle
width = 4.5
height = 7.9
area = (width * height)
print(round(area,2))
perimeter = 2(width + height)
print(round(perimeter,2))

#find last 3 digits of user's phone number
phone_number = input("Enter your phone number: ")
if len(phone_number) >= 3:
    last_three_digits = phone_number[-3:]
    print("Last three digits of your phone number:", last_three_digits)
else:
    print("Invalid input: Phone number should contain at least three digits.")

# what day will that be when you and your frindes are going to meet? 
X = int(input("Enter the number of days: "))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
current_day = 0  # 0 represents Sunday
meeting_day = (current_day + X) % 7
print("You will meet your friend on:", days[meeting_day])

