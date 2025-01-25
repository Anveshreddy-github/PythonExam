def is_palindrome(value):
    # Convert the value to string
    str_value = str(value)
    # Check if the string is equal to its reverse
    return str_value == str_value[::-1]

def main():
        user_input = input("Enter a string or postive number to check for palindrome ")
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome.")
        else:
            print(f"'{user_input}' is not a palindrome.")
main()
