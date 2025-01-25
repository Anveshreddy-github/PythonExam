def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    number = int(input("Enter a number: "))
    print(f"The factorial of {number} is {factorial(number)}")
main()