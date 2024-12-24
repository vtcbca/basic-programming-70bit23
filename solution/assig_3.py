n = 15
num1 = 0
num2 = 1

# Print the first two Fibonacci numbers
print(num1, num2, end=" ")

# Generate the remaining Fibonacci numbers using a for loop
for _ in range(3, n + 1):
    next_number = num1 + num2
    print(next_number, end=" ")
    num1, num2 = num2, next_number
print()
