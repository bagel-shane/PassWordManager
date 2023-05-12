import tkinter as tk
from Manger import PasswordManagerGUI

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("600x400")
    app = PasswordManagerGUI(window)
    window.mainloop()