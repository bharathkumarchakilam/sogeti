n = int(input("Enter the number of terms: "))

a, b = -1, 1
print("Fibonacci series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b