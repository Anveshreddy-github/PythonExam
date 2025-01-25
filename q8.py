def multiplication_table(num,start,end): #multiplication logic
    for i in range(start,end + 1):
        print(f"{num} x {i} = {num * i} ")

def main():
    print("enter only positive numbers")
    num=int(input("enter the number to generate multiplication:"))
    start=int(input("enter the starting range:"))
    end=int(input("enter the ending range:"))
    if end < start:
        print("invalid try again")
    multiplication_table(num,start,end)
main()