from tkinter import *
from tkinter import messagebox as messageBox
from tkinter import ttk
from tkinter import colorchooser as colorChooser 
root=Tk()
root.geometry("500x300")

def COLOR():
    
    print("#"+c1.get()+c2.get()+c3.get())
    x=c1.get()+c2.get()+c3.get()
    if len(x)>6:
       B.config(text=f'Introdujiste mas de \n 6 digitos, revisa.')

    elif len(x)<6:
       B.config(text=f'Introdujiste menos de \n 6 digitos, revisa.')

        
    else:
     ventanaPrincipal.config(bg=("#"+c1.get()+c2.get()+c3.get()))


c1=StringVar()
c2=StringVar()
c3=StringVar()
ventanaPrincipal=Frame(root)
ventanaPrincipal.pack(fill="both", expand=1)

titulo=Label(ventanaPrincipal,text="CAMBIO DE COLORES",font=("Roboto",20))
titulo.grid(row=1,column=2,padx=5,pady=5)

RED=Label(ventanaPrincipal,text="RED",font=("Roboto",16))
RED.grid(row=5,column=1,padx=5,pady=5)
color1=Entry(ventanaPrincipal,textvariable=c1,font=("Roboto",13))
color1.grid(row=5,column=2,padx=5,pady=5)

GREEN=Label(ventanaPrincipal,text="GREEN",font=("Roboto",16))
GREEN.grid(row=9,column=1,padx=5,pady=5)
color2=Entry(ventanaPrincipal,textvariable=c2,font=("Roboto",13))
color2.grid(row=9,column=2,padx=5,pady=5)

BLUE=Label(ventanaPrincipal,text="BLUE",font=("Roboto",16))
BLUE.grid(row=13,column=1,padx=5,pady=5)
color3=Entry(ventanaPrincipal,textvariable=c3,font=("Roboto",13))
color3.grid(row=13,column=2,padx=5,pady=5)


Color=Button(ventanaPrincipal,text="CAMBIAR COLOR",font=("Roboto",15),command=COLOR)
Color.grid(row=17,column=2,padx=5,pady=5)

B = Label(ventanaPrincipal, text="", font=("Roboto",15))
B.grid(row=19, column=2, padx=10, pady=10)


root.mainloop()