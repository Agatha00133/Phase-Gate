number = int(input("Enter a number: "))

factorial = 1

for index in range(1, number + 1):
    factorial *= index

print("Factorial of", number, "is:", factorial)
