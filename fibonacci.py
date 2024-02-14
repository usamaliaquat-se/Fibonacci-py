# 0622188791

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

 
n = int(input("Enter the value of N: "))
print("The", n, "th Fibonacci number is:", fibonacci(n))