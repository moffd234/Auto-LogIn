from tkinter import messagebox

from ClockIn import ClockIn

if __name__ == '__main__':
    try:
        app = ClockIn()
    except Exception as e:
        messagebox.showerror("Error", str(e))
