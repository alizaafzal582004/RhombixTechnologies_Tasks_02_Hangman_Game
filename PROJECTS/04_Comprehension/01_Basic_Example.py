# my_list = [ expression for i in range if condition]
#[ (value to store)   for (loop_variable) in (sequence) ]
# SIMPLE SYNTAX
# num  = [ x for x in range(5)]
# print(num)

# #EXPRESSSION

# square = [x**2 for x in range(5)]
# print(square)

# # If i am taking 2  variable exprssson than like A+b

# a,b = 2 , 3
# result = [ a + b for _ in range(6)]
# print(result) # [5, 5, 5, 5, 5]

# a, b = 2, 3
# result = [a + b + x for x in range(6)]
# print(result)   # [5, 6, 7, 8, 9]


# evens = [x for x in range(6) if x%2 ==0 ]
# print(evens)





num = [ x for x in range (1,11)]
print(num)


square = [ x**2  for  x in  range(1,11)]
print(square)


even = [ x for x in range(11) if x%2==0]
print(even)

words = [ "apple", "bnana", "cherry"]
length = [len(words) for words in words]
print(length)
    

words = [ "apple", "bnana", "cherry"]
length = [words.upper() for words in words]
print(length)
    