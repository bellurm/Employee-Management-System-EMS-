from tkinter import *
from tkinter import messagebox
import sqlite3
import webbrowser as web

system = Tk()
system.geometry("1920x1080")
system.title("Cyber Worm")
system.iconbitmap("C:/Python/EMS/logo.ico")
system.configure(bg="#005b96")
#system.attributes('-fullscreen', True)

defaultDatabase = StringVar()
defaultDatabase.set("employee.db")

titleLabel = Label(system, text="EMPLOYEE MANAGEMENT SYSTEM (EMS)", bg='#005b96', fg='red', font=('Arial', 35, 'bold'))
titleLabel.place(relx=0.15, rely=0.03)

########################################### CREATE TABLE AND ADD VARIABLE ###########################################
def createTableMethod():
    try:
        databaseName = getDbNameEntryCREATE.get()
        tableName = getTableNameEntryCREATE.get()
        variables = getVariablesEntryCREATE.get()
        connection = sqlite3.connect(f'{databaseName}')
        cursor = connection.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {tableName} {variables}")
        connection.commit()
        connection.close()
        return messagebox.showinfo("System Message", "Table is created successfully.")
    except:
        return messagebox.showerror("System Message", "Something went wrong.")


createTableFrame = LabelFrame(system, text="Create Table", fg='white', bg='#005b96', font=('Arial', 12), height=220, width=320)
createTableFrame.place(relx=0.05, rely=0.14)

getDbNameEntryCREATE = Entry(createTableFrame, textvariable=defaultDatabase, border=5)
getDbNameEntryCREATE.place(relx=0.5, rely= 0.1)

getDbNameLabelCREATE = Label(createTableFrame, text="DB Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getDbNameLabelCREATE.place(relx=0.05, rely=0.1)

getTableNameEntryCREATE = Entry(createTableFrame, border=5)
getTableNameEntryCREATE.place(relx=0.5, rely= 0.3)

getTableNameLabelCREATE = Label(createTableFrame, text="Table Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getTableNameLabelCREATE.place(relx=0.05, rely=0.3)

getVariablesLabelCREATE = Label(createTableFrame, text="Variables:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getVariablesLabelCREATE.place(relx=0.05, rely=0.5)

getVariablesEntryCREATE = Entry(createTableFrame, border=5)
getVariablesEntryCREATE.place(relx=0.5, rely= 0.5)

helpButtonCREATE = Button(createTableFrame, text="? ", font=('Arial', 10, 'bold'), bg='red', fg='white', \
    command=lambda : messagebox.showinfo("Usage", "USAGE: (<variable name> <data type>,...)\
        \nYou can take support from your manager."))
helpButtonCREATE.place(relx=0.4, rely=0.5)

createTableButton = Button(createTableFrame, text="Create Table", fg='#005b96', width=40, height=2, command=createTableMethod)
createTableButton.place(relx=0.05, rely=0.75)
########################################### CREATE TABLE AND ADD VARIABLE ###########################################

########################################### DELETE TABLE ###########################################
def dropTable():
    try:
        databaseName = getDbNameEntry_DropTable.get()
        tableName = getTableNameEntry_DropTable.get()
        connection = sqlite3.connect(f'{databaseName}')
        cursor = connection.cursor()
        cursor.execute(f"DROP TABLE {tableName}")
        connection.commit()
        connection.close()
        return messagebox.showinfo("System Message", "Table is deleted successfully.")
    except:
        return messagebox.showerror("System Message", "Something went wrong.")

dropTableFrame = LabelFrame(system, text="Delete Table", fg='white', bg='#005b96', font=('Arial', 12), height=170, width=320)    
dropTableFrame.place(relx=0.7, rely=0.2)

getDbNameEntry_DropTable = Entry(dropTableFrame, textvariable=defaultDatabase, border=5)
getDbNameEntry_DropTable.place(relx=0.5, rely= 0.1)

getDbNameLabel_DropTable = Label(dropTableFrame, text="DB Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getDbNameLabel_DropTable.place(relx=0.05, rely=0.1)

getTableNameEntry_DropTable = Entry(dropTableFrame, border=5)
getTableNameEntry_DropTable.place(relx=0.5, rely= 0.4)

getTableNameLabel_DropTable = Label(dropTableFrame, text="Table Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getTableNameLabel_DropTable.place(relx=0.05, rely=0.4)

dropTableButton = Button(dropTableFrame, text="Delete Table", fg='#005b96', width=40, height=2, command=dropTable)
dropTableButton.place(relx=0.05, rely=0.69)
########################################### DELETE TABLE ###########################################

########################################### DELETE ROW ###########################################
def deleteRow():
    try:
        databaseName = getDbNameEntry_DeleteRow.get()
        tableName = getTableNameEntry_DeleteRow.get()
        rowIdentifier = getRowEntry_DeleteRow.get()
        connection = sqlite3.connect(f'{databaseName}')
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {tableName} WHERE ROWID={int(rowIdentifier)}")
        connection.commit()
        connection.close()
        return messagebox.showinfo("System Message", f"Employee is removed from {tableName} successfully.")
    except:
        return messagebox.showerror("System Message", "Something went wrong.")

deleteRowFrame = LabelFrame(system, text="Delete Row", fg='white', bg='#005b96', font=('Arial', 12), height=220, width=320)    
deleteRowFrame.place(relx=0.05, rely=0.5)

getDbNameEntry_DeleteRow = Entry(deleteRowFrame, textvariable=defaultDatabase, border=5)
getDbNameEntry_DeleteRow.place(relx=0.5, rely= 0.1)

getDbNameLabel_DeleteRow = Label(deleteRowFrame, text="DB Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getDbNameLabel_DeleteRow.place(relx=0.05, rely=0.1)

getTableNameEntry_DeleteRow = Entry(deleteRowFrame, border=5)
getTableNameEntry_DeleteRow.place(relx=0.5, rely= 0.3)

getTableNameLabel_DeleteRow = Label(deleteRowFrame, text="Table Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getTableNameLabel_DeleteRow.place(relx=0.05, rely=0.3)

getRowEntry_DeleteRow = Entry(deleteRowFrame, border=5)
getRowEntry_DeleteRow.place(relx=0.5, rely=0.5)

getRowLabel_DeleteRow = Label(deleteRowFrame, text="Row Identifier:", bg='#005b96', fg='white', font=('Arial', 11, 'bold'))
getRowLabel_DeleteRow.place(relx=0.05, rely=0.5)

helpButton_DeleteRow = Button(deleteRowFrame, text="? ", font=('Arial', 10, 'bold'), bg='red', fg='white', \
    command=lambda : messagebox.showinfo("Usage", "USAGE: The number of the record to be deleted.\
        \nYou can take support from your manager."))
helpButton_DeleteRow.place(relx=0.4, rely=0.5)

deleteRowButton = Button(deleteRowFrame, text="Delete Row", fg='#005b96', width=40, height=2, command=deleteRow)
deleteRowButton.place(relx=0.05, rely=0.74)
########################################### DELETE ROW ###########################################

########################################### SHOW TABLES OR ROWS ###########################################
def showTables():
    # Geçersiz tablo ismi girilmesi durumunda hata mesajı verilebilir.
    windowInfo = Toplevel()
    windowInfo.geometry("1920x1080")
    windowInfo.title(f"Table's ({getDbNameEntry_Table.get()}) rows.")
    windowInfo.iconbitmap("C:/Python/EMS/logo.ico")
    windowInfo.configure(bg="#005b96")

    databaseName = getDbNameEntry_Table.get()
    connection = sqlite3.connect(f'{databaseName}')
    cursor = connection.cursor()
    # show tables
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    tablesInfoText = Text(windowInfo, bg='#005b96', fg='white' ,font=('Arial', 12, 'bold'), width=80, height=15)
    tablesInfoText.pack()

    for i in enumerate(tables, 1):
        print(i)
        tablesInfoText.insert(END, f"{i}\n")
    # connection.commit()
    connection.close()

def showRows():
    # Geçersiz tablo ismi girilmesi durumunda hata mesajı verilebilir.
    windowInfo = Toplevel()
    windowInfo.geometry("1920x1080")
    windowInfo.title(f"Table's ({getTableNameEntry_Row.get()}) rows.")
    windowInfo.iconbitmap("C:/Python/EMS/logo.ico")
    windowInfo.configure(bg="#005b96")

    databaseName = getDbNameEntry_Table.get()
    tableName = getTableNameEntry_Row.get()
    connection = sqlite3.connect(f'{databaseName}')
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {tableName}")
    rows = cursor.fetchall()
    
    rowInfoText = Text(windowInfo, bg='#005b96', fg='white' ,font=('Arial', 12, 'bold'), width=80, height=15)
    rowInfoText.pack()
    
    for i in enumerate(rows, 1):
        rowInfoText.insert(END, f"{i}\n")

    connection.close()

showTablesOrRowsFrame = LabelFrame(system, text="Show Tables or Rows", fg='white', bg='#005b96', font=('Arial', 12), height=220, width=320)    
showTablesOrRowsFrame.place(relx=0.4, rely=0.14)

getDbNameEntry_Table = Entry(showTablesOrRowsFrame, textvariable=defaultDatabase, border=5)
getDbNameEntry_Table.place(relx=0.5, rely= 0.1)

getDbNameLabel_Table = Label(showTablesOrRowsFrame, text="DB Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getDbNameLabel_Table.place(relx=0.05, rely=0.1)

getTableNameEntry_Row = Entry(showTablesOrRowsFrame, border=5)
getTableNameEntry_Row.place(relx=0.5, rely= 0.38)

getTableNameLabel_TableOrRow2 = Label(showTablesOrRowsFrame, text="Table Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getTableNameLabel_TableOrRow2.place(relx=0.05, rely=0.38)

showTablesButton = Button(showTablesOrRowsFrame, text="Show Tables", fg='#005b96', width=20, height=4, command=showTables)
showTablesButton.place(relx=0.02, rely=0.62)

showRowsButton = Button(showTablesOrRowsFrame, text="Show Table's Rows", fg='#005b96', width=20, height=4, command=showRows)
showRowsButton.place(relx=0.51, rely=0.62)
########################################### SHOW TABLES OR ROWS ###########################################

########################################### ADD EMPLOYEE ###########################################

def addEmployee():
    try:
        databaseName = getDbNameEntry_addEmployee.get()
        tableName = getTableNameEntry_addEmployee.get()
        variables = getVarsEntry_addEmployee.get()
        connection = sqlite3.connect(f'{databaseName}')
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {tableName} VALUES({variables})")
        connection.commit()
        connection.close()
        return messagebox.showinfo("System Message", f"Employee is added to {tableName} successfully.")
    except:
        return messagebox.showerror("System Message", "Something went wrong.")

addEmployeeFrame = LabelFrame(system, text="Add Employee", fg='white', bg='#005b96', font=('Arial', 12), height=220, width=320)    
addEmployeeFrame.place(relx=0.4, rely=0.5)

getDbNameEntry_addEmployee = Entry(addEmployeeFrame, textvariable=defaultDatabase, border=5)
getDbNameEntry_addEmployee.place(relx=0.5, rely= 0.1)

getDbNameLabel_addEmployee = Label(addEmployeeFrame, text="DB Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getDbNameLabel_addEmployee.place(relx=0.05, rely=0.1)

getTableNameEntry_addEmployee = Entry(addEmployeeFrame, border=5)
getTableNameEntry_addEmployee.place(relx=0.5, rely= 0.3)

getTableNameLabel_addEmployee = Label(addEmployeeFrame, text="Table Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getTableNameLabel_addEmployee.place(relx=0.05, rely=0.3)

getVarsEntry_addEmployee = Entry(addEmployeeFrame, border=5)
getVarsEntry_addEmployee.place(relx=0.5, rely=0.5)

getVarsLabel_addEmployee = Label(addEmployeeFrame, text="Employee Vars:", bg='#005b96', fg='white', font=('Arial', 11, 'bold'))
getVarsLabel_addEmployee.place(relx=0.05, rely=0.5)

addEmployeeButton = Button(addEmployeeFrame, text="Add Employee", fg='#005b96', width=40, height=2, command=addEmployee)
addEmployeeButton.place(relx=0.05, rely=0.74)

helpButton_addEmployee = Button(addEmployeeFrame, text="? ", font=('Arial', 10, 'bold'), bg='red', fg='white', \
    command=lambda : messagebox.showinfo("Usage", "USAGE: <variable's value>, ...\
        \nYou can take support from your manager."))
helpButton_addEmployee.place(relx=0.42, rely=0.5)
########################################### ADD EMPLOYEE ###########################################

########################################### UPDATE DATA ###########################################
def updateData():
    try:
        databaseName = getDbNameEntry_update.get()
        tableName = getTableNameEntry_update.get()
        variables = getVarsEntry_update.get()
        rowIdentifier = getRowEntry_update.get()
        connection = sqlite3.connect(f'{databaseName}')
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {tableName} SET {variables} WHERE ROWID={rowIdentifier}")
        connection.commit()
        connection.close()
        return messagebox.showinfo("System Message", f"Employee is updated successfully.")
    except:
        return messagebox.showerror("System Message", "Something went wrong.")

updateFrame = LabelFrame(system, text="Update Employee", fg='white', bg='#005b96', font=('Arial', 12), height=260, width=320)    
updateFrame.place(relx=0.7, rely=0.5)

getDbNameEntry_update = Entry(updateFrame, textvariable=defaultDatabase, border=5)
getDbNameEntry_update.place(relx=0.5, rely= 0.05)

getDbNameLabel_update = Label(updateFrame, text="DB Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getDbNameLabel_update.place(relx=0.05, rely=0.05)

getTableNameEntry_update = Entry(updateFrame, border=5)
getTableNameEntry_update.place(relx=0.5, rely= 0.22)

getTableNameLabel_update = Label(updateFrame, text="Table Name:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getTableNameLabel_update.place(relx=0.05, rely=0.22)

getVarsEntry_update = Entry(updateFrame, border=5)
getVarsEntry_update.place(relx=0.5, rely=0.4)

getVarsLabel_update = Label(updateFrame, text="To Be Updated:", bg='#005b96', fg='white', font=('Arial', 11, 'bold'))
getVarsLabel_update.place(relx=0.05, rely=0.4)

getRowEntry_update = Entry(updateFrame, border=5)
getRowEntry_update.place(relx=0.5, rely=0.6)

getRowLabel_update = Label(updateFrame, text="Row Identifier:", bg='#005b96', fg='white', font=('Arial', 12, 'bold'))
getRowLabel_update.place(relx=0.05, rely=0.6)

helpButton_update = Button(updateFrame, text="? ", font=('Arial', 10, 'bold'), bg='red', fg='white', \
    command=lambda : messagebox.showinfo("Usage", "USAGE: <variable>='<value>'\
        \nYou can take support from your manager."))
helpButton_update.place(relx=0.42, rely=0.4)

UpdateButton = Button(updateFrame, text="Update Employee", fg='#005b96', width=40, height=2, command=updateData)
UpdateButton.place(relx=0.05, rely=0.78)
########################################### UPDATE DATA ###########################################

########################################### CONTACT ###########################################
def contact():
    web.open("https://blog-cyberworm.com/blog/telegram-instagram")

contactFrame = LabelFrame(system, text="Contact", fg='white', bg='#005b96', font=('Arial', 12), height=100, width=900)
contactFrame.place(relx=0.05, rely=0.8)

contactLabel = Label(contactFrame, text="I can edit this code in a more efficient, effective and advanced way.\nThis code just for the practice and education. Contact me if you want:", \
    font=('Arial', 14, 'bold'), bg='#005b96', fg='red')
contactLabel.place(relx=0.01, rely=0.1)

contactButton = Button(contactFrame, text="Contact", fg='#005b96', width=30, height=2, command=contact)
contactButton.place(relx=0.75, rely=0.2)
########################################### CONTACT ###########################################

if __name__ == "__main__":
    system.mainloop()
