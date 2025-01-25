def separate_odd_even(numbers):
    odd_numbers = []
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
        else:
            odd_numbers.append(n)
    return odd_numbers, even_numbers

def main():
        user_input = input("Enter a list of numbers separated by spaces")
        numbers = list(map(int, user_input.split()))
        odd_numbers, even_numbers = separate_odd_even(numbers)
        print(f"Odd numbers: {odd_numbers}")
        print(f"Even numbers: {even_numbers}")
main()