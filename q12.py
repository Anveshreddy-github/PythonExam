def generate_pattern(n, reverse=False):
    if reverse:
        for i in range(n, 0, -1):
            print('*' * i)
    else:
        for i in range(1, n + 1):
            print('*' * i)

def main():
    n = int(input("Enter the number of rows: "))
    reverse = input("Do you want to print the pattern in reverse? (yes/no): ").strip().lower() == 'yes'
    generate_pattern(n, reverse)
main()