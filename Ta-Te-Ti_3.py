import tkinter
from functools import partial

ventana = tkinter.Tk()
ventana.geometry("210x250")
tablero = []

turno = "x"

def chequearGanador(tablero):
    if tablero[0][0].cget("text") and tablero[0][0].cget("text") == tablero[0][1].cget("text") and tablero[0][1].cget("text") == tablero[0][2].cget("text"):
        print("gano " + turno)
    if tablero[1][0].cget("text") and tablero[1][0].cget("text") == tablero[1][1].cget("text") and tablero[1][1].cget("text") == tablero[1][2].cget("text"):
        print("gano " + turno)
    if tablero[2][0].cget("text") and tablero[2][0].cget("text") == tablero[2][1].cget("text") and tablero[2][1].cget("text") == tablero[2][2].cget("text"):
        print("gano " + turno)
    if tablero[0][0].cget("text") and tablero[0][0].cget("text") == tablero[1][0].cget("text") and tablero[1][0].cget("text") == tablero[2][0].cget("text"):
        print("gano " + turno)
    if tablero[0][1].cget("text") and tablero[0][1].cget("text") == tablero[1][1].cget("text") and tablero[1][1].cget("text") == tablero[2][1].cget("text"):
        print("gano " + turno)
    if tablero[0][2].cget("text") and tablero[0][2].cget("text") == tablero[1][2].cget("text") and tablero[1][2].cget("text") == tablero[2][2].cget("text"):
        print("gano " + turno)
    if tablero[0][0].cget("text") and tablero[0][0].cget("text") == tablero[1][1].cget("text") and tablero[1][1].cget("text") == tablero[2][2].cget("text"):
        print("gano " + turno)
    if tablero[0][2].cget("text") and tablero[0][2].cget("text") == tablero[1][1].cget("text") and tablero[1][1].cget("text") == tablero[2][0].cget("text"):
        print("gano " + turno)
        
def apretar(i, j):
    global turno
    if not tablero[i][j].cget("text"):
        if turno == "x":
            tablero[i][j].config(text="x", relief=tkinter.SUNKEN)
            chequearGanador(tablero)
            turno = "o"
        else:
            tablero[i][j].config(text="o", relief=tkinter.SUNKEN)
            chequearGanador(tablero)
            turno = "x"
        
for i in range(3):
    lista = []
    for j in range(3):
        boton = tkinter.Button(ventana, height = 5, width = 5, text="", command=partial(apretar, i,j))
        boton.grid(column=j, row=i)
        lista.append(boton)
    tablero.append(lista)

ventana.mainloop()