# Python - Sort Lists

'''Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:'''

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print("Ascending order : ",thislist)

# thislist.sort(reverse=True)
# print("reverse the list :",thislist)



#CASE SENTIVE

# thislist_1 = ["banana", "Orange", "Kiwi", "cherry"]
# thislist_1.sort()
# print(thislist_1)


# print("Case Sentive : ")
# thislist_1.sort(key=str.lower)
# print(thislist_1)  


# Copy a List
'''You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
'''

'''thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

'''


# Make a copy of a list with the list() method:
'''
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
'''


# Use the slice Operator

'''thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)'''


# Python Join the list 
''' Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.
One of the easiest ways are by using the + operator. '''

new = [1,2,3,4,56,45,64]
list3 = thislist + new
print(list3)


new.extend(thislist)
print(new)

l1 = ['a','b','c','d','e']
l2 = [1,2,3,4,5]
l1.extend(l2)
print(l1)