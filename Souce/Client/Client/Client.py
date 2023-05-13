import socket
import time
from tkinter import*
from threading import Thread
import tkinter.ttk as exTk

def hienthi():
    if(checkDMY(int(day.get()) , int(month.get()) , int(year.get())) == False):
        print("Khong hop le")
    else :
        print("Hop le")

def checkDMY(ngay , thang , nam):
    if(ngay <= 0 or ngay >= 32) : 
        return False
    if(thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
        if(ngay < 1 or ngay > 31) : 
            return False
        else : 
            return True
    elif(thang == 4 or thang == 6 or thang == 9 or thang == 11):
        if(ngay < 1 or ngay > 30) : 
            return False
        else : 
            return True
    elif(thang == 2):
        if(nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)):
            if(ngay < 1 or ngay > 29) : 
                return False
            else : 
                return True
        else :
            if(ngay < 1 or ngay > 28) : 
                return False
            else : 
                return True
    else : 
        return False


def clickday(event):
    day.config(state = NORMAL)
    day.delete(0 , END)

def clickmonth(event):
    month.config(state = NORMAL)
    month.delete(0 , END)

def clickyear(event):
    year.config(state = NORMAL)
    year.delete(0 , END)

def clicktype(event):
    money.config(state = NORMAL)
    money.delete(0 , END)

def receive():
    try:
         msg = s.recv(1024).decode("utf8")
    except OSError: 
         print("Disconnection !")
         return
    return msg

def formatDMY():
    try :
       s.sendall(bytes(combo.get() , "utf8"))
       print('Send ' + combo.get())
       data1 = receive()
       if(data1 == '1') : 
           b = checkDMY(int(day.get()) , int(month.get()) , int(year.get()))
           if(b == False) : print("Check again !")
           else :
                if(day.get() >= '01' and day.get() <= '09') : dd = day.get()
                if(month.get() >= '01' and month.get() <= '09') : dd = day.get()
                if(int(day.get()) < 10) : dd = '0' + day.get()
                if(int(day.get()) >= 10) : dd = day.get()
                if(int(month.get()) < 10) : mm = '0' + month.get()
                if(int(month.get()) >= 10) : mm = month.get()
                if(int(year.get()) < 10) : yyyy = '000' + year.get()
                if(int(year.get()) < 100 and int(year.get()) >= 10) : yyyy = '00' + year.get()
                if(int(year.get()) < 1000 and int(year.get()) >= 100) : yyyy = '0' + year.get()
                if(int(year.get()) >= 1000 and int(year.get()) < 10000) : yyyy = year.get()
                text = str(dd +'/' + mm + '/' + yyyy)
                print('Send ' + text)
                s.sendall(bytes(text , "utf8"))
                data2 = receive()
                if(data2 == '2'):
                    s.sendall(bytes(money.get() , "utf8"))
                    print('Send ' + money.get())
                    data3 = receive()
                    global box
                    box = Text(search , width = 40 ,height = 10 , font = 'Times 15')
                    box.insert(END  , data3)
                    box.place(x = 170 , y = 350)
       else :
               print(data1)
    except OSError :
        print("Disconnected !")

def sendInfo():
    send_info = Thread(target = formatDMY)
    send_info.start()

def thoatGiaoDien() : 
    s.sendall(bytes("Clients left system" , "utf8"))
    search.destroy()

def searchingmoney():
    try :
        global day , month , year , money , combo
        global search
        search = Tk()
        search.title("Searching")
        scr=search.winfo_screenwidth()
        scr=search.winfo_screenheight()
        search.geometry('730x700+%d+%d' % (scr/2-250, scr/2-300))
        show = Label(search , text = 'Searching Money'  , font = 'Times 33 bold italic' , borderwidth = 70).pack()
        day = Entry(search , width = 20 , font = 'Times 10')
        day.insert(0, 'Enter day')
        day.config(state = DISABLED)
        day.bind("<Button-1>" , clickday)
        month = Entry(search , width = 20 , font = 'Times 10')
        month.insert(0, 'Enter month')
        month.config(state = DISABLED)
        month.bind("<Button-1>" , clickmonth)
        year = Entry(search , width = 20 , font = 'Times 10')
        year.insert(0, 'Enter year')
        year.config(state = DISABLED)
        year.bind("<Button-1>" , clickyear)
        money = Entry(search , width = 20 , font = 'Times 10')
        money.insert(0, 'Enter type of money')
        money.config(state = DISABLED)
        money.bind("<Button-1>" , clicktype)
        combo = exTk.Combobox(search , width = 20 , state = 'readonly')
        combo['values'] = ('AgriBank' , 'VietcomBank' , 'VietinBank' , 'TechcomBank' , 'SacomBank')
        accept = Button(search , text = "Enter" , font = 'Times 18 bold' , command = sendInfo)
        thoat = Button(search , text = "Exit" , font = 'Times 18 bold' , command = thoatGiaoDien)
        day.place(x = 90 , y = 200)
        month.place(x = 295 , y = 200)
        year.place(x = 500 , y = 200)
        money.place(x =  295 , y = 250)
        combo.place(x = 295 , y = 150)
        accept.place(x = 200 , y = 650)
        thoat.place(x = 500, y = 650)
        search.mainloop()
    except OSError :
        print("Disconnected !")


def click(event):
    user.config(state = NORMAL)
    user.delete(0 , END)

def click2(event) :
    password.config(state = NORMAL)
    password.delete(0 , END)

def click3(event):
    user1.config(state = NORMAL)
    user1.delete(0 , END)

def click4(event):
    password1.config(state = NORMAL)
    password1.delete(0 , END)

def click5(event):
    ip.config(state = NORMAL)
    ip.delete(0 , END)

def click6(event) :
    port.config(state = NORMAL)
    port.delete(0 , END)

def sendthreading():
    try :
        global s , user , password
        s.sendall(bytes('in' , "utf8"))
        c = receive()
        if(c == 'c'):
            s.sendall(bytes(user.get() , "utf8"))
        elif(c != 'c') : print(c)
        a = receive()
        if(a == 'a'):
            s.sendall(bytes(password.get() , "utf8"))
        tk = receive()
        if(tk == 'Fail'):
            Label(top , text='●', font='Times 18 bold', fg='red').place(x = 180 , y = 500)
            Label(top , text = "Check again !" , font = 'Times 18 bold').place(x = 200 , y = 500)
            print('Check again')
        if(tk != 'Fail'):
            Label(top , text='●', font='Times 18 bold', fg='limegreen').place(x = 130 , y = 500)
            Label(top , text = "Login succesfully !" , font = 'Times 18 bold').place(x = 160 , y = 500)
            print('Login succesfully')
            time.sleep(2)
            top.withdraw()
            searchingmoney()
    except OSError :
        print("Disconnected !")
            
def sendMess():
    send_thread = Thread(target = sendthreading)
    send_thread.start()
        
def sendtext():
    try :
        global s , user1 , password1 , top
        s.sendall(bytes('up' , "utf8"))
        c = receive()
        if(c == 'c'):
            s.sendall(bytes(user1.get() , "utf8"))
        elif(c != 'c') : print(c)
        a = receive()
        if(a == 'a'):
            s.sendall(bytes(password1.get() , "utf8"))
        tk = receive()
        print(tk)
        if(tk == 'Fail'):
            Label(login , text='●', font='Times 18 bold', fg='red').place(x = 100 , y = 500)
            Label(login , text = "Account already exists !" , font = 'Times 18 bold').place(x = 120 , y = 500)
            print('Account already exists !')
        if(tk != 'Fail'):
            print('Register succesfully')
            login.withdraw()
            top.deiconify()
    except OSError :
        print("Disconnected !")

def textThreading():
    send_thread = Thread(target = sendtext)
    send_thread.start()

def create():
    try :
        time.sleep(2)
        connect.withdraw()
        global top , user , password
        top = Tk()
        top.title("MoneySystem")
        scrW1=top.winfo_screenwidth()
        scrH1=top.winfo_screenheight()
        top.geometry('500x600+%d+%d' % (scrW/2-250, scrH/2-300))
        text = Label(top , text = 'Welcome to MoneySystem'  , font = 'Times 33 bold italic' , borderwidth = 70)
        user = Entry(top , width = 30 , font = 'Times 12')
        user.insert(0, 'Enter your user')
        user.config(state = DISABLED)
        user.bind("<Button-1>" , click)
        password = Entry(top , width = 30 , font = 'Times 12' , show = '*')
        password.insert(0, 'Enter your password')
        password.config(state = DISABLED)
        password.bind("<Button-1>" , click2)
        Enter = Button(top , text = "Sign in" , font = 'Times 15 bold italic' ,  command = sendMess)
        Register = Button(top , text = "Sign up" , font = 'Times 15 bold italic' , command = register)
        text.pack()
        user.pack()
        user.focus()
        password.pack()
        Enter.pack()
        Register.pack()
        top.mainloop()
    except OSError :
        print("Disconnected !")


def connection() : 
    try:
        hostAdd = ip.get()
        portAdd = port.get()
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (hostAdd , int(portAdd))
        s.connect(server_address)
        boot = Label(connect , text = "●" ,  font = 'Times 18' , fg = 'limegreen').place(x = 50 , y = 500)
        boot1 = Label(connect , text = "  Connection has been established !" ,  font = 'Times 18 bold' , fg = 'black').place(x = 70, y = 500)
        print(server_address)
        receive_thread = Thread(target = create)
        receive_thread.start()
        global search
    except OSError :
        print("Disconnected !")

def register():
    try : 
        top.withdraw()
        global login ,user1 , password1
        login = Tk()
        login.title("Register")
        sc=login.winfo_screenwidth()
        sc=login.winfo_screenheight()
        login.geometry('500x600+%d+%d' % (sc/2-250, sc/2-300))
        text1 = Label(login , text = 'Create new account'  , font = 'Times 35 bold italic' , borderwidth = 70)
        user1 = Entry(login , width = 30 , font = 'Times 12 ')
        user1.insert(0, 'Enter your user')
        user1.config(state = DISABLED)
        user1.bind("<Button-1>" , click3)
        password1 = Entry(login , width = 30 , show = '*' , font = 'Times 12')
        password1.insert(0, 'Enter your password')
        password1.config(state = DISABLED)
        password1.bind("<Button-1>" , click4)
        Enter1 = Button(login , text = "Enter" , font = 'Times 15 bold italic'  , command = textThreading)
        text1.pack()
        user1.pack()
        user1.focus()
        password1.pack()
        Enter1.pack()
        login.mainloop()
    except OSError :
        print("Disconnected !")


def exitCode():
    try : 
        print("Exit")
        connect.destroy()
    except OSError :
        print("Disconnected !")


connect = Tk()
connect.title("Connection")
scrW=connect.winfo_screenwidth()
scrH=connect.winfo_screenheight()
connect.geometry('500x600+%d+%d' % (scrW/2-250, scrH/2-300))
dataa = Label(connect , text = 'Connection System'  , font = 'Times 33 bold italic italic' , borderwidth = 70)
ip = Entry(connect , width = 30 , font = 'Times 12')
ip.insert(0, 'Enter IP')
ip.config(state = DISABLED)
ip.bind("<Button-1>" , click5)
port = Entry(connect , width = 30 , font = 'Times 12')
port.insert(0, 'Enter Port')
port.config(state = DISABLED)
port.bind("<Button-1>" , click6)
connectButton = Button(connect , text = "Connect"  , font = 'Times 15 bold' , command = connection)
exit = Button(connect , text = "Exit" , font = 'Times 15 bold' , command = exitCode)
bost1 = Label(connect , text='●', font='Times 18 bold', fg='limegreen')
bost2 = Label(connect , text=' Ready to connect', font='Times 18 bold', fg='black')
dataa.pack()
ip.pack()
port.pack()
connectButton.pack()
exit.pack()
bost1.place(x = 130 , y = 500)
bost2.place(x = 150 , y = 500)
print('---------------CLIENT----------------- \n')
connect.mainloop()

