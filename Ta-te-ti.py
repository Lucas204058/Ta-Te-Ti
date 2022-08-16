import turtle
import tkinter
import random
import tkinter as tk
import tkinter as tk
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk

ventana = tkinter.Tk()
ventana.geometry("300x300")
tabla = []


def jugar():
    for k in range(3):
        tabla[k][k].config(bg='Blue')
        time.sleep(1)


for i in range(3):
    fila = []
    for j in range(3):
        boton = tkinter.Button(ventana, bg='Orange', command=jugar)
        boton.config(relief=tkinter.SUNKEN)
        boton.grid(column=i, row=j)
        fila.append(boton)
    tabla.append(fila)

app = tk.Tk()
  
buttonExample1 = tk.Button(app, text="Iniciar", width=4, height=4)
buttonExample2 = tk.Button(app,text="Salir", width=4, height=4)

buttonExample1.pack(side=tk.LEFT)
buttonExample2.pack(side=tk.RIGHT)

s = ttk.Style()
s.configure("TButton", foreground="#ff0000")
boton = ttk.Button(text="Iniciar")
boton.place(x=40, y=50)

app.mainloop()
