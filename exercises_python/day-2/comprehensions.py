marks=[30,46,49,80,80]
bonus= [mark + 5 for mark in marks if mark>40]
print(bonus)

#check pass or fail
marks = [75, 35, 82, 20,20]

results = ["Pass" if mark >= 40 else "Fail" for mark in marks]
print(results)

#with name-
students = {
    "Rahim": 80,
    "Karim": 35,
    "Ayesha": 92
}

grades = {
    name: "Pass" if mark >= 40 else "Fail"
    for name, mark in students.items()
}

print(grades)

#set comprehension {} is used
marks = [80, 70, 80, 90, 70]

unique_marks = {mark for mark in marks}
print(unique_marks)

