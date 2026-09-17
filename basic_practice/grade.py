# this is a simple python program to check grade of a student based on their marks.

mark = float(input("Enter your marks: "))

if mark >= 80 and mark <= 100:
    print("You got A+ grade.")
elif mark >= 70 and mark < 80:
    print("You got A grade")
elif mark >= 60 and mark < 70:
    print("you got B grade")
elif mark >= 50 and mark < 60:
    print("You got C grade")
elif mark >= 40 and mark < 50:
    print("You got D grade")
elif mark >= 33 and mark < 40:
    print ("You got E grade")
else:
    print("You got F grade. Better luck next time.")
    