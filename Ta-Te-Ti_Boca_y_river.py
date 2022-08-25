import tkinter
from functools import partial
from tkinter import PhotoImage
from PIL import Image,ImageTk

ventana = tkinter.Tk()
ventana.geometry("210x250")
tabla_botones = []
turno = "river"
turno = "boca"

img = Image.open('river.png')
img = img.resize((50,60), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)

img1 = Image.open("boca.png")
img1 = img1.resize((50, 60), Image.Resampling.LANCZOS)
img1 = ImageTk.PhotoImage(img1)

def boton_apretado(col, fila):
    global x
    if x:
        imagen = img
        texto = "river"
    else:
        imagen = img1
        texto = "boca"
    tabla_botones[col][fila].config(text=texto, image=imagen, height=63, width=65)
    chequearGanador(tabla_botones)
    x = not x

tabla_botones =[]
x = True
    
def chequearGanador(tabla_botones):
    if tabla_botones[0][0].cget("text") and tabla_botones[0][0].cget("text") == tabla_botones[0][1].cget("text") and tabla_botones[0][1].cget("text") == tabla_botones[0][2].cget("text"):
        print("gano " + turno)
    if tabla_botones[1][0].cget("text") and tabla_botones[1][0].cget("text") == tabla_botones[1][1].cget("text") and tabla_botones[1][1].cget("text") == tabla_botones[1][2].cget("text"):
        print("gano " + turno)
    if tabla_botones[2][0].cget("text") and tabla_botones[2][0].cget("text") == tabla_botones[2][1].cget("text") and tabla_botones[2][1].cget("text") == tabla_botones[2][2].cget("text"):
        print("gano " + turno)
    if tabla_botones[0][0].cget("text") and tabla_botones[0][0].cget("text") == tabla_botones[1][0].cget("text") and tabla_botones[1][0].cget("text") == tabla_botones[2][0].cget("text"):
        print("gano " + turno)
    if tabla_botones[0][1].cget("text") and tabla_botones[0][1].cget("text") == tabla_botones[1][1].cget("text") and tabla_botones[1][1].cget("text") == tabla_botones[2][1].cget("text"):
        print("gano " + turno)
    if tabla_botones[0][2].cget("text") and tabla_botones[0][2].cget("text") == tabla_botones[1][2].cget("text") and tabla_botones[1][2].cget("text") == tabla_botones[2][2].cget("text"):
        print("gano " + turno)
    if tabla_botones[0][0].cget("text") and tabla_botones[0][0].cget("text") == tabla_botones[1][1].cget("text") and tabla_botones[1][1].cget("text") == tabla_botones[2][2].cget("text"):
        print("gano " + turno)
    if tabla_botones[0][2].cget("text") and tabla_botones[0][2].cget("text") == tabla_botones[1][1].cget("text") and tabla_botones[1][1].cget("text") == tabla_botones[2][0].cget("text"):
        print("gano " + turno)
                    
for i in range(3):
    fila_botones = []    
    for j in range(3):
        b = tkinter.Button(ventana,  command=partial(boton_apretado, i, j), height=4, width=5)
        b.grid(row=i, column=j)
        fila_botones.append(b)
    tabla_botones.append(fila_botones)
    
print(tabla_botones)
ventana.mainloop()
