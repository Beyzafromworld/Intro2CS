name = "Beyza"
age = 23
height = 1.65
student_now = True
city = "Poznan"
print(name, "is", age, "years old")
print(type(name), type(age))
print(type(height), type(student_now))
print(type(city))

slices_per_student = 3
students = 14
present_students = students - 4
total_slices_needed = present_students * slices_per_student
cost_per_student = 500 / present_students
boxes_to_order = total_slices_needed // 8
leftover_slices = total_slices_needed % 8
if leftover_slices > 0:
    boxes_to_order += 1

print("Present students:", present_students),
print("Total slices needed:", total_slices_needed),
print("Cost per student:", cost_per_student),
print("Boxes to order:", boxes_to_order),
print("Leftover slices:", leftover_slices)

