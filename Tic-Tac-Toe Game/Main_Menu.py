from tkinter import *
from tkinter import messagebox
from RGB import from_rgb
import Cerito_Multiplayer
import Cerito_One_Player
from mis_librerias.Centrar_Ventana import centrar_ventana

def main():
    rgb = from_rgb
    width = 400
    height = 300
    root = Tk()
    root.geometry(centrar_ventana(width,height,root))
    
    frame = Frame()
    frame.config(bg = rgb((0,0,150)))
    frame.pack(fill = "both", expand = "True")
    
    label_titulo = Label(frame, text = "Menu")
    label_titulo.config(font=("Courier",18))
    label_titulo.place(x = (width/2) - 30, y = 30)
    
    seleccion1 = IntVar()
    seleccion2 = IntVar()
    
    def cambiar_estado_checkbutton1():
        seleccion2.set(0)
    def cambiar_estado_checkbutton2():
        seleccion1.set(0)        
    
    check1 = Checkbutton(frame, text = "Un Jugador", variable = seleccion1, command = cambiar_estado_checkbutton1)
    check1.config(width = "11")
    check1.place(x = "100", y = "150")
    
    check2 = Checkbutton(frame, text = "Dos Jugadores", variable = seleccion2, command = cambiar_estado_checkbutton2)
    check2.place(x = "100", y = "200")
        
    
    def codigo_boton():
        if seleccion1.get() == True:
            cerito = Cerito_One_Player
            root.destroy()
            cerito.Cerito()
            
        elif seleccion2.get() == True:
            cerito = Cerito_Multiplayer
            root.destroy()
            cerito.Cerito()
        else:
            messagebox.showinfo("Error","Debes seleccionar uno de los dos")
            
    
    button = Button(frame, text = "Aceptar",command = codigo_boton)
    button.config(width = "10", height = "5")
    button.place(x = "250", y = "150")   
    
    root.mainloop()
    
main()    