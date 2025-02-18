import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())  # Get weight in kg
        feet = float(feet_entry.get())  # Get height in feet

        if weight <= 0 or feet <= 0:
            messagebox.showerror("Error", "Please enter valid positive values!")
            return

        # Convert height from feet to meters
        height_m = feet * 0.3048

        # Calculate BMI
        bmi = weight / (height_m ** 2)
        result_label.config(text=f"Your BMI: {bmi:.2f}")

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        category_label.config(text=f"Category: {category}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values!")

# Create main application window
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("300x300")
app.resizable(False, False)

# Weight input
tk.Label(app, text="Enter Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(app)
weight_entry.pack(pady=5)

# Height input (Feet)
tk.Label(app, text="Enter Height (Feet):").pack(pady=5)
feet_entry = tk.Entry(app)
feet_entry.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

# Result Labels
result_label = tk.Label(app, text="Your BMI: ", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

category_label = tk.Label(app, text="Category: ", font=("Arial", 12, "bold"))
category_label.pack(pady=5)

# Run the application
app.mainloop()
