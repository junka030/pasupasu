import tkinter as tk
from tkinter import messagebox, ttk
import vault
import os
# global database connection and encryption key
db_conn = None
encryption_key = vault.load_key()


"""
Login Page
"""
def login():
    global db_conn
    password = entryPassword.get()
    db_conn = vault.get_db_connection(password)

    if db_conn:
        messagebox.showinfo("Success", "Login successful~ʚʕ•ﻌ•ʔɞ")
        populate_appnames()
        show_main_page()
    else:
        messagebox.showerror("Error", "Login failed!ฅ˙Ⱉ˙ฅʔ")


"""
Main page
"""
def show_main_page():
    login_frame.pack_forget()
    main_frame.pack()


def populate_appnames():
    appnames = vault.list_apps(db_conn)
    dropdown['values'] = appnames

"""
Operations
"""
# add password
def add():
    appname = entryName.get()
    loginid = entryLoginId.get()
    password = entryPasswordMain.get()
    vault.add_password(db_conn,encryption_key,appname,loginid,password)
    populate_appnames()
    clear_fields()

# get password
def get():
    appname = dropdown.get()
    loginid,password = vault.get_password(db_conn,encryption_key,appname)

    if loginid and password:
        messagebox.showinfo("Password info",f"Password for {appname}\nʕっ•ᴥ•ʔっ\n\n\nLogin id: {loginid}\n\nPassword: {password}")
    elif appname:
        messagebox.showinfo("Error", "App not found. ʕx﹏xʔ")

# get applications
def getlist():
    appnames = vault.list_apps(db_conn)
    if appnames:
        mess = "List of stored apps:\n\n"
        for name in appnames:
            mess += f"{name}\n"
        messagebox.showinfo("Applications", mess)
    else:
        messagebox.showinfo("Applications", "No application found!ʢ｡•ﻌ•｡ʡ")

# delete entry
def delete():
    appname = dropdown.get()
    vault.delete_password(db_conn, appname)
    dropdown.set("")
    populate_appnames()

def clear_fields():
    entryName.delete(0, tk.END)
    entryLoginId.delete(0, tk.END)
    entryPasswordMain.delete(0, tk.END)

"""
Main loop
"""

if __name__ == "__main__":

    app = tk.Tk()
    app.geometry("560x320")
    app.title("PasuPasu")

    # login page
    login_frame = tk.Frame(app)
    login_frame.pack()

    labelPassword = tk.Label(login_frame, text="Enter vault password: ")
    labelPassword.grid(row=0, column=0, padx=15, pady=15)
    entryPassword = tk.Entry(login_frame, show='*')
    entryPassword.grid(row=0, column=1, padx=15, pady=15)

    buttonLogin = tk.Button(login_frame, text="Login", command=login)
    buttonLogin.grid(row=1, column=0, columnspan=2, padx=15, pady=15)


    # main page
    main_frame = tk.Frame(app)

    # dropdown for appnames
    labelDropdown = tk.Label(main_frame, text="Select application: ")
    labelDropdown.grid(row=0, column=0, padx=15, pady=15)
    dropdown = ttk.Combobox(main_frame)
    dropdown.grid(row=0, column=1, padx=15, pady=15)

    # get button
    buttonGet = tk.Button(main_frame, text="Get", command=get, width=15)
    buttonGet.grid(row=1, column=0, padx=15, pady=5, sticky="we")

    # delete button
    buttonDelete = tk.Button(main_frame, text="Delete", command=delete, width=15)
    buttonDelete.grid(row=1, column=1, padx=15, pady=5, sticky="we")

    # list Button
    buttonList = tk.Button(main_frame, text="List", command=getlist, width=30)
    buttonList.grid(row=2, column=0, columnspan=2, padx=15, pady=5, sticky="we")

    # application name block
    labelName = tk.Label(main_frame, text="Application:")
    labelName.grid(row=3, column=0, padx=15, pady=15)
    entryName = tk.Entry(main_frame)
    entryName.grid(row=3, column=1, padx=15, pady=15)

    # login id name block
    labelLoginId = tk.Label(main_frame, text="Login id:")
    labelLoginId.grid(row=4, column=0, padx=15, pady=15)
    entryLoginId = tk.Entry(main_frame)
    entryLoginId.grid(row=4, column=1, padx=15, pady=15)

    # password block
    labelPasswordMain = tk.Label(main_frame, text="Password:")
    labelPasswordMain.grid(row=5, column=0, padx=10, pady=5)
    entryPasswordMain = tk.Entry(main_frame, show='*')
    entryPasswordMain.grid(row=5, column=1, padx=10, pady=5)

    # add button
    buttonAdd = tk.Button(main_frame, text="Add", command=add)
    buttonAdd.grid(row=6, column=0, columnspan=2, padx=15, pady=8, sticky="we")

    app.mainloop()