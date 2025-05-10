from tkinter import *
from PIL import Image, ImageTk
import random

# Create a window with a title bar and set its geometry
root = Tk()
root.title('Image')
root.geometry('400x400')

# Load and display the image
upload = Image.open("password lock.jpg")
image = ImageTk.PhotoImage(upload)
image_label = Label(root, image=image)
image_label.pack()

# Label at the bottom
label = Label(root, text="RANDOM PASSWORD")
label.pack()

# Show/Hide password logic
def show_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

password_label = Label(root, text="Password:")
password_label.pack()

password_entry = Entry(root, show="*")
password_entry.pack()

show_password_var = BooleanVar()
show_password_checkbox = Checkbutton(root, text="Show Password", variable=show_password_var, command=show_password)
show_password_checkbox.pack()

# Generate a random password
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = "".join(random.choices(chars, k=12))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

random.seed(10)
generate_password()

# Run the application
root.mainloop()