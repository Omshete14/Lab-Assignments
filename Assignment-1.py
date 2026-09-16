students = {
    101: ("Ansh", "CSE", 62),
    102: ("Aarav", "ECE", 71),
    103: ("Piyush", "EEE", 62)
}
roll_list = list(students.keys())
print("Initial Records")
print(students)

#1. Add record
students[104] = ("Rohan", "Mech", 55)
roll_list.append(104)

#2.Delete record
del students[103]
roll_list.remove

#3. Update record
students[102] = ("Purushottam", "CSE", 77)

print("\n Final list after Append, update, Delete:")
for roll in students:
    record = students[roll]
    name = record[0]
    branch = record[1]
    marks = record[2]


print(f"Roll. No:{roll}, Name:{name} , Branch:{branch}, Marks:{marks}")

print("Roll Number List:",roll_list)
