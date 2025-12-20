list1 = [1,25,46,78,9,78,654,9,565,5465,6256,15]
print(list1)

list1.sort()

# combine two list as key pair value in tuple

std_name = ["Aditya","Neha","kajal","Sahil","Ajay"]
std_marks = [80,99,78,80,75]

combined = list(zip(std_name,std_marks))

print(combined)
combined.sort()
print(combined)

combined.sort(key=lambda x: x[1])
print(combined)


'''zip(names, marks)
Combines elements index-by-index
names[0] → marks[0]
names[1] → marks[1]
lambda x: x[1]
x = one tuple → ('Rahul', 78)
x[1] = marks → 78
Sorting happens using marks only'''