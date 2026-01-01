"""Instead of writing many if..else statements, you can use the match statement.
The match statement selects one of many code blocks to be executed."""

day = int(input("Enter the day"))

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")
    
    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")
    
    case 7:
        print("sunday")



# important
# switch compares only fixed values and needs break statements, whereas Python’s match supports powerful pattern matching without break and can work with complex data types like tuples and objects.



# Combine Values
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:

num = int(input("Enter value "))

match num:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
    
  case 6 | 7:
    print("I love weekends!")