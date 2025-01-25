def input_bmi():
    weight=float(input("enter weight in kg:"))
    height=float(input("enter height in m:"))
    return weight,height

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight, height = input_bmi()
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")

main()