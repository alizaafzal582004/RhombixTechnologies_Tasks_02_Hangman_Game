import math 
# def circle(radius):
#     # print("hi") do execute
#     return math.pi* radius ** 2
#     # print("hi") dont execute ....
# # print("hi") do execute

# print(circle(2))


# def circum(radius):
#     return 2*math.pi*radius
# print(circum(5))


# def circle(radius):
#     area = math.pi * radius**2
#     circum = 2 * math.pi * radius
#     return area,circum
# print(circle(2))


def circle(radius):
    area = math.pi * radius**2
    circum = 2 * math.pi * radius
    return area,circum
a,c=circle(2)

print(a ,"and", c)