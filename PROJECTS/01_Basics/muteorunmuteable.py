# IMMUTABLE (CANNOT BE CHANGED) TYPES IN PYTHON

x = 10
y = x   

print("x:", x)
print("y:", y)

x = 20
print("After changing x:")   #change reference of x..not value of it 
print("x:", x)
print("y:", y)




# string is also immutable
username = "Alizay" 
print("Username:", username)
print( username[0]) ##accessing first character