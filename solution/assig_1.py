def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

number = 15
result = factorial(number)
print("The factorial of", number, "is", result)
