#conditional statements
x = 10
y = 50

print(x)

#snakecasing
my_city = "Nairobi"
my_favourite_sport = "Hockey"

#camelcasing
myOldestCar = "Suzuki"

name = "Rodney"
age = 22

#Types of data
#numbers
height = 3 #integer
weight = 60.45 #float
#strings
full_name = "Jack Kim"
distance = "45"
#boolean
is_listed= True
is_disabled = False

# conditional statements
password = "123456"
db_password = "654321"

if password == db_password:
    print("Success")
else:
    print("Failed")

score = 15
if score >= 90:
    print("A")
elif score >= 80 and score<=89:
    print("A-")
elif score >= 75 and score <= 79:
    print("B+")
elif score >= 70 and score<=74:
    print("B")
elif score >= 65 and score<=69:
    print("B-")
elif score >= 60 and score<=64:
    print("C+")
elif score >= 55 and score<=59:
    print("C")
elif score >= 50 and score<=54:
    print("C-")
elif score >= 45 and score<=50:
    print("D+")
elif score >= 40 and score<=44:
    print("D")
elif score >= 35 and score<=40:
    print("D-")
else:
    print("E")
