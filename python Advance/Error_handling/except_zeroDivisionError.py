# except ZeroDivisionError
try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("you can't divide by zero")

# simple except
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    c=a/b
    print("Result is:",c)

except ValueError:
    print("Error: Invalid input char is not allowed")

except:
    print("Error: Division by zero is not allowed")