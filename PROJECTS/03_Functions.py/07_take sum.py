# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2,3,4,5,6))
# print(sum_all(1,2))
# print(sum_all(1,2,6,8,9,3,0,1,1,9,2,0,0,5))

# def sum_all(*chai):
#     return sum(chai)

# print(sum_all(1,2,3,4,5,6))
# print(sum_all(1,2))
# print(sum_all(1,2,6,8,9,3,0,1,1,9,2,0,0,5))



# def sum_all(*chai):
#     print(*chai)
#     return sum(chai)

# print(sum_all(1,2,3,4,5,6))
# print(sum_all(1,2))
# print(sum_all(1,2,6,8,9,3,0,1,1,9,2,0,0,5))



# def sum_all(*chai):
#     print(chai)# eturns tuple
#     return sum(chai)

# print(sum_all(1,2,3,4,5,6))
# print(sum_all(1,2))
# print(sum_all(1,2,6,8,9,3,0,1,1,9,2,0,0,5))




def sum_all(*chai):
    print(*chai)
    for i in chai:
        print(i*2)
    return sum(chai)

print(sum_all(1,2,3,4,5,6))
# print(sum_all(1,2))
# print(sum_all(1,2,6,8,9,3,0,1,1,9,2,0,0,5))
