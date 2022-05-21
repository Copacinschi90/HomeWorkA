employee_shift = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]
print("Old employee list : " + str(employee_shift))

new_employees = [item.replace("Kelly", "Maria") for item in employee_shift]

print("The list after substring replacement : " + str(new_employees))