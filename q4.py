def input_student_details():  #used for taking input
    name = input("Enter student name: ")
    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject out of 100 {i}: "))
        marks.append(mark)
    return name, marks

def calculate_total_marks(marks): #adding all marks
    return sum(marks)

def calculate_percentage(total_marks):# calculating percentage
    return (total_marks / 500) * 100

def determine_grade(percentage):#determinig grade
    if percentage >= 85:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'Fail'

def display_results(name, total_marks, percentage, grade): # dispaly the result
    print(f"Student Name: {name}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

def main():
    name, marks = input_student_details()
    total_marks = calculate_total_marks(marks)
    percentage = calculate_percentage(total_marks)
    grade = determine_grade(percentage)
    display_results(name, total_marks, percentage, grade)

main()