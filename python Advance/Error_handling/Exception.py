# Exception 
try:
    x=int(input("enter your first number:"))
    y=int(input("Enter your second number:"))
    p=x+y
    print("Result is:",p)
except Exception:
    print("Error: char is not allowed")
    print(Exception)
    # Exception using to print error  class 'exception ' is not defined
else:
    print("No error occurred")
