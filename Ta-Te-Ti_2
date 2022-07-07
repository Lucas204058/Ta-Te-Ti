import turtle
import tkinter
import time
import random

posponer = 0.1

ventana = tkinter.Tk()
ventana.geometry("200x253")
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
        boton = tkinter.Button(ventana, height = 5, width = 5)
        boton.grid(column=i, row=j)
#         boton = tkinter.Button(ventana, height = 50, width = 50)
        fila.append(boton)
    tabla.append(fila)
    

    

ventana.mainloop()
