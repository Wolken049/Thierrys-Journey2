Score = int(input("Please enter your score: "))

if Score >= 80:
    grade = "A"
elif Score >= 60:
    grade = "B"
else:
    grade = "C"

print(grade)