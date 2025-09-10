shop = []
print("WELCOME TO OUR SHOPE")

buy=input("What do you want to buy? ")
# item_list=list(map(str,buy.split(",")))
shop.append(buy)

print(shop)

buy=input("What else do you want to remove? ")

shop.remove(buy)
print(shop)

buy = input("do you want to view your list ? (yes/no): ")
if buy=="yes":
    print("Your shopping list is: ")

    print(shop)

else:
    print("Thank you for shopping with us!")










# #LIST METHODDS
# #1.APPEND
# fruits = ["apple", "banana"]
# fruits.append("cherry")
# print(fruits)  # ['apple', 'banana', 'cherry']
# #2.INSERT
# fruits.insert(1, "mango")
# print(fruits)  # ['apple', 'mango', 'banana', 'cherry']
# #ENTEND
# fruits.extend(["grape", "orange"])
# print(fruits)  # ['apple', 'mango', 'banana', 'cherry', 'grape', 'orange']
# #REMOVE 
# fruits.remove("banana")
# print(fruits)  # ['apple', 'mango', 'cherry', 'grape', 'orange']
# #3.POP
# last = fruits.pop()
# print(last)    # 'orange'
# print(fruits)  # ['apple', 'mango', 'cherry', 'grape']
