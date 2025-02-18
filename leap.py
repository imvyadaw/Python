import tkinter as tk
from tkinter import messagebox

class LeapYearChecker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Leap Year Checker")

        # Create input field
        self.year_label = tk.Label(self.window, text="Enter a year:")
        self.year_label.pack()
        self.year_entry = tk.Entry(self.window)
        self.year_entry.pack()

        # Create button to check if year is a leap year
        self.check_button = tk.Button(self.window, text="Check", command=self.check_leap_year)
        self.check_button.pack()

        # Create label to display result
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

    def is_leap_year(self, year: int) -> bool:
        """
        Checks if a given year is a leap year.

        Args:
        year (int): The year to check.

        Returns:
        bool: True if the year is a leap year, False otherwise.
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def check_leap_year(self):
        try:
            year = int(self.year_entry.get())
            if self.is_leap_year(year):
                self.result_label.config(text=f"{year} is a leap year")
            else:
                self.result_label.config(text=f"{year} is not a leap year")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid year")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = LeapYearChecker()
    app.run()