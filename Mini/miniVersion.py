'''
if you want to change the window border to appear (minimize button, maximize button, close button):

            - Change the overrideredirect(1) to overrideredirect(0).
            - Comment out: exit_button.place(x=955, y=16.47)
            - Change frame = Label(root, image=frame_image, bg="grey") to frame = Label(root, image=frame_image, bg="#F4F4F4")
'''

from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("1000x533")
root.overrideredirect(1)
root.wm_attributes('-transparentcolor', 'grey')
root.resizable(False, False)
root.iconbitmap("icon.ico")

def move(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')
def login(e):
    print("Login")
def exit(e):
    root.destroy()
def remember_onclick(e):
    check_button_image.configure(file="Mini/check_on.png")
    check_button.bind('<Button>', remember_onclick_1)
def remember_onclick_1(e):
    check_button_image.configure(file="Mini/check.png")
    check_button.bind('<Button>', remember_onclick)
def eye_onclick(e):
    password.config(show='')
    eye_image.configure(file="Mini/eye_fill.png")
    eye_button.bind('<Button>', eye_onclick_1)
def eye_onclick_1(e):
    password.config(show='*')
    eye_image.configure(file="Mini/eye_slash.png")
    eye_button.bind('<Button>', eye_onclick)
def signUp(e):
    print("direct to sign up page")
def forget(e):
    print("direct to forget password page")
def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg='#2F2F2F', font=("Poppins", 10, "bold"))

    def on_focus_in(event):
        if entry.get().strip() == placeholder_text.strip():
            entry.delete(0, tk.END)
            entry.config(fg='#2F2F2F', font=("Poppins", 10, "bold"))

    def on_focus_out(event):
        if entry.get().strip() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg='#2F2F2F', font=("Poppins", 10, "bold"))

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
def on_leave(e):
    login_button_image.configure(file="Mini/button.png")
def on_enter(e):
    login_button_image.configure(file="Mini/button_hover.png")

# Assets
frame_image = PhotoImage(file="Mini/FrameMini.png")
login_button_image = PhotoImage(file="Mini/button.png")
exit_button_image = PhotoImage(file="Mini/exit.png")
check_button_image = PhotoImage(file="Mini/check.png")
register_image = PhotoImage(file="Mini/register.png")
forget_password_image = PhotoImage(file="Mini/forget_password.png")
eye_image = PhotoImage(file="Mini/eye_slash.png")

#Main Frame
frame = Label(root, image=frame_image, bg="grey")
frame.pack(fill=BOTH, expand=True)
frame.bind('<B1-Motion>', move)

#Exit button
exit_button = Label(root, image=exit_button_image, bg="#F4F4F4", cursor="hand2")
exit_button.place(x=955, y=16.47)
exit_button.bind('<Button>', exit)

#Email Entry
email = Entry(root, bg="#ECECEC", fg="#2F2F2F", font="Poppins 10 bold", width=46, border=0)
email.place(x=535.15, y=220.78)
add_placeholder(email, "example@gmail.com")

#Password Entry
password = Entry(root, bg="#ECECEC", fg="#2F2F2F", font="Poppins 10", width=46, border=0, show="*")
password.place(x=535.15, y=287)
add_placeholder(password, "password")

#Eye button
eye_button = Label(root, image=eye_image, bg="#ECECEC", cursor="hand2")
eye_button.place(x=906.26, y=283.31)
eye_button.bind('<Button>', eye_onclick)

#Remember me button
check_button = Label(root, image=check_button_image, bg="white", cursor="hand2")
check_button.place(x=480.77, y=329)
check_button.bind('<Button>', remember_onclick)

#Login Button
login_button = Label(root, image=login_button_image, bg="white", cursor="hand2")
login_button.place(x=479.41, y=361.47)
login_button.bind('<Enter>', on_enter)
login_button.bind('<Leave>', on_leave)
login_button.bind('<Button>', login)

#register button
register = Label(root, image=register_image, bg="white", cursor="hand2")
register.place(x=740.41, y=445.32)
register.bind('<Button>', signUp)

#forget_password button
forget_password = Label(root, image=forget_password_image, bg="white", cursor="hand2")
forget_password.place(x=836.25, y=330.2)
forget_password.bind('<Button>', forget)

root.mainloop()