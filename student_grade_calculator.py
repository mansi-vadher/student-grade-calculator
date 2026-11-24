print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
m4 = float(input("Enter marks for Subject 4: "))
m5 = float(input("Enter marks for Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n===== Result =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if m1 < 35 or m2 < 35 or m3 < 35 or m4 < 35 or m5 < 35:
    print("Result: Fail")
    print("Grade: F")
elif percentage >= 90:
    print("Result: Pass")
    print("Grade: A")
elif percentage >= 80:
    print("Result: Pass")
    print("Grade: B")
elif percentage >= 70:
    print("Result: Pass")
    print("Grade: C")
elif percentage >= 60:
    print("Result: Pass")
    print("Grade: D")
else:
    print("Result: Pass")
    print("Grade: E")