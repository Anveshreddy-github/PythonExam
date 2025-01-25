def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort()  # Sort the list
    return unique_numbers[-2]  # Return the second last element

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    second_largest = find_second_largest(numbers)
    if second_largest is None:
        print("The list must contain at least two distinct numbers.")
    else:
        print(f"The second largest number is: {second_largest}")
main()