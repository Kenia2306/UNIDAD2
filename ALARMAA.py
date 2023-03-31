
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
import time 
import pygame,sys
from pygame.locals import*
from tkinter import filedialog
pygame.init() 


root=Tk()
root.title("Alarma")
root.geometry("500x380")
ventanaprincipal=Frame(root,width=1000,height=1000,bg="pink")
ventanaprincipal.grid()

def clock():
    HoraDeReloj=time.strftime("%H")
    MinutosDeReloj=time.strftime("%M")
    SegundosDeReloj=time.strftime("%S")
    Tiempo=time.strftime(HoraDeReloj+":"+MinutosDeReloj+":"+SegundosDeReloj)
    Labelreloj.config(text=Tiempo)
    Labelreloj.after(1000,clock)
   
    if(HoraDeReloj==entryhoras.get()):
        if(MinutosDeReloj==EntryMinutos.get()):
            if(SegundosDeReloj=="00"):
                pygame.mixer.music.play()
                respuesta=MessageBox.askquestion("AskQuestion","Desea pausar la alarma?")
                if(respuesta=="yes"):
                    pygame.mixer.music.stop()
def alarmapotente():
    MessageBox.showwarning("ShowWarning","Alarma establecida")
def mostraralarma():
     MessageBox.showwarning("ShowWarning",entryhoras.get()+":"+EntryMinutos.get())
def mostrarmusica():
    cancion=filedialog.askopenfilename()
    pygame.mixer.music.load(cancion)


LabelTitulo=Label(ventanaprincipal,text="ALARMA",font=("Times",18,"bold"),background="pink",foreground="black", width=8,height=2, justify=CENTER,)
LabelTitulo.place(x=180,y=1)

LabelHora=Label(ventanaprincipal, text="HORA: ", font=("Times",14,"bold"),background="pink",foreground="black", width=8,height=2, justify=CENTER,)
LabelHora.place(x=20,y=100)

LabelMinutos=Label(ventanaprincipal,text="MINUTOS: ", font=("Times",14,"bold"), background="pink", width=8, height=2,  justify=CENTER,)
LabelMinutos.place(x=20,y=200)

LabelReloj=Label(ventanaprincipal, text="RELOJ", font=("Times",14,"bold"),background="pink",foreground="black", width=8,height=2, justify=CENTER,)
LabelReloj.place(x=60,y=50)

entryhoras=StringVar()
entradahoras=Entry(ventanaprincipal,font=("Times",12),textvariable=entryhoras).place(x=160,y=110)

EntryMinutos=StringVar()
EntradaMinutos=Entry(ventanaprincipal,font=("Times",12),textvariable=EntryMinutos).place(x=160,y=210)
Labelreloj=Label(ventanaprincipal,font=("Times",14,"bold"),background="pink",foreground="black", width=8,height=2, justify=CENTER,)
Labelreloj.place(x=170,y=50)

ButtonSetAlarma=Button(ventanaprincipal,font=("Times",14,"bold"),text="Poner Alarma",command=alarmapotente).place(x=10,y=300)
Buttonvalor=Button(ventanaprincipal,font=("Times",14,"bold"),text="Valor de alarma",command=mostraralarma).place(x=155,y=300)
ButtonMusica=Button(ventanaprincipal,font=("Times",14,"bold"),text="Seleccionar Musica",command=mostrarmusica).place(x=315,y=300)

clock()
root.mainloop()