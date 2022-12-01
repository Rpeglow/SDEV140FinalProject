import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("650x650")
root.title("Welcome to the Toggery.")


def gather_info():
    firstname = e_first_name.get().title()
    lastname = e_last_name.get().title()
    phone = e_phone.get()
    address = txt_address.get('1.0', tk.END)
    print(firstname, lastname, address, phone)


my_img = ImageTk.PhotoImage(Image.open("toggery.jpg"))
my_label = Label(image=my_img, )
my_label.pack()


label_f_name = tk.Label(root, text="Enter your First Name:", font=('Arial', 18))
label_f_name.pack()
e_first_name = Entry(root, width=50, borderwidth=3)
e_first_name.pack()


label_l_name = tk.Label(root, text="Enter your Last Name:", font=('Arial', 18))
label_l_name.pack()
e_last_name = Entry(root, width=50, borderwidth=3)
e_last_name.pack()


label_phone = tk.Label(root, text="Enter your Phone Number:", font=('Arial', 18))
label_phone.pack()
e_phone = Entry(root, width=50, borderwidth=3)
e_phone.pack()


label_address = tk.Label(root, text="Enter your Address:", font=('Arial', 18))
label_address.pack()
txt_address = Text(root, height=2, font=('Arial', 16))
txt_address.pack(padx=50)


btn_continue = tk.Button(root, text='Continue', command=gather_info, font='Arial, 18')
btn_continue.place(x=500, y=570, height=60, width=120)


mainloop()

