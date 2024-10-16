name = input("enter name:")
section = input("enter section:")
#basic info

#start of code
prelim = float(input("Enter Preliminary Period Grade (40-100): "))
if prelim < 40 or prelim > 100:
    print("Error: Preliminary Period Grade must be between 40 and 100.")
else:
    midterm = float(input("Enter Midterm Period Grade (40-100): "))
    if midterm < 40 or midterm > 100:
        print("Error: Midterm Period Grade must be between 40 and 100.")
    else:
        final = float(input("Enter Final Period Grade (40-100): "))
        if final < 40 or final > 100:
            print("Error: Final Period Grade must be between 40 and 100.")
        #if final < 40 or final > 100: ensures that if the number exceed 100 or the number is below 40 it will display a error message
        else:
            # Calculate the final grade
            final_grade = (prelim + midterm + final) / 3
            final_grade_rounded = round(final_grade)

            if final_grade_rounded  >= 99:
                gpa = 1.00
            elif final_grade_rounded  >= 96:
                gpa = 1.25
            elif final_grade_rounded  >= 93:
                gpa = 1.50
            elif final_grade_rounded  >= 90:
                gpa = 1.75
            elif final_grade_rounded  >= 87:
                gpa = 2.00
            elif final_grade_rounded  >= 84:
                gpa = 2.25
            elif final_grade_rounded  >= 81:
                gpa = 2.50
            elif final_grade_rounded  >= 78:
                gpa = 2.75
            elif final_grade_rounded  >= 75:
                gpa = 3.00
            else:
                gpa = 5.00  # Below this is failed

            # Display the final grade & gpa
            print(f"Hi {name} im from {section}!")
            print(f"Final Grade: {final_grade_rounded}")
            print(f"GPA: {gpa:.2f}")