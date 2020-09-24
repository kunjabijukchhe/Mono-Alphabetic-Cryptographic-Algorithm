from tkinter import *
from tkinter import messagebox
import pymysql



# creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(width=False, height=False)
        self.geometry('350x170')

        self.configure(bg="#20c997")
        self.title("Remove User")

        a = StringVar()

        def ent():
            if len(a.get()) == 0:
                messagebox.showinfo("Error", "Please Enter A Valid Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
                if d:
                    try:
                        self.conn = pymysql.connect(host="localhost", user="root", password="root", database="nds")
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from admin where id = %s", [a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm", "User Removed Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error", "Something goes wrong")

        Label(self, text='Remove User', bg='#17a2b8', fg='white', font=("Helvetica", 20, 'bold')).place(x=90, y=25)
        Label(self, text="Enter User Id: ", bg='#20c997', fg='black', font=('Helvetica', 15, 'bold')).place(x=10, y=100)
        e = Entry(self, textvariable=a, width=37)
        e.place(x=160, y=100, height=30, width=40)
        Button(self, text='Remove',bg='#dc3545',fg='#f9f9f9', height=1, width=10,font=("Helvetica", 12, 'bold'), command=ent).place(
            x=220, y=100)


Rem().mainloop()