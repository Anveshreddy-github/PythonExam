def password_strength_checker(string):
    digits="1234567890"
    string_length=len(string)
    digits_count=0
    uppercase_count=0
    lowercase_count=0
    specialchar=0
    
    if string_length < 8:
        print("password is weak")
        return
    
    for char in string:
            if char in digits:
                digits_count+=1
            if char.isupper():
                uppercase_count+=1
            if char.islower():
                lowercase_count+=1
            else:
                specialchar+=1

    if digits_count > 0 and uppercase_count > 0 and lowercase_count >0 and specialchar > 0:
        print("password is strong ")
    else :
        print ("password is weak")

def main():
    string=input("enter password:")
    password_strength_checker(string)
main()

