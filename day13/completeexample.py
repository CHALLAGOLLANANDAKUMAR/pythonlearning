name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
age = int(input("Enter Age: "))
branch = input("Enter Branch: ")
college = input("Enter College Name: ")
cgpa = float(input("Enter CGPA: "))
print("Name      :", name)
print("Roll No   :", roll)
print("Age       :", age)
print("Branch    :", branch)
print("College   :", college)
print("CGPA      :", cgpa)

print("\nEligibility")
print("Age >= 18 :", age >= 18)
print("CGPA > 7.5:", cgpa > 7.5)

if age >= 18 and cgpa >= 7.5:
    print("Status: Eligible for Campus Placement")
else:
    print("Status: Not Eligible for Campus Placement")
