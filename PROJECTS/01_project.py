# Fibonacci Generator Program

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Ask user for input
num = int(input("Enter how many Fibonacci numbers to generate: "))

print("Fibonacci Sequence:")
print(fibonacci(num))
