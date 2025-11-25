# import tkinter module
import tkinter as tk

# function to get text from entry widget
def print_entry_text(event):
    entry_text = entry.get()
    print(entry_text)

# main application window
root = tk.Tk()
root.title("Tkinter Entry Example")

# create entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=20)

# key bindinf event
entry.bind("<Return>", print_entry_text)

# run the application
root.mainloop()