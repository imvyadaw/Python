try:
    weight=float(input("Enter your weight in kg: "))
    Height=float(input("Enter your height in meters: "))

    if weight<=0 or Height<=0:
        print("Please enter a valid weight and height")
    else:
        BIM=weight/(Height**2)
        print(f"Your BMI is {BIM:.2f}")

        if BIM<18.5:
            print("You are underweight")
        elif 18.5<=BIM<29.9:
            print("You are normal weight")
        elif 25<=BIM<29.9:
            print("You are overweight")
        else:
            print("You are obese")
except ValueError:
    print("Invalid input. Please enter a valid number.")
