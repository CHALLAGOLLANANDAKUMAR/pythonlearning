name = input("Enter Student Name: ")

sub1 = int(input("Subject 1 Marks: "))
sub2 = int(input("Subject 2 Marks: "))
sub3 = int(input("Subject 3 Marks: "))

total = sub1 + sub2 + sub3
average = total / 3

print("\n RESULT")
print("Student Name :", name)
print("Total Marks :", total)
print("Average :", average)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade :", grade)

if average >= 35:
    print("Status : PASS")
else:
    print("Status : FAIL")
