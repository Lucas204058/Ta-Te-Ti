import tkinter
from functools import partial
from tkinter import PhotoImage
from PIL import Image,ImageTk

class Tateti:
    def __init__(self):      
        #Tamaño de la tabla
        ventana = tkinter.Tk()
        ventana.title("Ventana")
        ventana.geometry("210x300")
        tabla_botones = []
        self.listadeframes = []
        #Para hacer la imagen
        self.turno = "O"
        img = Image.open('X.png')
        img = img.resize((50,60), Image.Resampling.LANCZOS)
        self.imga = ImageTk.PhotoImage(img)
        self.turno = "X"
        img1 = Image.open("O.png")
        img1 = img1.resize((50, 60), Image.Resampling.LANCZOS)
        self.img1a = ImageTk.PhotoImage(img1)
        self.tabla_botones = []
        self.x = True
        
        #Creando Frames
        for f in range(2):
            frame = tkinter.Frame(ventana, weidth=210, height=250)
            self.listadeframes.append(frame)
        #Creando tablero 
        for i in range(3):
            fila_botones = []    
            for j in range(3):
                b = tkinter.Button(frame[0],  command=partial(self.boton_apretado, i, j), height=4, width=5)
                b.grid(row=i, column=j)
                fila_botones.append(b)
            self.tabla_botones.append(fila_botones)
        print(self.tabla_botones)
        ventana.mainloop()
        
    #Para apretar los botones
    def boton_apretado(self, col, fila):
        if self.x:
            imagen = self.imga
            texto = "X"
            self.turno = "X"
        else:
            imagen = self.img1a
            texto = "O"
            self.turno = "O"
        self.tabla_botones[col][fila].config(text=texto, image=imagen, height=63, width=65)
        self.chequearGanador(self.tabla_botones)
        self.x = not self.x
        
    #Verifica el ganador    
    def chequearGanador(self, tabla_botones):
        if self.tabla_botones[0][0].cget("text") and self.tabla_botones[0][0].cget("text") == self.tabla_botones[0][1].cget("text") and self.tabla_botones[0][1].cget("text") == self.tabla_botones[0][2].cget("text"):
            print("gano " + self.turno)
        if self.tabla_botones[1][0].cget("text") and self.tabla_botones[1][0].cget("text") == self.tabla_botones[1][1].cget("text") and self.tabla_botones[1][1].cget("text") == self.tabla_botones[1][2].cget("text"):
            print("gano " + self.turno)
        if self.tabla_botones[2][0].cget("text") and self.tabla_botones[2][0].cget("text") == self.tabla_botones[2][1].cget("text") and self.tabla_botones[2][1].cget("text") == self.tabla_botones[2][2].cget("text"):
            print("gano " + self.turno)
        if self.tabla_botones[0][0].cget("text") and self.tabla_botones[0][0].cget("text") == self.tabla_botones[1][0].cget("text") and self.tabla_botones[1][0].cget("text") == self.tabla_botones[2][0].cget("text"):
            print("gano " + self.turno)
        if self.tabla_botones[0][1].cget("text") and self.tabla_botones[0][1].cget("text") == self.tabla_botones[1][1].cget("text") and self.tabla_botones[1][1].cget("text") == self.tabla_botones[2][1].cget("text"):
            print("gano " + self.turno)
        if self.tabla_botones[0][2].cget("text") and self.tabla_botones[0][2].cget("text") == self.tabla_botones[1][2].cget("text") and self.tabla_botones[1][2].cget("text") == self.tabla_botones[2][2].cget("text"):
            print("gano " + self.turno)
        if self.tabla_botones[0][0].cget("text") and self.tabla_botones[0][0].cget("text") == self.tabla_botones[1][1].cget("text") and self.tabla_botones[1][1].cget("text") == self.tabla_botones[2][2].cget("text"):
            print("gano " + self.turno)
        if self.tabla_botones[0][2].cget("text") and self.tabla_botones[0][2].cget("text") == self.tabla_botones[1][1].cget("text") and self.tabla_botones[1][1].cget("text") == self.tabla_botones[2][0].cget("text"):
            print("gano " + self.turno)
 
                       
ttt = Tateti()