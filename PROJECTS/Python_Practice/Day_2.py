# 18 years allowed for driving and vote
# 16 years allowed to drive but not vote
age = int(input("Please Enter Your Age: "))


if age>=18:
    print("you are allowed for vote and driving")
if age>=16 and age<18:
    print("you are allowed to drive but not for vote")
else:
    print("you are not allowed for vote and driving")