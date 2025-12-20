# list1 = list((58,26,7,4,59,6))
# list2 = list((11,22,33,44,55))
# print(list1) 

# Adding element in the list
'''list1.append(12)
print("Add the element at the end of the list")
print(list1)'''

# list1.insert(0,88)
'''print("Add element at  the specific position")
print(list1)
'''
# list1.extend(list2)
# print(list1)

# list1.sort()
# print(list1)


# #Removing Elements from List
# list1.remove(22)
# print(list1)

# list1.pop(3)
# print(list1)

# del list1[5]
# print(list1)

# for i in list1:
#     print(i)


"""List Comprehension
List comprehension is a concise way to create lists using a single line of code. It is useful for applying an operation or filter to items in an iterable, such as a list or range"""


# Add to list in single list

# newlist = list1.append(list2)
# print(newlist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

'''for i in thislist:
    print(i)
    if i == "cherry":
        print(f"we found {i} at index :",thislist.index(i))
        break;


print(type(thislist))'''



#Range of Negative Indexes  

'''print(thislist[-4:-1])
print(len(thislist))'''


# Python - Change List Items
'''sum = 0
num = [20,40,12,5,897,78,46,49]

    for i in num:
    print(i)
    sum = sum +i

print("sum : ",sum)

print(num)

num[1] = 250
print(num)
'''

'''  thislist[0:2] = ["s_cherry","watermelon"]
print(thislist)
 
''' 
''' thislist.append("cary")
print(thislist) '''

#use for loop to enter item in loop from user.

''' num = int(input("enter the number of items you want to store: "))
list_new = []

for i in range(1,num+1):
    item = input("enter the items : ")
    list_new.append(item)

print(list_new) '''
    

#lets write  a new program 
# This is only for practice.......

'''list1 = []



while(True):
    choice = input("Do you want to add items or if you have done all items then type Done : ")
    items = input("enter the items :")
    list1.append(items)
    if choice == "Done":
        break;



print(list1)

   '''


# take input from user and store in list: 

'''list  = []

while(True):
    choice = input("Type 'add' to add item or 'done' to finish :").lower()

    if choice == "done":
        break;
    
    if choice == "add":
        items = input("enter the items : ")
        list.append(items)
    
    else:
        print("Invalid choice! Please type 'add' or 'done'.")


print("\n This is final list :")
print(list)

'''

# For Loop Version (Ask user how many items they want to add)

'''list1 = []

num = int(input("How many items you want to add: "))

for i in range(num):
    item = input(f"Enter item {i+1}: ")
    list1.append(item)

print("\nYour final list:")
print(list1)'''


# Use of insert() method 
# it use for insert an item in list at specific index

'''list1 = [1,3,4,5,6,7,8,9,10]
list1.insert(-1,2)
print(list1)
'''


# Extend List 

'''Append elements from another list to the current list, use the extend() method.
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).'''


list1 = [1,2,3,4,5,6]
list2 =[11,22,33,44,55,66]

'''list1.extend(list2)
print(list1)

t1 = (1,2,3,4,5)

list1.extend(t1)
print(list1)
'''
# remove items from list and it take only one argument 

'''list1.remove(2)
print(list1)'''


#The pop() method removes the specified index.
'''list1.pop(2)
print(list1)

list1.pop()
print(list1)'''


#The del keyword also removes the specified index:

'''del list1[1]
print(list1)
'''

'''Clear the List
The clear() method empties the list.
The list still remains, but it has no content.'''



thislist1 = ["mango","banana","graphes","apple","watermelon","tomato","kiwi","blueberry","kiwikiss","jelly"]
# thislist1.clear()
# print(thislist1)

'''i = 0
count = 0
while(i<len(thislist1)):
    print("index :",i,"item : ",thislist1[i])
    i = i+1
    count =i+1

print("total items :",count)
'''


#Python - List Comprehension
'''List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:'''


fruits_items = ["apple", "banana", "cherry", "kiwi", "mango","watermelon","graphes","blueberry","strayberry","orang"]

# '''index = 0
# for i in fruits_items:
#     print(index,i)
#     index +=1'''


#list comprehension with use for loop;

# new_list =[]
# for i in fruits_items:
#     if "a" in i:
#         new_list.append(i)
    
# print(new_list)


#in single line code 
'''structure 
[new_value   for   each_item   in   collection   if condition]
   '''

# '''list_3 = [x for x in fruits_items if "k" in x]
# print(list_3)'''

# The syntax 

'''newlist = [expression for item in iterable if condition == True]
The condition is like a filter that only accepts the items that evaluate to True.

'''

'''newlist = [x for x in fruits_items if x !="apple"]  
print(newlist)
 '''


# expression
'''The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:'''

list_1 =[i.upper() for i in fruits_items]
print(list_1)


# ''''The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:'''

# this is good for logic think very carefully

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_one = [x.upper() if x != "banana" else "orangle" for x in fruits]
print(new_one)










 


















    




        







        









































