from tkinter import *
import math

geome=Tk()
geome.title("Emergency Calculator")
geome.geometry("570x400+100+200")
geome.resizable(False,False)
geome.configure(bg="#ffffff")

def korkeplet():
    try:
        korT = math.pi*int(korsugar.get())**2
        korK = 2*math.pi*int(korsugar.get())
        korterulet.config(text="Kör területe: " + str(round(korT,2)))
        korkerulet.config(text="Kör kerülete: " + str(round(korK,2)))
    except ValueError:
        korterulet.config(text="")

def haromkeplet():
    try:
        trA = int(haromA.get())
        trB = int(haromB.get())
        trC = int(haromC.get())
        sqA = trA*trA
        sqB = trB*trB
        sqC = trC*trC
        corner = math.acos((sqA + sqB - sqC) / (2 * trA * trB))
        magasA = trB * math.sin(corner)
        haromT = (magasA*trA) /2
        haromK = trA + trB + trC
        haromterulet.config(text="Háromszög Területe: " + str(round(haromT,2)))
        haromkerulet.config(text="Háromszög Kerülete: " + str(round(haromK,2)))
    except ValueError:
        haromterulet.config(text="")

def negyzetkeplet():
    try:
        squareT = int(squareA.get()) * int(squareA.get())
        squareK = 4 * int(squareA.get())
        squareterulet.config(text="A négyzet területe: "+ str(round(squareT,2)))
        squarekerulet.config(text="A négyzet kerülete: " + str(round(squareK, 2)))
    except ValueError:
        squareterulet.config(text="")

def teglalapkeplet():
    try:
        rectT = int(recA.get()) * int(recB.get())
        rectK = 2 * (int(recA.get()) + int(recB.get()))
        recterulet.config(text="A téglalap területe: "+ str(round(rectT,2)))
        reckerulet.config(text="A téglalap kerülete: " + str(round(rectK, 2)))
    except ValueError:
        squareterulet.config(text="")

#Kör section
kortitle= Label(geome,text="Kör",font=("arial",15,"bold"),bg="#ffffff",fg="#000")
kortitle.place(x=0,y=0)
korintro= Label(geome,text="Sugár: ",font=("arial",0),bg="#ffffff",fg="#000000")
korintro.place(x=0,y=30)
korsugar = Entry(geome, width=5, font=("Arial",12),bg="#eeeeee",fg="#000")
korsugar.place(x=100,y=32)
korterulet = Label(geome,text="",width=30, font=("Arial",12,"bold"),bg="#ffffff",fg="#000")
korterulet.place(x=250,y=10)
korkerulet = Label(geome,text="",width=30, font=("Arial",12,"bold"),bg="#ffffff",fg="#000")
korkerulet.place(x=250,y=35)
button1 = Button(geome, text="Számolj", height=1, width=7,fg="#fff",bg="#530083", font=("arial",10),command=korkeplet)
button1.place(x=160,y=30)
#Háromszög section
haromtitle= Label(geome,text="Háromszög",font=("arial",15,"bold"),bg="#ffffff",fg="#000")
haromtitle.place(x=0,y=100)
haromterulet = Label(geome,text="",width=30, font=("Arial",12,"bold"),bg="#ffffff",fg="#000")
haromterulet.place(x=250,y=110)
haromkerulet = Label(geome,text="",width=30, font=("Arial",12,"bold"),bg="#ffffff",fg="#000")
haromkerulet.place(x=250,y=135)
haromMagas= Label(geome,text="Oldalak:",font=("arial",10),bg="#ffffff",fg="#000")
haromMagas.place(x=0,y=130)
haromtitle= Label(geome,text="Háromszög",font=("arial",15,"bold"),bg="#ffffff",fg="#000")
haromtitle.place(x=0,y=100)
haromA = Entry(geome, width=3, font=("Arial",12),bg="#eeeeee",fg="#000")
haromA.place(x=50,y=130)
haromB = Entry(geome, width=3, font=("Arial",12),bg="#eeeeee",fg="#000")
haromB.place(x=85,y=130)
haromC = Entry(geome, width=3, font=("Arial",12),bg="#eeeeee",fg="#000")
haromC.place(x=120,y=130)

button2 = Button(geome, text="Számolj", height=1, width=7,fg="#fff",bg="#530083", font=("arial",10),command=haromkeplet)
button2.place(x=160,y=130)
#Négyzet section
squaretitle= Label(geome,text="Négyzet",font=("arial",15,"bold"),bg="#ffffff",fg="#000")
squaretitle.place(x=0,y=200)
squareintro= Label(geome,text="Oldal: ",font=("arial",0),bg="#ffffff",fg="#000000")
squareintro.place(x=0,y=230)
squareA = Entry(geome, width=5, font=("Arial",12),bg="#eeeeee",fg="#000")
squareA.place(x=50,y=232)
squareterulet = Label(geome,text="",width=30, font=("Arial",12,"bold"),bg="#ffffff",fg="#000")
squareterulet.place(x=250,y=210)
squarekerulet = Label(geome,text="",width=30, font=("Arial",12,"bold"),bg="#ffffff",fg="#000")
squarekerulet.place(x=250,y=235)
button3 = Button(geome, text="Számolj", height=1, width=7,fg="#fff",bg="#530083", font=("arial",10),command=negyzetkeplet)
button3.place(x=160,y=230)
#Téglalap section
rectitle= Label(geome,text="Téglalap",font=("arial",15,"bold"),bg="#ffffff",fg="#000")
rectitle.place(x=0,y=300)
recintro= Label(geome,text="Oldalak: ",font=("arial",0),bg="#ffffff",fg="#000000")
recintro.place(x=0,y=330)
recA = Entry(geome, width=3, font=("Arial",12),bg="#eeeeee",fg="#000")
recA.place(x=60,y=332)
recB = Entry(geome, width=3, font=("Arial",12),bg="#eeeeee",fg="#000")
recB.place(x=95,y=332)
recterulet = Label(geome,text="",width=30, font=("Arial",12,"bold"),bg="#ffffff",fg="#000")
recterulet.place(x=250,y=310)
reckerulet = Label(geome,text="",width=30, font=("Arial",12,"bold"),bg="#ffffff",fg="#000")
reckerulet.place(x=250,y=335)
button4 = Button(geome, text="Számolj", height=1, width=7,fg="#fff",bg="#530083", font=("arial",10),command=teglalapkeplet)
button4.place(x=160,y=330)

geome.mainloop()