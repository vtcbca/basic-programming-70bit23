x = "kakak"
is_palindrome = True
for i in range(len(x) // 2):
    if x[i] != x[-(i+1)]:
        is_palindrome = False
        break
if is_palindrome:
    print("yes")
else:
    print("No")
