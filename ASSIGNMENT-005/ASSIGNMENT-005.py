###         ASSIGNMENT-005
###    MODULE 6: DATA STRUCTURES AND STRINGS IN PYTHON


# TASK-1:CREATE A DICTIONARY OF STUDENT MARKS

# DICTIONARY
my_dict = {
    'Alice': 85,
    'Mike': 60,
    'Jack': 29}

# CODE
name =input("ENTER YOUR NAME(Alice,Mike,Jack):  ")

if name in my_dict:
    print(f"{name}'s marks =  {my_dict[name]} ")
else:
    print("Student not found.")


### TASK-2:DEMONSTRATE LIST SLICING

original_list = {1,2,3,4,5,6,7,8,9,10}
#                0 1 2 3 4 5 6 7 8 9
extended = original_list[0:4]
reversed = original_list[::-1]

print(f"ORIGINAL LISTS: {original_list}")

print(f"EXRACTED FIRST FIVE ELEMENTS : {extended}")

print(f"REVERSED EXTRACTED ELEMENTS: {reversed}")









