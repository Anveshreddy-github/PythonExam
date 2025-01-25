def input_details():
    salary=float(input("enter salary:"))
    age=int(input("enter age:"))
    credit=int(input("enter credit score:"))
    return salary,age,credit

def check_loan_elgibility(salary,age,credit):
    reasons=[]
    if salary < 30000:
        reasons.append("salary is below the reqiured amount for loan")
    if age < 21 or age >65:
        reasons.append("age is not within the eligible range (21-65)")
    if credit < 700:
        reasons.append("credit score is below required score ")
    if not reasons:
        return "Loan Approved"
    else:
        return "Loan Rejected: " + ", ".join(reasons)
    

def main():
    (salary,age,credit)=input_details()
    n=check_loan_elgibility(salary,age,credit)
    print(n)
main()
