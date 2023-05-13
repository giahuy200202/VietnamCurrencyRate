import socket
import time
from tkinter import *
import threading
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import concurrent.futures

win=Tk()
win.title('Server connection')

def updateData(bank, client):
    while True:
        try:
            time.sleep(1800)
            notice='--------Updating data for '+bank +'---------'
            print(notice)
            if(bank=='AgriBank'):
                AgribankProcessing(client)
            elif(bank=='VietcomBank'):
                VietcombankProcessing(client)
            elif(bank=='VietinBank'):
                VietinbankProcessing(client)
            elif(bank=='TechcomBank'):
                TechcombankProcessing(client)
            elif(bank=='SacomBank'):
                SacombankProcessing(client)
        except OSError:
            print('Disconnected')
            break;
            
def ConnectAndSaveToJsonAgri(date):
    try:
        data={}
        n=1
        browser=webdriver.Chrome(executable_path="chromedriver.exe")
        browser.get("https://www.agribank.com.vn/vn/ty-gia")
        us=browser.find_element_by_id("dateStart")
        for i in range(10):
            us.send_keys(Keys.BACKSPACE)
        us.send_keys(date)
        time.sleep(1)
        us.send_keys(Keys.ENTER)
        time.sleep(1)
        cur=cash=transfer=sell=''
        for i in browser.find_elements_by_tag_name('tr'):
            n=1
            for k in i.find_elements_by_tag_name('td'):
                if(n==1): cur=k.text
                elif(n==2): cash=k.text
                elif(n==3): transfer=k.text
                elif(n==4): sell=k.text
                n+=1   
            data[cur]=[]
            data[cur].append({'Cash':cash, 'Transfer':transfer, 'Sell':sell})
        browser.close()
        with open('agribank.json', 'w') as file:
            json.dump(data, file)
    except OSError:
            print('Disconnected')
    
def AgribankProcessing(client):
    try:
        ConnectAndSaveToJsonAgri(date)
        obj=json.loads(open('agribank.json', 'r').read())
        if((currency not in obj) ==True): 
            stringSend='Agribank does not have '+currency+' currency'
        else:
            list=obj[currency]
            cash=list[0].get("Cash")
            trans=list[0].get("Transfer")
            sell=list[0].get("Sell")
            stringSend='AGRIBANK\nCurrency: '+currency+'\nBuy Cash: '+cash+'\nBuy Transfer: '+trans+'\nSell: '+sell
        print(stringSend)
        client.send(bytes(stringSend, "utf8"))
        threading.Thread(target=updateData, args=(bank, client,)).start()
    except OSError:
            print('Disconnected')

def ConnectAndSaveToJsonVietcom(date):
    try:
        data={}
        n=1
        browser=webdriver.Chrome(executable_path="chromedriver.exe")
        browser.get("https://portal.vietcombank.com.vn/Personal/TG/Pages/ty-gia.aspx?devicechannel=default")
        us=browser.find_element_by_id("txttungay")
        for i in range(10):
            us.send_keys(Keys.BACKSPACE)
        us.send_keys(date)
        time.sleep(0.5)
        us.send_keys(Keys.ENTER)
        us.send_keys(Keys.ENTER)
        time.sleep(1)
        cur=cash=transfer=sell=''
        for i in browser.find_elements_by_class_name('odd'):
            n=1
            for k in i.find_elements_by_tag_name('td'):
                if(n==2): cur=k.text
                elif(n==3): cash=k.text
                elif(n==4): transfer=k.text
                elif(n==5): sell=k.text
                n+=1
            data[cur]=[]
            data[cur].append({'Cash':cash, 'Transfer':transfer, 'Sell':sell})
        browser.close()
        with open('vietcombank.json', 'w') as file:
            json.dump(data, file)
    except OSError:
            print('Disconnected')
def VietcombankProcessing(client):
    try:
        ConnectAndSaveToJsonVietcom(date)
        obj=json.loads(open('vietcombank.json', 'r').read())
        if((currency not in obj) ==True): 
            stringSend='Vietcombank does not have '+currency+' currency'
        else:
            list=obj[currency]
            cash=list[0].get("Cash")
            trans=list[0].get("Transfer")
            sell=list[0].get("Sell")
            stringSend='VIETCOMBANK\nCurrency: '+currency+'\nBuy Cash: '+cash+'\nBuy Transfer: '+trans+'\nSell: '+sell
        print(stringSend)
        client.send(bytes(stringSend, "utf8"))
        threading.Thread(target=updateData, args=(bank, client,)).start()
    except OSError:
            print('Disconnected')

def ConnectAndSaveToJsonVietin(date):
    try:
        data={}
        n=1
        browser=webdriver.Chrome(executable_path="chromedriver.exe")
        browser.get("https://www.vietinbank.vn/web/home/vn/ty-gia/")
        us=browser.find_element_by_name("theDate")
        for i in range(10):
            us.send_keys(Keys.BACKSPACE)
        us.send_keys(date)
        browser.find_element_by_xpath('//*[@id="articles"]/form/input[2]').click()
        time.sleep(1)
        cur=cash=transfer=sell=''
        m=1
        for i in browser.find_elements_by_tag_name('tr'):
            n=1
            if(m>5 and m!=12 and m!=17 and m!=18 and m!=20 and m<24):
               for k in i.find_elements_by_tag_name('td'):
                   if(n==1): cur=k.text
                   elif(n==3): cash=k.text
                   elif(n==4): transfer=k.text
                   elif(n==5): sell=k.text
                   n+=1
                   data[cur]=[]
                   data[cur].append({'Cash':cash, 'Transfer':transfer, 'Sell':sell})
            m+=1
        browser.close()
        with open('viettin.json', 'w') as file:
            json.dump(data, file)
    except OSError:
            print('Disconnected')
def VietinbankProcessing(client):
    try:
        ConnectAndSaveToJsonVietin(date)
        obj=json.loads(open('viettin.json', 'r').read())
        if((currency not in obj) ==True): 
            stringSend='Vietinbank does not have '+currency
        else:
            list=obj[currency]
            cash=list[0].get("Cash")
            trans=list[0].get("Transfer")
            sell=list[0].get("Sell")
            stringSend='VIETINBANKK\nCurrency: '+currency+'\nBuy Cash: '+cash+'\nBuy Transfer: '+trans+'\nSell: '+sell
        print(stringSend)
        client.send(bytes(stringSend, "utf8"))
        threading.Thread(target=updateData, args=(bank, client,)).start()
    except OSError:
            print('Disconnected')

def ConnectAndSaveToJsonTech(date):
    try:
        data={}
        n=1
        browser=webdriver.Chrome(executable_path="chromedriver.exe")
        browser.get("https://www.techcombank.com.vn/cong-cu-tien-ich/ti-gia/ti-gia-hoi-doai")
        us=browser.find_element_by_xpath('/html/body/div[10]/div/div[2]/div[4]/table/tbody/tr/td[2]/input')
        for i in range(10):
            us.send_keys(Keys.BACKSPACE)
        us.send_keys(date)
        time.sleep(1)
        us.send_keys(Keys.ENTER)
        us.send_keys(Keys.ENTER)
        us.send_keys(Keys.ENTER)
        us.send_keys(Keys.ENTER)
        time.sleep(2)
        cur=cash=transfer=sell=''
        m=1
        for i in browser.find_elements_by_tag_name('tr'):
            n=1
            if(m>=10 and m%2==0 and m!=32 and m!=28 and m!=26 and m<=33):
               for k in i.find_elements_by_tag_name('td'):
                   if(n==1): 
                       cur=k.text.replace(' ', '')
                       if(m==10): cur=cur.replace(',50-100','')
                   elif(n==2): cash=k.text.replace(' ', '')
                   elif(n==3): transfer=k.text.replace(' ', '')
                   elif(n==4): sell=k.text.replace(' ', '')
                   n+=1
                   data[cur]=[]
                   data[cur].append({'Cash':cash, 'Transfer':transfer, 'Sell':sell})
            m+=1
        with open('techcombank.json', 'w') as file:
            json.dump(data, file)
    except OSError:
            print('Disconnected')
def TechcombankProcessing(client):
    try:
        ConnectAndSaveToJsonTech(date)
        obj=json.loads(open('techcombank.json', 'r').read())
        if((currency not in obj) ==True): 
            stringSend='Techcombank does not have '+currency
        else:
            list=obj[currency]
            cash=list[0].get("Cash")
            trans=list[0].get("Transfer")
            sell=list[0].get("Sell")
            stringSend='TECHCOMBANK\nCurrency: '+currency+'\nBuy Cash: '+cash+'\nBuy Transfer: '+trans+'\nSell: '+sell
        print(stringSend)
        client.send(bytes(stringSend, "utf8"))
        threading.Thread(target=updateData, args=(bank, client,)).start()
    except OSError:
            print('Disconnected')

def ConnectAndSaveToJsonSacom(date):
    try:
        data={}
        n=1
        browser=webdriver.Chrome(executable_path="chromedriver.exe")
        browser.get("https://www.sacombank.com.vn/company/Pages/ty-gia.aspx")
        us=browser.find_element_by_xpath("/html/body/form/div[11]/div[3]/div[2]/main/div[4]/div/div[3]/section[2]/div/div/div[2]/div/div[1]/div/div[1]/div/input")
        for i in range(10):
            us.send_keys(Keys.BACKSPACE)
        us.send_keys(date)
        browser.find_element_by_xpath('//*[@id="dtpNgayMoney"]/span/i').click()
        browser.find_element_by_xpath('//*[@id="dtpNgayMoney"]/span/i').click()
        time.sleep(3)
        cur=cash=transfer=sell=''
        m=1
        for i in browser.find_elements_by_class_name('tr-items'):
            n=1
            if(m<=8):
               for k in i.find_elements_by_tag_name('td'):
                   if(n==1): cur=k.text
                   elif(n==2): cash=k.text
                   elif(n==3): transfer=k.text
                   elif(n==5): sell=k.text
                   n+=1
                   data[cur]=[]
                   data[cur].append({'Cash':cash, 'Transfer':transfer, 'Sell':sell})
            m+=1
        browser.close()
        with open('sacombank.json', 'w') as file:
            json.dump(data, file)
    except OSError:
            print('Disconnected')
def SacombankProcessing(client):
    try:
        ConnectAndSaveToJsonSacom(date)
        obj=json.loads(open('sacombank.json', 'r').read())
        if((currency not in obj) ==True): 
            stringSend='Sacombank does not have '+currency
        else:
            list=obj[currency]
            cash=list[0].get("Cash")
            trans=list[0].get("Transfer")
            sell=list[0].get("Sell")
            stringSend='SACOMBANK\nCurrency: '+currency+'\nBuy Cash: '+cash+'\nBuy Transfer: '+trans+'\nSell: '+sell
        print(stringSend)
        client.send(bytes(stringSend, "utf8"))
        threading.Thread(target=updateData, args=(bank, client,)).start()
    except OSError:
            print('Disconnected')

def receiveMoneyInfo(client):
    while True:
        try:
            global bank
            bank=client.recv(1024).decode()
            print('Server recieve bank from client: ', bank)
            if(bank!=''): 
                client.send(bytes('1', "utf8"))
            global date
            date=client.recv(1024).decode()
            print('Server recieve date from client: ', date)
            if(date!=''): 
                client.send(bytes('2', "utf8"))
            global currency
            currency=client.recv(1024).decode()
            print('Server recieve currency from client: ', currency)
            if(bank=='AgriBank'):
                print('----------Processing-----------')
                AgribankProcessing(client)
            elif(bank=='VietcomBank'):
                print('----------Processing-----------')
                VietcombankProcessing(client)
            elif(bank=='VietinBank'):
                print('----------Processing-----------')
                VietinbankProcessing(client)
            elif(bank=='TechcomBank'):
                print('----------Processing-----------')
                TechcombankProcessing(client)
            elif(bank=='SacomBank'):
                print('----------Processing-----------')
                SacombankProcessing(client)
        except OSError:
            print('Disconnected')
            break

def signIn(client, name1, name2):
    try:
        temp=0
        f1=open('Username.txt', mode='r')
        f1.seek(0)
        userAlreadyExist=0
        lineN_th=0
        while True:
            user_=f1.readline()
            user_=user_.replace('\n','')
            if(user_==''): break
            elif(user_==name1): 
                userAlreadyExist+=1
                break
            lineN_th+=1
        f1.close() 

        f2=open('Password.txt', mode='r')
        f2.seek(0)
        passwordAlreadyExist=0
        index=0
        while True:
            pass_=f2.readline()
            pass_=pass_.replace('\n','')
            if(pass_==''): break
            if(index==lineN_th):
                if(name2==pass_):
                    passwordAlreadyExist+=1
                    break
            index+=1
        f2.close()
        if(userAlreadyExist==1 and passwordAlreadyExist==1):
            temp+=1
            client.send(bytes('Sucess', "utf8"))
        else:
            client.send(bytes('Fail', "utf8"))
        return temp
    except OSError:
            print('Disconnected')

def signUp(client, name1, name2):
    try:
        temp=0
        f1=open('Username.txt', mode='a+')
        f2=open('Password.txt', mode='a+')
        userAlreadyExist=0
        f1.seek(0)
        while True:
            userRead=f1.readline()
            userPass=f2.readline()
            userRead=userRead.replace('\n','')
            if(userRead==''): break
            elif(name1==userRead): 
                userAlreadyExist+=1 
                break
        if(userAlreadyExist==0):
            temp+=1
            userWrite=f1.write(name1+'\n')
            passWrite=f2.write(name2+'\n')
            client.send(bytes('Sucess', "utf8"))
        else:
            client.send(bytes('Fail', "utf8"))
        f1.close()
        f2.close()
        return temp
    except OSError:
            print('Disconnected')

def loopForSignInSignUp(client):

    while True:
        try:
            choice=client.recv(1024).decode()
            if(choice!=''): client.send(bytes('c',"utf8"))
            name1=client.recv(1024).decode()
            if(name1!=''): client.send(bytes('a',"utf8"))
            name2=client.recv(1024).decode()
            print('Server recieved username from client: ' + name1)
            print('Server recieved password from client: ' + name2)

            if(choice=='in'):
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(signIn, client, name1, name2)
                    return_value = future.result()
                if(return_value==1):
                    break
                    print("Client signin success")
                else: print('Client signin fail')
                
            elif(choice=='up'):
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(signUp, client, name1, name2)
                    return_value = future.result()
                if(return_value==1):
                    print("Client signup success")
                else: print('Client signup fail')
        except OSError:
            msg = s.recv(1024).decode("utf8")
            print(msg)
            print('Disconnected')
            break
    threading.Thread(target=receiveMoneyInfo, args=(client,)).start()

def exit(client):
    client.send(bytes('Server left system', 'utf8'))
    print("Server left system")
    win.destroy()

clients={}

def connect():
    try:
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip.get(), int(port.get())))
        s.listen(100)
        Label(win, text='●', font='Times 12 bold italic', fg='goldenrod').place(x=10, y=269)
        Label(win, text='Waiting for client      ', font='Times 11').place(x=29, y=270)
        n=0
        Label(win, text='●', font='Times 12 bold italic', fg='goldenrod').place(x=10, y=269)
        Label(win, text='Waiting for client      ', font='Times 11').place(x=29, y=270)
        while True:
            client, addr = s.accept()
            clients[client]=client
            if(n==0):  Label(win, text='Client', font='Times 11 bold').place(x=90, y=120 )
            n+=1
            Label(win, text=addr, font='Times 11').place(x=65, y=130 + n*20)
            print('Connected with: ', addr, '\n')
            Label(win, text='●', font='Times 12 bold italic', fg='limegreen').place(x=10, y=269)
            Label(win, text='Connect successfully     ', font='Times 11').place(x=29, y=270)
            Button(win , text = 'Exit' , font = 'Times 16 bold' , borderwidth = 5 , width =  5, height = 1 , command =lambda: exit(client)).place(x=290, y=240)
            threading.Thread(target=loopForSignInSignUp, args=(clients[client],)).start()
    except OSError:
            msg = s.recv(1024).decode("utf8")
            print(msg)
            print('Disconnected')

def connectServer():
    Label(win, text='●', font='Times 12 bold italic', fg='limegreen').place(x=10, y=269)
    Label(win, text='Ready to connect', font='Times 11').place(x=29, y=270)
    threading.Thread(target=connect).start()

scrW=win.winfo_screenwidth()
scrH=win.winfo_screenheight()
win.geometry('400x300+%d+%d' % (scrW/2-200, scrH/2-150))

Label(win, text='SERVER CONNECTION', font='Times 13 bold underline').place(x = 20, y=15)

Label(win, text='IP', font = 'Times 11' ).place(x = 15, y = 50)
ip=Entry(win,  font = 'Times 11 ')
ip.place(x = 65, y = 52)

Label(win, text='Port', font = 'Times 11' ).place(x = 15, y = 80)
port=Entry(win,  font = 'Times 11 ')
port.place(x = 65, y = 82)

Button(win, text='Connect', font = 'Times 16 bold', borderwidth=5, width=10, height=2, command=connectServer). place(x=230, y=40)
Label(win, text='●', font='Times 12 bold italic', fg='limegreen').place(x=10, y=269)
Label(win, text='Ready to connect', font='Times 11').place(x=29, y=270)
print('---------------SERVER----------------- \n') 
win.mainloop()