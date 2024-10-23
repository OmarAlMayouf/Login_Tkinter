'''
if you want to change the window border to appear (minimize button, maximize button, close button):

            - Change the overrideredirect(1) to overrideredirect(0).
            - Comment out: exit_button.place(x=1454, y=17)
            - Change frame = Label(root, image=frame_image, bg="grey") to frame = Label(root, image=frame_image, bg="#F4F4F4")
'''

import os
from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("1500x800")
root.overrideredirect(0)
root.wm_attributes('-transparentcolor', 'grey')
root.resizable(False, False)
root.iconbitmap("icon.ico")

def move(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')
def register(e):
    print("register")
def exit(e):
    root.destroy()
def eye_onclick(e):
    password.config(show='')
    eye_image.configure(file="eye_fill.png")
    eye_button.bind('<Button>', eye_onclick_1)
def eye_onclick_1(e):
    password.config(show='*')
    eye_image.configure(file="eye_slash.png")
    eye_button.bind('<Button>', eye_onclick)
def signIn(e):
    root.destroy()
    os.system("python main.py")
def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg='#676767', font=("Poppins", 12, "bold"))

    def on_focus_in(event):
        if entry.get().strip() == placeholder_text.strip():
            entry.delete(0, tk.END)
            entry.config(fg='#676767', font=("Poppins", 12, "bold"))

    def on_focus_out(event):
        if entry.get().strip() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg='#676767', font=("Poppins", 12, "bold"))

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
def on_leave(e):
    register_button_image.configure(file="register_button.png")
def on_enter(e):
    register_button_image.configure(file="register_button_hover.png")

# Assets
frame_image = PhotoImage(file="Create Account Frame.png")
register_button_image = PhotoImage(file="register_button.png")
exit_button_image = PhotoImage(file="exit.png")
register_image = PhotoImage(file="register.png")
eye_image = PhotoImage(file="eye_slash.png")

#Main Frame
frame = Label(root, image=frame_image, bg="#F4F4F4")
frame.pack(fill=BOTH, expand=True)
frame.bind('<B1-Motion>', move)

#Exit button
exit_button = Label(root, image=exit_button_image, bg="#F4F4F4", cursor="hand2")
#exit_button.place(x=1454, y=17)
exit_button.bind('<Button>', exit)

#Username Entry
username = Entry(root, bg="#ECECEC", fg="#676767", font="Poppins 12 bold", width=46, border=0)
username.place(x=944.06, y=399)
add_placeholder(username, "Enter your username")

#Email Entry
email = Entry(root, bg="#ECECEC", fg="#676767", font="Poppins 12 bold", width=46, border=0)
email.place(x=944.06, y=475.91)
add_placeholder(email, "Enter your email")

#Password Entry
password = Entry(root, bg="#ECECEC", fg="#676767", font="Poppins 12", width=46, border=0, show="*")
password.place(x=944, y=553)
add_placeholder(password, "Create your password")

#Eye button
eye_button = Label(root, image=eye_image, bg="#ECECEC", cursor="hand2")
eye_button.place(x=1370.63, y=549)
eye_button.bind('<Button>', eye_onclick)

#register Button
register_button = Label(root, image=register_button_image, bg="white", cursor="hand2")
register_button.place(x=880, y=606)
register_button.bind('<Enter>', on_enter)
register_button.bind('<Leave>', on_leave)
register_button.bind('<Button>', register)

#register button
login_text = Label(root, image=register_image, bg="white", cursor="hand2")
login_text.place(x=1210, y=694)
login_text.bind('<Button>', signIn)

root.mainloop()