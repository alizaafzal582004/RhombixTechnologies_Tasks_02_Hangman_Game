x = 10   # Global

def outer():
    x = 20   # Enclosing
    def inner():
        x = 30   # Local
        print(x) # prints Local (30)
    inner()
    print(x)     # prints Enclosing (20)

outer()
print(x)         # prints Global (10)


