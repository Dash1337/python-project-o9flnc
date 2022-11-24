from tkinter import *


subs=Tk()
subs.title("Subnet Calculator")
subs.geometry("400x100+100+200")
subs.resizable(False,False)
subs.configure(bg="#000000")

def number():
    label_result2.config(text= str(entry1.get()) +"."+ str(entry2.get()) +"."+ str(entry3.get()) +"."+ str(entry4.get()))
    try:
        if 0 <= int(entry1.get()) <= 126:
            label_result1.config(text="A Típusú (0-126)")
        if 127 <= int(entry1.get()) <= 191:
            label_result1.config(text="B Típusú (127-191)")
        if int(entry1.get()) >= 192:
            label_result1.config(text="C Típusú (192+)")
    except ValueError:
        label_result1.config(text="Bránero")

    try:
        if int(entry5.get()) > 32:
            label_result3.config(text="No")
        if int(entry5.get()) == 32:
            label_result3.config(text="255.255.255.255")
            label_result4.config(text="Hostok száma: 1")
        if int(entry5.get()) == 31:
            label_result3.config(text="255.255.255.254")
            label_result4.config(text="Hostok száma: 2")
        if int(entry5.get()) == 30:
            label_result3.config(text="255.255.255.252")
            label_result4.config(text="Hostok száma: 4")
        if int(entry5.get()) == 29:
            label_result3.config(text="255.255.255.248")
            label_result4.config(text="Hostok száma: 8")
        if int(entry5.get()) == 28:
            label_result3.config(text="255.255.255.240")
            label_result4.config(text="Hostok száma: 16")
        if int(entry5.get()) == 27:
            label_result3.config(text="255.255.255.224")
            label_result4.config(text="Hostok száma: 32")
        if int(entry5.get()) == 26:
            label_result3.config(text="255.255.255.192")
            label_result4.config(text="Hostok száma: 64")
        if int(entry5.get()) == 25:
            label_result3.config(text="255.255.255.128")
            label_result4.config(text="Hostok száma: 128")
        if int(entry5.get()) == 24:
            label_result3.config(text="255.255.255.0")
            label_result4.config(text="Hostok száma: 256")
        if int(entry5.get()) == 23:
            label_result3.config(text="255.255.254.0")
            label_result4.config(text="Hostok száma: 512")
        if int(entry5.get()) == 22:
            label_result3.config(text="255.255.252.0")
            label_result4.config(text="Hostok száma: 1024")
        if int(entry5.get()) == 21:
            label_result3.config(text="255.255.248.0")
            label_result4.config(text="Hostok száma: 2048")
        if int(entry5.get()) == 20:
            label_result3.config(text="255.255.240.0")
            label_result4.config(text="Hostok száma: 4096")
        if int(entry5.get()) == 19:
            label_result3.config(text="255.255.224.0")
            label_result4.config(text="Hostok száma: 8192")
        if int(entry5.get()) == 18:
            label_result3.config(text="255.255.192.0")
            label_result4.config(text="Hostok száma: 16382")
        if int(entry5.get()) == 17:
            label_result3.config(text="255.255.128.0")
            label_result4.config(text="Hostok száma: 32768")
        if int(entry5.get()) == 16:
            label_result3.config(text="255.255.0.0")
            label_result4.config(text="Hostok száma: 65536")
        if int(entry5.get()) == 15:
            label_result3.config(text="255.254.0.0")
            label_result4.config(text="Hostok száma: 131072")
        if int(entry5.get()) == 14:
            label_result3.config(text="255.252.0.0")
            label_result4.config(text="Hostok száma: 262144")
        if int(entry5.get()) == 13:
            label_result3.config(text="255.248.0.0")
            label_result4.config(text="Hostok száma: 524288")
        if int(entry5.get()) == 12:
            label_result3.config(text="255.240.0.0")
            label_result4.config(text="Hostok száma: 1048576")
        if int(entry5.get()) == 11:
            label_result3.config(text="255.224.0.0")
            label_result4.config(text="Hostok száma: 2097152")
        if int(entry5.get()) == 10:
            label_result3.config(text="255.192.0.0")
            label_result4.config(text="Hostok száma: 4194304")
        if int(entry5.get()) == 9:
            label_result3.config(text="255.128.0.0")
            label_result4.config(text="Hostok száma: 8388608")
        if int(entry5.get()) == 8:
            label_result3.config(text="255.0.0.0")
            label_result4.config(text="Hostok száma: 16777216")
        if int(entry5.get()) == 7:
            label_result3.config(text="254.0.0.0")
            label_result4.config(text="Hostok száma: 33554432")
        if int(entry5.get()) == 6:
            label_result3.config(text="252.0.0.0")
            label_result4.config(text="Hostok száma: 67108864")
        if int(entry5.get()) == 5:
            label_result3.config(text="248.0.0.0")
            label_result4.config(text="Hostok száma: 134217728")
        if int(entry5.get()) == 4:
            label_result3.config(text="240.0.0.0")
            label_result4.config(text="Hostok száma: 268435456")
        if int(entry5.get()) == 3:
            label_result3.config(text="224.0.0.0")
            label_result4.config(text="Hostok száma: 67108864")
        if int(entry5.get()) == 2:
            label_result3.config(text="192.0.0.0")
            label_result4.config(text="Hostok száma: 536870912")
        if int(entry5.get()) == 1:
            label_result3.config(text="128.0.0.0")
            label_result4.config(text="Hostok száma: 1073741824")
        if int(entry5.get()) == 0:
            label_result3.config(text="0.0.0.0")
            label_result4.config(text="Hostok száma: 2147483648")

    except ValueError:
        label_result3.config(text="")

#IP bemenet
entry1 = Entry(subs, width=3, font=("Arial",12),bg="#211F45",fg="#fff")
entry1.place(x=0,y=0)
entry2 = Entry(subs, width=3,font=("Arial",12),bg="#211F45",fg="#fff")
entry2.place(x=32,y=0)
entry3 = Entry(subs, width=3,font=("Arial",12),bg="#211F45",fg="#fff")
entry3.place(x=64,y=0)
entry4 = Entry(subs, width=3,font=("Arial",12),bg="#211F45",fg="#fff")
entry4.place(x=96,y=0)
entry5 = Entry(subs, width=3,font=("Arial",12),bg="#211F45",fg="#fff")
entry5.place(x=130,y=0)

#IP kimenet
label_result1= Label(subs,text="",font=("arial",10),bg="#000000",fg="#fff")
label_result1.place(x=200,y=0)

label_result2= Label(subs,text="",font=("arial",10),bg="#000000",fg="#fff")
label_result2.place(x=0,y=50)

label_result3= Label(subs,text="",font=("arial",10),bg="#000000",fg="#fff")
label_result3.place(x=200,y=30)

label_result4= Label(subs,text="",font=("arial",10),bg="#000000",fg="#fff")
label_result4.place(x=200,y=50)

example = Label(subs,text="Példa: 192.168.1.0/25",font=("arial",10),bg="#000000",fg="#fff")
example.place(x=0,y=75);

button1 = Button(subs, text="Számolj", height=1, width=7,fg="#fff",bg="#830000", font=("arial",10),command=number)
button1.place(x=0,y=27)

subs.mainloop()