# Python - Modify Strings
#Upper Case

x = "hello world"
print(x)
print(x.upper())


#Lower Case

y = "This IS STRING"
print(y.lower())

#This is very important 
'''Remove Whitespace  Whitespace is the space before and/or after the actual text, and very often you want to remove this space'''

new_str = " This is string and we learn about it "
print(len(new_str))
print(len(new_str.strip()))



# Replace String
#The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))


# Python String split() Method
'''Split a string into a list where each word is a list item:'''

txt = "welcome to the jungle"

x1 = txt.split()

print(len(x1))





'''
Parameter	Description
separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences" '''


txt_2= "hello, my name is Peter, I am 26 years old"

ab = txt_2.split(", ")

print(ab)