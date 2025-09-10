
# Task 1 – Basic Function
# Write a function called welcome_message() that prints “Welcome to Python Functions Practice!”. Call the function.

def welcome_message():
    print("Welcome to Python")

welcome_message()

# Task 2 – Function with Multiple Parameters
# Create a function called student_info(name, age) that prints a student’s name and age. Call it with at least two different sets of arguments.


def student_info(name,roll_no):
    # name = "aliza"
    # roll_no = 9001
    return name,roll_no

print(student_info("aliza",9001))




# Task 3 – Polymorphism

# Create a function multiply(x, y) that works with both numbers and strings.

# Example: multiply(3, 5) → 15

# Example: multiply("Hi", 3) → "HiHiHi"

# Try multiply("Hi", "Hello") and note the error.




def Multiply(a,b):
    return a*b
print(Multiply("alizay",6))
print(Multiply(3,5))
#print(Multiply("aliza","afzal"))



# Task 4 – Multiple Return Values

# Write a function math_operations(a, b) that returns:

# Sum of a and b

# Difference of a and b

# Product of a and b
# Print the results separately.





def math_operations(a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    return sum , sub , mul 
math_operations(1,3)

    

cube = lambda x: x**3
print(cube(3))


add = lambda a, b: a + b
print(add(5, 7))   # 12

    


