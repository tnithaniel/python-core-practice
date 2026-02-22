num = int(input("Enter a number : "))

if num == 0:
    print("Factorial is :", 1)
else:
    res = 1
    for i in range(1, num + 1):
        res *= i
    print("Factorial is :", res)