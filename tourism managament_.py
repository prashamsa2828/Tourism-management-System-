import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showerror, showinfo
import random
from PIL import Image, ImageTk
import pymysql
window, Button1, Button2, otp, p, b = '', '', '', '', '', ''
def book():
    global window
    window = tk.Tk()
    window.title("Booking")
    window.resizable(0, 0)
    l1 = tk.Label(window, text="Full Name", font=("Arial bold", 12))
    l1.place(x=10, y=10)
    t1 = tk.Entry(window, width=25, bd=5, font=(12))
    t1.place(x=200, y=10)

    l2 = tk.Label(window, text="Mail ID", font=("Arial bold", 12))
    l2.place(x=10, y=60)
    t2 = tk.Entry(window, width=25, bd=5, font=(12))
    t2.place(x=200, y=60)

    l3 = tk.Label(window, text="Mobile Number", font=("Arial bold", 12))
    l3.place(x=10, y=110)
    t3 = tk.Entry(window, width=25, bd=5, font=(12))
    t3.place(x=200, y=110)

    l4 = tk.Label(window, text="Package/ Hotel Name", font=("Arial bold", 12))
    l4.place(x=10, y=160)
    t4 = tk.Entry(window, width=25, bd=5, font=(12))
    t4.place(x=200, y=160)

    l5 = tk.Label(window, text="State", font=("Arial bold", 12))
    l5.place(x=10, y=210)
    t5 = tk.Entry(window, width=25, bd=5, font=(12))
    t5.place(x=200, y=210)

    def check():
        if t1.get() == '' or t2.get() == '' or t3.get() == '' or t4.get() == '' or t5.get() == '' :
            showerror('Error', "All Fields Are Required", parent=window)
        else:
            window.destroy()
            messagebox.showinfo('Success', "Booking confirmed")

    Button = tk.Button(window, text="Confirm Booking", font=("Arial", 20, "bold"), command=check)
    Button.place(x=300, y=260)
    window.geometry("700x350")
    window.mainloop()

class Firstpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("beach.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Frame = tk.Frame(self, bg="white")
        Frame.place(x=450, y=200, height=450, width=600)

        Label = tk.Label(self, text="Tourism Management", font=("Arial", 35, "bold"),
                         fg="pink", bg="white",
                         relief=RAISED,
                         bd=10,
                         padx=50, pady=10)
        Label.place(x=100, y=25)

        Label = tk.Label(Frame, text="LOGIN AS", font=("Arial", 40, "bold"), fg="pink", bg = "white")
        Label.place(x=45, y=30)

        Button = tk.Button(Frame, text="USER", font=("Arial", 25), height=1, width=12, command=lambda: controller.show_frame(Secondpage))
        Button.place(x=190, y=150)

        Button = tk.Button(Frame, text="ADMIN", font=("Arial", 25), height=1, width=12, command = lambda: controller.show_frame(Thirdpage))
        Button.place(x=190, y=280)

class Secondpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("beach.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Label = tk.Label(self, text="Looking for...", font=("Arial bold", 20, "bold"), fg='black', bg="white", bd=10)
        Label.place(x=300, y=25)

        def package():
            j, c, s = 100, 0, 0
            con = pymysql.connect(host='localhost', user='root', password='Vmr123@*', database='package')
            cur = con.cursor()
            cur.execute("select * from info")
            r = list(cur.fetchall())

            for i in range(0, len(r), 2):
                border = tk.LabelFrame(self, text=r[i][1], bg='white', bd=10, font=("Arial ", 20))
                border.place(x=50, y=s * 370 + j, height=250, width=500)

                label3 = tk.Label(border, text="Number of days:\n\nPlaces:\n\nActivities:\n\nPrice:\n\n",
                                  font=('Arial bold', 13), bg="white")
                label3.place(x=18, y=15)
                label4 = tk.Label(border, text=r[i][2] + "\n\n" + r[i][3] + "\n\n" + r[i][4] + "\n\n" + r[i][5],
                                  font=('Arial', 13), bg="white")
                label4.place(x=250, y=15)
                Button1 = tk.Button(border, text="Book", font=("Arial", 15), height=1, width=5 ,command= book)
                Button1.place(x=400, y=150)

                c = i + 1
                if c < len(r):
                    border = tk.LabelFrame(self, text=r[i + 1][1], bg='white', bd=10, font=("Arial ", 20))
                    border.place(x=650, y=s * 370 + j, height=250, width=500)
                    label3 = tk.Label(border, text="Number of days:\n\nPlaces:\n\nActivities:\n\nPrice:\n\n",
                                      font=('Arial bold', 13), bg="white")
                    label3.place(x=18, y=15)

                    label4 = tk.Label(border,
                                      text=r[i + 1][2] + "\n\n" + r[i + 1][3] + "\n\n" + r[i + 1][4] + "\n\n" + r[i + 1][5],
                                      font=('Arial', 13), bg="white")
                    label4.place(x=250, y=15)

                    Button1 = tk.Button(border, text="Book", font=("Arial", 15), height=1, width=5 ,command= book)
                    Button1.place(x=400, y=150)
                j = 0
                s += 1

            Button = tk.Button(self, text="back", font=("Arial bold", 17), height=1, width=5, command=lambda: controller.show_frame(Firstpage))
            Button.place(x=25, y=630)
            if s==3:
                Button = tk.Button(self, text="Next", font=("Arial bold", 17), height=1, width=5, command=lambda: controller.show_frame(Login2))
                Button.place(x=1090, y=630)

        def hotel():
            j, c, s = 100, 0, 0
            con = pymysql.connect(host='localhost', user='root', password='Vmr123@*', database='hotel')
            cur = con.cursor()
            cur.execute("select * from data")
            r = list(cur.fetchall())

            for i in range(0, len(r), 2):
                border = tk.LabelFrame(self,bg='white', bd=10, font=("Arial ", 20))
                border.place(x=50, y=s * 370 + j, height=250, width=500)

                label3 = tk.Label(border, text="Hotel Name:\n\nState:\n\nCity:\n\nPrice:\n\n",
                               font=('Arial bold', 14), bg="white")
                label3.place(x=18, y=15)
                label4 = tk.Label(border, text = r[i][1] + "\n\n" + r[i][2] + "\n\n" + r[i][3] + "\n\n" + r[i][4],
                               font=('Arial', 14), bg="white")
                label4.place(x=250, y=15)
                Button1 = tk.Button(border, text="Book", font=("Arial", 15), height=1, width=5 ,command= book)
                Button1.place(x=400, y=150)

                c = i + 1
                if c < len(r):
                    border = tk.LabelFrame(self, bg='white', bd=10, font=("Arial ", 20))
                    border.place(x=650, y=s * 370 + j, height=250, width=500)
                    label3 = tk.Label(border, text="Hotel Name:\n\nState:\n\nCity:\n\nPrice:\n\n",
                                   font=('Arial bold', 14), bg="white")
                    label3.place(x=18, y=15)

                    label4 = tk.Label(border, text=r[i + 1][1] + "\n\n" + r[i + 1][2] + "\n\n" + r[i + 1][3] + "\n\n" + r[i + 1][4],
                                   font=('Arial', 14), bg="white")
                    label4.place(x=250, y=15)

                    Button1 = tk.Button(border, text="Book", font=("Arial", 15), height=1, width=5,command= book)
                    Button1.place(x=400, y=150)
                    j = 0
                    s += 1

            Button = tk.Button(self, text="back", font=("Arial bold", 17), height=1, width=5, command = lambda: controller.show_frame(Firstpage))
            Button.place(x=25, y=630)

            if s==3:
                print(s)
                Button = tk.Button(self, text="Next", font=("Arial bold", 17), height=1, width=5, command=lambda: controller.show_frame(Login1))
                Button.place(x=1090, y=630)

        selected = tk.StringVar()
        def selection(event):
            if selected.get()=='Hotel':
                hotel()
            if selected.get()== 'Holiday package':
                package()

        comboquestion = ttk.Combobox(self, font=('Arial', 20), state='readonly', justify=CENTER, textvariable=selected)
        comboquestion['values'] = (
            'Select', 'Hotel', 'Holiday package')
        comboquestion.current(0)
        comboquestion.place(x=550, y=30, width=350)
        comboquestion.bind('<<ComboboxSelected>>', selection)

class Login1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("beach.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        j, c, s = 90, 0, 0
        con = pymysql.connect(host='localhost', user='root', password='Vmr123@*', database='hotel')
        cur = con.cursor()
        cur.execute("select * from data")
        r = list(cur.fetchall())

        for i in range(4, len(r), 2):
            border = tk.LabelFrame(self,bg='white', bd=10, font=("Arial ", 20))
            border.place(x=50, y=s * 370 + j, height=250, width=500)

            label3 = tk.Label(border, text="Hotel Name:\n\nState:\n\nCity:\n\nPrice:\n\n",
                              font=('Arial bold', 14), bg="white")
            label3.place(x=18, y=15)
            label4 = tk.Label(border, text=r[i][1] + "\n\n" +r [i][3] + "\n\n" + r[i][4] + "\n\n" + r[i][5],
                              font=('Arial', 14), bg="white")
            label4.place(x=250, y=15)
            Button1 = tk.Button(border, text="Book", font=("Arial", 15), height=1, width=5, command=book)
            Button1.place(x=400, y=150)

            c = i + 1
            if c < len(r):
                border = tk.LabelFrame(self, bg='white', bd=10, font=("Arial ", 20))
                border.place(x=650, y=s * 370 + j, height=250, width=500)
                label3 = tk.Label(border, text="Hotel Name:\n\nState:\n\nCity:\n\nPrice:\n\n",
                                  font=('Arial bold', 14), bg="white")
                label3.place(x=18, y=15)

                label4 = tk.Label(border, text=r[i + 1][1] + "\n\n" + r[i + 1][3] + "\n\n" + r[i + 1][4] + "\n\n" + r[i + 1][5],
                                  font=('Arial', 13), bg="white")
                label4.place(x=250, y=15)

                Button1 = tk.Button(border, text="Book", font=("Arial", 14), height=1, width=5, command=book)
                Button1.place(x=400, y=150)
                j = 0
                s += 1

        Button = tk.Button(self, text="back", font=("Arial bold", 17), height=1, width=5,
                           command=lambda: controller.show_frame(Secondpage))
        Button.place(x=25, y=630)

        if s == 7:
            print(s)
            Button = tk.Button(self, text="Next", font=("Arial bold", 17), height=1, width=5,
                               command=lambda: controller.show_frame(Login1))
            Button.place(x=1090, y=630)

class Login2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("beach.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        def package():
            j, c, s = 90, 0, 0
            con = pymysql.connect(host='localhost', user='root', password='Vmr123@*', database='package')
            cur = con.cursor()
            cur.execute("select * from info")
            r = list(cur.fetchall())

            for i in range(4, len(r), 2):
                border = tk.LabelFrame(self, text=r[i][1], bg='white', bd=10, font=("Arial ", 20))
                border.place(x=50, y=s * 370 + j, height=250, width=500)

                label3 = tk.Label(border, text="Number of days:\n\nPlaces:\n\nActivities:\n\nPrice:\n\n",
                                  font=('Arial bold', 13), bg="white")
                label3.place(x=18, y=15)
                label4 = tk.Label(border, text=r[i][3] + "\n\n" + r[i][4] + "\n\n" + r[i][5] + "\n\n" + r[i][6],
                                  font=('Arial', 13), bg="white")
                label4.place(x=250, y=15)
                Button1 = tk.Button(border, text="Book", font=("Arial", 15), height=1, width=5 ,command= book)
                Button1.place(x=400, y=150)

                c = i + 1
                if c < len(r):
                    border = tk.LabelFrame(self, text=r[i + 1][1], bg='white', bd=10, font=("Arial ", 20))
                    border.place(x=650, y=s * 370 + j, height=250, width=500)
                    label3 = tk.Label(border, text="Number of days:\n\nPlaces:\n\nActivities:\n\nPrice:\n\n",
                                      font=('Arial bold', 13), bg="white")
                    label3.place(x=18, y=15)

                    label4 = tk.Label(border,
                                      text=r[i + 1][3] + "\n\n" + r[i + 1][4] + "\n\n" + r[i + 1][5] + "\n\n" + r[i + 1][6],
                                      font=('Arial', 13), bg="white")
                    label4.place(x=250, y=15)

                    Button1 = tk.Button(border, text="Book", font=("Arial", 15), height=1, width=5 ,command= book)
                    Button1.place(x=400, y=150)
                j = 0
                s += 1

            Button = tk.Button(self, text="back", font=("Arial bold", 17), height=1, width=5, command=lambda: controller.show_frame(Secondpage))
            Button.place(x=25, y=630)
            if s==7:
                Button = tk.Button(self, text="Next", font=("Arial bold", 17), height=1, width=5, command=lambda: controller.show_frame(Login2))
                Button.place(x=1090, y=630)
        package()

class Thirdpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("beach.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        border = tk.LabelFrame(self, text = 'Login', bg = 'white', bd=10, font=("Arial bold", 28))
        border.place(x=330, y=200, height=350, width=700)


        l1=tk.Label(border, text="Username", font=("Arial Bold", 20))
        l1.place(x=50,y=50)
        s1=tk.Entry(border, width=25, bd=5, font=(12))
        s1.place(x=240, y=50)

        l2 = tk.Label(border, text="Password",font=("Arial Bold", 20))
        l2.place(x=50, y=130)
        s2 = tk.Entry(border, show='*', width=25, bd=5, font=(12))
        s2.place(x=240, y=130)

        def login():
            global p
            if s1.get() == '' or s2.get() == '':
                showerror('Error', 'All Fields Are Required')
                delete()
            else:
                try:
                    p = s1.get()
                    con = pymysql.connect(host='localhost', user='root', password='Vmr123@*', database='register')
                    cur = con.cursor()
                    cur.execute('select * from user where username=%s and password=%s',
                                (s1.get(), s2.get()))
                    row = cur.fetchone()
                    if row == None:
                        showerror('error', 'Invalid Email or Password')

                    else:
                        controller.show_frame(AdminNext)

                    con.close()
                except Exception as e:
                    showerror('Error', f"Error due to: {e}")
                finally:
                    delete()
        def delete():
            s1.delete(0, 'end')
            s2.delete(0, 'end')

        Button = tk.Button(border, text="Submit", font=("Arial", 20, "bold"), command = login)
        Button.place(x=450, y=200)

        def register():
            global window
            window=tk.Tk()
            window.title("Register")
            window.resizable(0,0)
            l1 = tk.Label(window, text="Username", font=("Arial bold", 12))
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=25, bd=5, font=(12))
            t1.place(x=200, y=10)

            l2 = tk.Label(window, text="Password", font=("Arial bold", 12))
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=25, bd=5, font=(12))
            t2.place(x=200, y=60)

            l3 = tk.Label(window, text="Confirm Password", font=("Arial bold", 12))
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=25, bd=5, font=(12))
            t3.place(x=200, y=110)

            def check():
                if t1.get()=='' or t2.get()=='' or t3.get()=='':
                    showerror('Error', "All Fields Are Required", parent=window)
                elif t2.get() != t3.get():
                    showerror('Error', "Password Mismatch", parent = window)
                else:
                    try:
                        con = pymysql.connect(host='localhost', user='root', password='Vmr123@*', database='register')
                        cur = con.cursor()
                        cur.execute('select * from user where username=%s', t1.get())
                        row=cur.fetchone()
                        if row!=None:
                            messagebox.showerror('error', 'User already exits', parent = window)
                        else:
                            cur.execute('insert into user(username,password, confirm_password) values(%s, %s, %s)', (t1.get(), t2.get(), t3.get()))
                            con.commit()
                            con.close()

                            messagebox.showinfo('success', 'registration is successful')
                    except Exception as e:
                        messagebox.showerror('error', f'error due to {e}')
                    finally:
                        window.destroy()

            Button = tk.Button(window, text="Submit", font=("Arial", 20, "bold"), command= check)
            Button.place(x=300, y=160)

            window.geometry("700x250")
            window.mainloop()

        Button = tk.Button(border, text="Register New Account?", font=("Arial bold", 12), bd=0, fg='gray20', bg='white',
                           cursor='hand2', command=register)
        Button.place(x=80, y=190)

        Label = tk.Label(self, text="Admin", font=("Arial", 35, "bold"),
                         fg="grey", bg="white",
                         relief=RAISED,
                         bd=10,
                         padx=50, pady=10)

        Label.place(x=100, y=25)

        Button = tk.Button(self, text="Home", font=("Arial", 20, "bold"),
                           command=lambda: controller.show_frame(Firstpage))
        Button.place(x=25, y=620)

def getpasscode():
    global otp
    numbers = '1234567890'
    ot = random.choices(numbers, k=4)
    otp = ''.join(ot)
    messagebox.showinfo('passcode', 'Your passcode is ' + otp)
    Button1["state"] = DISABLED

def hotel_display():
    con = pymysql.connect(host='localhost', user='root', password='Vmr123@*', database='hotel')
    cur = con.cursor()
    cur.execute("select * from data where passcode=%s", otp)
    r = list(cur.fetchall())
    l=tk.Label(Frame1, text = 'Your Final Entries:', font = ('Arial bold', 22), bg='white', fg = 'grey')
    l.place(x=90, y=120)
    label3 = tk.Label(Frame1, text='Hotel name: ' + r[0][1] + '\n\nState: ' + r[0][2] + '\n\nCity: ' + r[0][3] + '\n\nPrice: ' + r[0][4], font=('Arial', 18), bg = "white")
    label3.place(x=100, y=180)

def hotel():
    Button2["state"] = DISABLED
    global window
    window = tk.Tk()
    window.title("Hotel")
    window.resizable(0, 0)
    l1 = tk.Label(window, text="Hotel Name", font=("Arial bold", 12))
    l1.place(x=10, y=10)
    t1 = tk.Entry(window, width=25, bd=5, font=(12))
    t1.place(x=200, y=10)



    l2 = tk.Label(window, text="State", font=("Arial bold", 12))
    l2.place(x=10, y=60)
    t2 = tk.Entry(window, width=25, bd=5, font=(12))
    t2.place(x=200, y=60)

    l3 = tk.Label(window, text="City", font=("Arial bold", 12))
    l3.place(x=10, y=110)
    t3= tk.Entry(window, width=25, bd=5, font=(12))
    t3.place(x=200, y=110)

    l4 = tk.Label(window, text="Price", font=("Arial bold", 12))
    l4.place(x=10, y=160)
    t4 = tk.Entry(window, width=25, bd=5, font=(12))
    t4.place(x=200, y=160)

    def check():
        if t1.get() == '' or t2.get() == '' or t3.get() == '' or t4.get() == '':
            showerror('Error', "All Fields Are Required", parent=window)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Vmr123@*', database='hotel')
                cur = con.cursor()
                cur.execute('select * from data where passcode=%s', otp)
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror('error', 'Wrong passcode', parent=window)
                else:
                    cur.execute(
                        'insert into data(passcode ,hotel_name, state, city, price) values(%s, %s, %s, %s, %s)',
                        (otp, t1.get(), t2.get(), t3.get(), t4.get()))
                    con.commit()
                    con.close()

                    messagebox.showinfo('Success', 'Your Entry is saved')
            except Exception as e:
                messagebox.showerror('error', f'error due to {e}')
            finally:
                window.destroy()
                hotel_display()

    Button = tk.Button(window, text="Save", font=("Arial", 20, "bold"), command=check)
    Button.place(x=300, y=260)
    window.geometry("700x350")
    window.mainloop()

def package_display():
    con = pymysql.connect(host='localhost', user='root', password='Vmr123@*', database='package')
    cur = con.cursor()
    cur.execute("select * from info where passcode=%s", otp)
    r = list(cur.fetchall())
    l = tk.Label(Frame1, text='Your Final Entries:', font=('Arial bold', 22), bg='white', fg='grey')
    l.place(x=90, y=120)
    label3 = tk.Label(Frame1,
                      text='Package name: ' + r[0][1] + '\n\nNumber of days: ' + r[0][2] + '\n\nPlaces name: ' + r[0][3] + '\n\nActivities: ' +
                           r[0][4]  + '\n\nPrice: ' + r[0][5], font=('Arial', 18), bg="white")
    label3.place(x=100, y=180)

def holiday_package():
    global window
    window = tk.Tk()
    window.title("Holiday package")
    window.resizable(0, 0)
    l1 = tk.Label(window, text="Package Name", font=("Arial bold", 12))
    l1.place(x=10, y=10)
    t1 = tk.Entry(window, width=25, bd=5, font=(12))
    t1.place(x=200, y=10)



    l3 = tk.Label(window, text="Number of days", font=("Arial bold", 12))
    l3.place(x=10, y=60)
    t3 = tk.Entry(window, width=25, bd=5, font=(12))
    t3.place(x=200, y=60)

    l4 = tk.Label(window, text="Places Name", font=("Arial bold", 12))
    l4.place(x=10, y=110)
    t4 = tk.Entry(window, width=25, bd=5, font=(12))
    t4.place(x=200, y=110)

    l5 = tk.Label(window, text="Activities", font=("Arial bold", 12))
    l5.place(x=10, y=160)
    t5 = tk.Entry(window, width=25, bd=5, font=(12))
    t5.place(x=200, y=160)

    l6 = tk.Label(window, text="Price", font=("Arial bold", 12))
    l6.place(x=10, y=210)
    t6 = tk.Entry(window, width=25, bd=5, font=(12))
    t6.place(x=200, y=210)

    def check():
        if t1.get() == ''  or t3.get() == '' or t4.get() == '' or t5.get() == '':
            showerror('Error', "All Fields Are Required", parent=window)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Vmr123@*', database='package')
                cur = con.cursor()
                cur.execute('select * from info where passcode=%s', otp)
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror('error', 'Wrong passcode', parent=window)
                else:
                    cur.execute(
                        'insert into info(passcode ,package_name, days, places_name, activities, price) values( %s, %s, %s, %s, %s, %s)',
                        (otp, t1.get(), t3.get(), t4.get(), t5.get(), t6.get()))
                    con.commit()
                    con.close()

                    messagebox.showinfo('Success', 'Your Entry is saved')
            except Exception as e:
                messagebox.showerror('error', f'error due to {e}')
            finally:
                window.destroy()
                package_display()

    Button = tk.Button(window, text="Submit", font=("Arial", 20, "bold"), command=check)
    Button.place(x=300, y=310)

    window.geometry("700x370")
    window.mainloop()

class AdminNext(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("beach.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        def create():
            selected = tk.StringVar()
            def selection(event):
                global Frame1
                Frame1 = tk.Frame(self, bg="white")
                Frame1.place(x=180, y=160, height=500, width=900)
                global Button1
                Button1 = tk.Button(Frame1, text="Get passcode", font=("Arial", 13, "bold"), command=getpasscode)
                Button1.place(x=400, y=8)

                def forall():
                    l = tk.Label(Frame1, text="Enter passcode", font=("Arial Bold", 13))
                    l.place(x=50, y=55)
                    t = tk.Entry(Frame1, width=15, bd=5, font=(12))
                    t.place(x=240, y=55)

                    def check():
                        if t.get() != otp:
                            messagebox.showerror('Error', 'Invalid passcode')
                            t.delete(0, 'end')

                        else:
                            try:
                                con = pymysql.connect(host='localhost', user='root', password='Vmr123@*',
                                                      database='register')
                                cur = con.cursor()
                                cur.execute("update user set passcode = %s where username = %s", (otp, p))
                                con.commit()


                            except Exception as e:
                                messagebox.showerror('error', f'error due to {e}')


                if selected.get() == 'Holiday package':
                    forall()
                    global Button2
                    Button2 = tk.Button(Frame1, text="Next", font=("Arial", 13, "bold"), command=holiday_package)
                    Button2.place(x=500, y=55)

                if selected.get() == 'Hotel':
                    forall()
                    Button2 = tk.Button(Frame1, text="Next", font=("Arial", 13, "bold"), command=hotel)
                    Button2.place(x=500, y=55)

            comboquestion = ttk.Combobox(self, font=('Arial', 20), state='readonly', justify=CENTER, textvariable=selected)
            comboquestion['values'] = (
            'Select', 'Hotel', 'Holiday package')
            comboquestion.current(0)
            comboquestion.place(x=450, y=100, width=350)
            comboquestion.bind('<<ComboboxSelected>>', selection)

        Button = tk.Button(self, text="Create", font=("Arial", 20, "bold"), command = create)
        Button.place(x=500, y=25)

        Button = tk.Button(self, text="Home", font=("Arial", 20, "bold"), command = lambda: controller.show_frame(Firstpage))
        Button.place(x=25, y=620)

class root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window=tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize = 700)
        window.grid_columnconfigure(0, minsize=1200)

        self.frames={}
        for F in (Firstpage, Secondpage, Thirdpage, AdminNext, Login1, Login2):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky = "nsew")

        self.show_frame(Firstpage)

    def show_frame(self, page):
        frame =self.frames[page]
        frame.tkraise()

app=root()
app.mainloop()
