from tkinter.ttk import *
from tkinter import *
import sqlite3

root = Tk()
root.title("Log-in Information")
root.geometry('600x300')
root.configure(bg='#CCCCCC')



# ====================================METHOD=S=======================#

def Database():
    global conn, cursor
    conn = sqlite3.connect("member.db")
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS IT(
                mem_id INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
                username TEXT NOT NULL, 
                password TEXT NOT NULL)
                """)
    cursor.execute("SELECT * FROM 'IT' WHERE username = 'admin' AND password = 'admin' ")

    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO IT (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please Complete the required filed!", fg="red")
        Back()

    else:
        cursor.execute("SELECT * FROM IT WHERE username = ? AND password = ? ", (USERNAME.get(), PASSWORD.get()))
    if cursor.fetchone() is not None:
        root.destroy()
        import gui
        USERNAME.get()
        PASSWORD.get()


    else:
        lbl_text.config(text="Invalid username or password", fg="red")
        cursor.close()
        conn.close()

def Back():
    Home.destroy()
    root.deiconify()


# =========VARIABLES
USERNAME = StringVar()
PASSWORD = StringVar()
#############Frames

Top = Frame(root, bd=2, relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack()

# ============text="Log-in for File Handling", bg = "cyan", font=("Arial", 20, "bold"), fg="black"
lbl_title = Label(Top, text="LOG-IN TO CONTINUE!", bg = "gray", font=("Gothic", 20, "bold"), fg="black")
lbl_title.pack(fill=X)
lbl_username = Label(Form, text="Username: ", font=("Arial", 20, "bold"), fg="black")
lbl_username.grid(row=0, sticky="e")

lbl_password = Label(Form, text="Password: ", font=("Arial", 20, "bold"), fg="black")
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

# ENTRY WIDGETS

username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

# BUTTON WIDGETS
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(padx=25, pady=3, columnspan=2)
btn_login.bind('<Return>', Login)


root.mainloop()