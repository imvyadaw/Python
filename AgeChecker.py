try:
    age=int(input("Enter your age: "))
    if age>=18 and age<=100:
        print("You are an adult")
    elif age<18 and age>=0:
        print("You are a child")
    elif age>=101:
        print("Invalid are you a time traveler?")
        exit()
    else:
        print("Invalid age")
except ValueError:
    print("Invalid input. Please enter a valid age.")