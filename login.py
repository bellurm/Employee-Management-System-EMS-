from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry("400x450")
root.title("Cyber Worm")
root.iconbitmap("C:/Python/EMS/logo.ico")
root.configure(bg="#005b96")

connection = sqlite3.connect("admins.db")
myCursor = connection.cursor()

############################################## LOGIN ##############################################
def loginButton():
    myCursor.execute("SELECT username FROM administrators")
    results = myCursor.fetchall()
    for result in results:
        for selected in result:
            if usernameEntry.get() in selected:
                myCursor.execute(f"SELECT password FROM administrators WHERE username='{selected}'")
                passwd = myCursor.fetchall()
                if passwordEntry.get() == passwd[0][0]:
                    messagebox.showinfo("System Message", "Successfully logged in.")
                    exec(open("employee.py").read())
                else:
                    return messagebox.showinfo("System Message", "Username or password is wrong.")

welcomeLabel = Label(root, text="Welcome.", font=('Arial', 20, 'bold'), bg='#005b96', fg='red', pady=100).pack()

usernameLabel = Label(root, text="Username: ", font=('Arial', 14), bg='#005b96', fg='white')
usernameLabel.place(relx=0.1, rely=0.4)

passwordLabel = Label(root, text="Password: ", font=('Arial', 14), bg='#005b96', fg='white')
passwordLabel.place(relx=0.1, rely=0.5)

usernameEntry = Entry(root, width=30, border=5)
usernameEntry.place(relx=0.4, rely=0.4)

passwordEntry = Entry(root, width=30, border=5, show="*")
passwordEntry.place(relx=0.4, rely=0.5)

enterButton = Button(root, text="Log In", width=43, height=2, command=loginButton).place(relx=0.1, rely=0.6)

############################################## LOGIN ##############################################

if __name__ == "__main__":
    root.mainloop()
    connection.close()
