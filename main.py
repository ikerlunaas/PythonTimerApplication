import time
import tkinter as tk
from tkinter import messagebox
import sys

def show_alert():
    messagebox.showinfo("Timer Alert", "Time's up! Timer completed.")

def countdown_timer(seconds):
    def update_timer():
        nonlocal seconds
        if seconds > 0:
            minutes, secs = divmod(seconds, 60)
            time_format = f"{minutes:02d}:{secs:02d}"
            label.config(text=time_format)
            print(time_format, end='\r')  # Display in console
            seconds -= 1
            timer_window.after(1000, update_timer)
        else:
            show_alert()
            timer_window.destroy()
            sys.exit()  # Exit the script

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Create the timer window
    timer_window = tk.Toplevel(root)
    timer_window.title("Countdown Timer")

    label = tk.Label(timer_window, text="")
    label.pack(padx=20, pady=20)

    update_timer()
    timer_window.mainloop()

if __name__ == "__main__":
    try:
        seconds = int(input("Enter the timer duration in seconds: "))
        countdown_timer(seconds)
    except ValueError:
        print("Please enter a valid number of seconds.")

