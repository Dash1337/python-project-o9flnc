import tkinter
from tkinter import *

home=tkinter.Tk()
home.title("Emergency Calculator")
home.geometry("570x600+100+200")
home.resizable(False,False)
home.configure(bg="#000000")

egyenlet = ""

def show(value):
    global egyenlet
    egyenlet+=value
    label_result1.config(text=egyenlet)

def clear():
    global egyenlet
    egyenlet =""
    label_result1.config(text=egyenlet)

def eredmeny():
    global egyenlet
    result =""
    if egyenlet !="":
        try:
            result= eval(egyenlet)
        except:
            result="error"
            egyenlet=""
    label_result1.config(text=result)

label_result1= Label(home, width=25, height=2, text="",font=("arial",30),bg="#000000",fg="#fff")
label_result1.pack()
#sor 1
Button(home, text="C", height=1, width=5,bd=1,fg="#fff",bg="#830000", font=("arial",30,"bold"),command=lambda: clear()).place(x=10,y=100)
Button(home, text="/", height=1, width=5,bd=1,fg="#fff",bg="#130E5B", font=("arial",30,"bold"),command=lambda: show("/")).place(x=150,y=100)
Button(home, text="%", height=1, width=5,bd=1,fg="#fff",bg="#130E5B", font=("arial",30,"bold"),command=lambda: show("%")).place(x=290,y=100)
Button(home, text="*", height=1, width=5,bd=1,fg="#fff",bg="#130E5B", font=("arial",30,"bold"),command=lambda: show("*")).place(x=430,y=100)

#sor 2
Button(home, text="7", height=1, width=5,bd=1,fg="#fff",bg="#211F45", font=("arial",30,"bold"),command=lambda: show("7")).place(x=10,y=200)
Button(home, text="8", height=1, width=5,bd=1,fg="#fff",bg="#211F45", font=("arial",30,"bold"),command=lambda: show("8")).place(x=150,y=200)
Button(home, text="9", height=1, width=5,bd=1,fg="#fff",bg="#211F45", font=("arial",30,"bold"),command=lambda: show("9")).place(x=290,y=200)
Button(home, text="-", height=1, width=5,bd=1,fg="#fff",bg="#130E5B", font=("arial",30,"bold"),command=lambda: show("-")).place(x=430,y=200)

#sor 3
Button(home, text="4", height=1, width=5,bd=1,fg="#fff",bg="#211F45", font=("arial",30,"bold"),command=lambda: show("4")).place(x=10,y=300)
Button(home, text="5", height=1, width=5,bd=1,fg="#fff",bg="#211F45", font=("arial",30,"bold"),command=lambda: show("5")).place(x=150,y=300)
Button(home, text="6", height=1, width=5,bd=1,fg="#fff",bg="#211F45", font=("arial",30,"bold"),command=lambda: show("6")).place(x=290,y=300)
Button(home, text="+", height=1, width=5,bd=1,fg="#fff",bg="#130E5B", font=("arial",30,"bold"),command=lambda: show("+")).place(x=430,y=300)

#sor 4
Button(home, text="1", height=1, width=5,bd=1,fg="#fff",bg="#211F45", font=("arial",30,"bold"),command=lambda: show("1")).place(x=10,y=400)
Button(home, text="2", height=1, width=5,bd=1,fg="#fff",bg="#211F45", font=("arial",30,"bold"),command=lambda: show("2")).place(x=150,y=400)
Button(home, text="3", height=1, width=5,bd=1,fg="#fff",bg="#211F45", font=("arial",30,"bold"),command=lambda: show("3")).place(x=290,y=400)
Button(home, text="0", height=1, width=11,bd=1,fg="#fff",bg="#211F45", font=("arial",30,"bold"),command=lambda: show("0")).place(x=10,y=500)

#sor 5
Button(home, text=".", height=1, width=5,bd=1,fg="#fff",bg="#130E5B", font=("arial",30,"bold"),command=lambda: show(".")).place(x=290,y=500)
Button(home, text="=", height=3, width=5,bd=1,fg="#fff",bg="#0A009B", font=("arial",30,"bold"),command=lambda: eredmeny()).place(x=430,y=400)


home.mainloop()