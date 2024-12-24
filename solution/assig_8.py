def print_pattern(n):
    for i in range(n):
        increasing_part = ''.join(chr(65 + j) for j in range(i + 1))
        decreasing_part = ''.join(chr(65 + j) for j in range(i - 1, -1, -1))
        print(' ' * (n - i - 1) + increasing_part + ' ' + decreasing_part)
n = int(input("Enter the value of n: "))
print_pattern(n)
