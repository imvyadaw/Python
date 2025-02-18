try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    c=a/b
    print("Result is:",c)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Error: char is not allowed")


# variable not defined
# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a number: "))
#     c=a/z
#     print("Result is:",c)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except NameError as b:
#     print("Error: variable",b)