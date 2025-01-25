def string_analyzer(string):
    vowels="aeiouAEIOU"
    digits="1234567890"
    vowels_count=0
    digits_count=0
    consonants=0
    special_char=0
    
    for char in string:
        if char in vowels:
            vowels_count+=1
        elif char.isalpha():
            consonants+=1
        elif char in digits:
            digits_count+=1
        else:
            special_char+=1
    
    reversed_string=string[::-1]

    print(f"vowels:{vowels_count}")
    print(f"consonants:{consonants}")
    print(f"digits:{digits_count}")
    print(f"special charaters:{special_char}")
    print(f"reverse of a given string:{reversed_string}")

def main():
    string=input("enter the string to analyzes:")
    string_analyzer(string)
main()