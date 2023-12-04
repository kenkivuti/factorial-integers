# code for a function that receives an integer and returns the factorial of the integer


def factorial(n):
    if n < 0:
        return ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("enter a number : "))
result = factorial(number)
print(f"The factorial of {number} is {result}")