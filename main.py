import tkinter
from tkinter import *
import subprocess

menu=tkinter.Tk()
menu.title("Calculator Menu")
menu.geometry("400x210+100+200")
menu.resizable(False,False)
menu.configure(bg="#000014")

def open1():
    subprocess.call(["python", "basiccalc.py"])

def open2():
    subprocess.call(["python", "subnet.py"])

def open3():
    subprocess.call(["python", "geometry.py"])

def info1():
    szoveg = Toplevel(menu)
    szoveg.title("Basic Calculator Leírás")
    Label(szoveg, text="""Basic Calculator, képes alap matematikai feladatok (összeadás, kivonás, osztás, szorzás) elvégzéséhez
    """, font=("arial",10,"bold"), fg="#fff",bg="#000").pack()

def info2():
        szoveg = Toplevel(menu)
        szoveg.title("Subnet Calculator Leírás")
        Label(szoveg, text="""Subnet Calculator, képes cím alapján kiszámolni hálózat subnet címét, és hostok számát
        """, font=("arial", 10,"bold"), fg="#fff",bg="#000").pack()

def info3():
        szoveg = Toplevel(menu)
        szoveg.title("Geometry Calculator Leírás")
        Label(szoveg, text="""Geometry Calculator, 2d tárgyak területét és kerületét számolja ki
        """, font=("arial", 10,"bold"), fg="#fff",bg="#000").pack()




Button(menu, text="Basic Calculator", height=1, width=18,bd=1,fg="#000",bg="#00EAFF", font=("arial",20,"bold"),command=open1).place(x=10,y=10)
Button(menu, text="i", height=1, width=3,bd=1,fg="#000",bg="#ffffff", font=("arial",20,"bold"),command=info1).place(x=330,y=10)

Button(menu, text="Subnet Calculator", height=1, width=18,bd=1,fg="#000",bg="#00EAFF", font=("arial",20,"bold"),command=open2).place(x=10,y=80)
Button(menu, text="i", height=1, width=3,bd=1,fg="#000",bg="#ffffff", font=("arial",20,"bold"),command=info2).place(x=330,y=80)

Button(menu, text="Geometry Calculator", height=1, width=18,bd=1,fg="#000",bg="#00EAFF", font=("arial",20,"bold"),command=open3).place(x=10,y=150)
Button(menu, text="i", height=1, width=3,bd=1,fg="#000",bg="#ffffff", font=("arial",20,"bold"),command=info3).place(x=330,y=150)


menu.mainloop()