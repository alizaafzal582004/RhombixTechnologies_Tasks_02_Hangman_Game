password = "ali@1234"

if len(password) < 6:
    print(" passwordh strength is weak")
elif len(password) <= 10:
    print(" password strength is medium")
elif len(password) > 10:
    print("Password strength is Strong")
    
