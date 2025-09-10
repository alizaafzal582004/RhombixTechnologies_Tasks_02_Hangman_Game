name = input("Please enter your name: ")
age = input("Please enter your age: ")
print(f'Your Name is {name} and you are {age} year old ')


text = "Aliza Afzal   "
print(text.strip())
print(text.lower())
print(text.capitalize())

var1 = 10
var2 = 20

var1 , var2 = var2, var1

print(f'var1{var1}' )
print( f'var2{var2}')

a = int(input("Please Enter Your First Value: "))
b = int(input("Please Enter your Second Value: "))

sum = a+b
sub = a-b
power= a**b

print(f'SUM: {sum} and SUB: {sub} and Power: {power}')


num = int(input("Enter Your Number"))

if (num % 2)==0:
    print("Your Number is Even")
if (num%2)==1:
    print("Your Number is Odd")

if (num % 2)!= 0:
    if(num % 3)==0:
        print("Your Number is Odd and Divisible by 3")
    elif(num % 5)==0:
        print("Your Number is Odd and Divisible by 5")
    else:
        print("Your Number is Not Divisible by 3 or 5")
else:
    print("Your Number is Even")

num = int(input("Please Enter Your Value"))

if (num >=0):
    print("Your Value is positive")
if(num<0):
    print("Your Value is Nagetive")
if(num == 0):
    print("You enter zero ")


age = int(input("Please enter yoour age : "))

if (age>=18):
    print("You are eligible to vote ")
else:
    print("You are not eligible to vote")

username = input("USERNAME: ")
password = input("PASSWORD: ")

if username=="admin" and password == "1234":
    print("ACCESS GRANTED ! ")
else:
 print("ACCESS DIEND")


first = int(input("Please enter your first value"))
second= int(input("Enter your second value"))
third = int(input("Enter your third value"))


largest=(max(first, second, third))

print(largest)


if first> second and first>third:
    print(f"The Largest Number is : {first}")
elif first<second and second> third:
    print(f"The Largest Number is : {second}")
else:
    print(f"The Largest Number is : {third}")


total_bill = int(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
each_pays = total_bill / people
print(f"Each person should pay Rs. {each_pays}")

year = int(input("Please enter your birth year: "))

current_year = 2025

age = current_year - year

print(f'you are {age} year old')

chai_type = "Masala Chai"
quantity = 2
ordder = print(f"I want {quantity} cups of {chai_type}.")