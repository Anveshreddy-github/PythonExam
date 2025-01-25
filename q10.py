def input_amount():
    total_amount=float(input("enter total amount to be splitted:"))
    num_of_people=int(input("enter toatl number of people:"))
    tips=float(input("enter any extra tips:"))
    return total_amount,num_of_people,tips

def calculation(total_amount,num_of_people,tips):
    amount_each_person=(total_amount + tips)/num_of_people
    print(f"The amount each person as pay is : {amount_each_person}")

def main():
    (total_amount,num_of_people,tips)=input_amount()
    calculation(total_amount,num_of_people,tips)
main()