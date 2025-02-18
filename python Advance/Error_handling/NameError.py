try:
    names=(input("enter your name "))
    if names.replace(" ","").isalpha():
        print(names)
    else:
        print("invalid input")
except Exception as e:
    print("An unexpected error occurred not related to the input:", e)