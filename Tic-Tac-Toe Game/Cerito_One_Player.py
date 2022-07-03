import random
import RGB
from tkinter import *
from tkinter import messagebox
from mis_librerias.Centrar_Ventana import centrar_ventana


class Cerito():
    
    def __init__(self):
       
       #Variables Globales
       self.turno = random.randint(0,1)#variable que determina el turno (si es X o O)inicia aleatoriamente
       self.asd = RGB
       self.turno_computadora:int
       self.rango_random = [1,2,3,4,5,6,7,8,9] #esta lista contiene el rango de numeros que puede seleccionar la computadora para presionar un boton
       
       if self.turno == 0:
           self.turno_computadora = 1
       if self.turno == 1:
           self.turno_computadora = 0
       
       self.raiz = Tk()
       self.raiz.resizable(0,0)
       self.raiz.title("Cerito")
       self.raiz.geometry(centrar_ventana(300,400,self.raiz))
       
       self.frame = Frame(self.raiz)
       self.frame.pack(fill="both",expand=True)
       
       self.imagen = PhotoImage(file= 'imagenes/raya_cruz.png')
       self.fondo = Label(self.frame,image=self.imagen)
       self.fondo.place(x= 35,y=100)
       
       self.label_turno = Label(self.frame,text="Turno:")
       self.label_turno.place(x=50,y=50)
       
       self.turno_x =Label(self.frame,text="X",fg="red")
       self.turno_x.place(x=100,y=50)
       
       self.turno_O =Label(self.frame,text="O",fg="red")
       self.turno_O.place(x=120,y=50)
       
       
       #estas variables guardaran la seleccion de cada boton (si lo que tiene es X o O)
       self.seleccion_boton1 = "1"
       self.seleccion_boton2 = "2"
       self.seleccion_boton3 = "3"
       self.seleccion_boton4 = "4"
       self.seleccion_boton5 = "5"
       self.seleccion_boton6 = "6"
       self.seleccion_boton7 = "7"
       self.seleccion_boton8 = "8"
       self.seleccion_boton9 = "9"
       
       #variables bandera para marcar si el boton ya fue presionado
       self.state_bot1 = False
       self.state_bot2 = False
       self.state_bot3 = False
       self.state_bot4 = False
       self.state_bot5 = False
       self.state_bot6 = False
       self.state_bot7 = False
       self.state_bot8 = False
       self.state_bot9 = False
       
       if self.turno == 0:
           self.turno_x.config(state=DISABLED)
       if self.turno == 1:
           self.turno_O.config(state=DISABLED)
           
       #enumeracion de los botones de izquierda a derecha para identificarlos 
       self.boton1 = Button(self.frame,command=self.Codigo_boton1,bg= "white")
       self.boton1.config(width=6,height=3)
       self.boton1.place(x=50,y=110)
       
       self.boton2 = Button(self.frame,command=self.Codigo_boton2,bg="white")
       self.boton2.config(width=6,height=3)
       self.boton2.place(x=125,y=110)
       
       self.boton3 = Button(self.frame,command=self.Codigo_boton3,bg="white")
       self.boton3.config(width=6,height=3)
       self.boton3.place(x=200,y=110)
       
       self.boton4 = Button(self.frame,command=self.Codigo_boton4,bg="white")
       self.boton4.config(width=6,height=3)
       self.boton4.place(x=50,y=185)
       
       self.boton5 = Button(self.frame,command=self.Codigo_boton5,bg="white")
       self.boton5.config(width=6,height=3)
       self.boton5.place(x=125,y=185)
       
       self.boton6 = Button(self.frame,command=self.Codigo_boton6,bg="white")
       self.boton6.config(width=6,height=3)
       self.boton6.place(x=200,y=185)
       
       self.boton7 = Button(self.frame,command=self.Codigo_boton7,bg="white")
       self.boton7.config(width=6,height=3)
       self.boton7.place(x=50,y=260)
       
       self.boton8 = Button(self.frame,command=self.Codigo_boton8,bg="white")
       self.boton8.config(width=6,height=3)
       self.boton8.place(x=125,y=260)
       
       self.boton9 = Button(self.frame,command=self.Codigo_boton9,bg="white")
       self.boton9.config(width=6,height=3)
       self.boton9.place(x=200,y=260)
       
       #boton para resetear la ventana
       image_reset = PhotoImage(file="imagenes/reset.png")
       boton_reset =Button(self.frame,image=image_reset,command=self.Codigo_boton_reset)
       boton_reset.config(width=30,height=30)
       boton_reset.place(x=210,y=30)
       
       self.raiz =mainloop()    
    
        #Evento de los botones
    """
    Al presionar cada boton :
    1-comprobamos el turno en que se encuentra (si es X o O) esto lo hacemos mediante la variable turno la cual inicia con el metodo random.
    2-dependiendo del turno en que se encuentre se le agrega el texto del simbolo del turno(X o O) al boton y se deshabilita para 
       que no pueda ser presionado nuevamente.
    3-cambiamos al turno del otro(mediante la variable turno)
    4-guardamos la seleccion del boton en la variable seleccion_boton.
    """      
    def Inteligencia_computadora(self):
         
        boton_a_presionar = random.choice(self.rango_random)
         
        if boton_a_presionar == 1 and self.state_bot1 == False:#si la variable boton_a_presionar vale 1 y el boton1 no ha sido presionado
           Cerito.Codigo_boton1(self)
           self.rango_random.remove(1)
        
        elif boton_a_presionar == 2 and self.state_bot2 == False:
            Cerito.Codigo_boton2(self)
            self.rango_random.remove(2)
        
        elif boton_a_presionar == 3 and self.state_bot3 == False:
            Cerito.Codigo_boton3(self)
            self.rango_random.remove(3)
        
        elif boton_a_presionar == 4 and self.state_bot4 == False:
             Cerito.Codigo_boton4(self)
             self.rango_random.remove(4)
        
        elif boton_a_presionar == 5 and self.state_bot5 == False:
             Cerito.Codigo_boton5(self)
             self.rango_random.remove(5)
        
        elif boton_a_presionar == 6 and self.state_bot6 == False:
             Cerito.Codigo_boton6(self)
             self.rango_random.remove(6)
        
        elif boton_a_presionar == 7 and self.state_bot7 == False:
             Cerito.Codigo_boton7(self) 
             self.rango_random.remove(7)    
        
        elif boton_a_presionar == 8 and self.state_bot8 == False:
             Cerito.Codigo_boton8(self)
             self.rango_random.remove(8)
        
        elif boton_a_presionar == 9 and self.state_bot9 == False:
             Cerito.Codigo_boton9(self)
             self.rango_random.remove(9) 
           
        else:
            pass  
                                   
                          
         
           
    def Codigo_boton1(self):
        if self.turno == 0:
            self.boton1.config(text="O",state=DISABLED)
            self.turno_O.config(state=DISABLED)
            self.turno_x.config(state=NORMAL)
            self.turno = 1
            self.seleccion_boton1 = "o"
        else:
            self.boton1.config(text="X",state=DISABLED)
            self.turno_x.config(state=DISABLED)
            self.turno_O.config(state=NORMAL)
            self.turno = 0
            self.seleccion_boton1 = "x"
        self.state_bot1 = True    
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
           Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton2(self):
        if self.turno == 0:
            self.boton2.config(text="O", state=DISABLED )
            self.turno_O.config(state=DISABLED)
            self.turno_x.config(state=NORMAL)
            self.turno = 1
            self.seleccion_boton2 = "o"
        else:
            self.boton2.config(text="X", state=DISABLED)
            self.turno_x.config(state=DISABLED)
            self.turno_O.config(state=NORMAL)
            self.turno = 0
            self.seleccion_boton2 = "x"
        self.state_bot2 = True    
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton3(self):
        if self.turno == 0:
            self.boton3.config(text="O", state=DISABLED )
            self.turno_O.config(state=DISABLED)
            self.turno_x.config(state=NORMAL)
            self.turno = 1
            self.seleccion_boton3 = "o"
        else:
            self.boton3.config(text="X", state=DISABLED)
            self.turno_x.config(state=DISABLED)
            self.turno_O.config(state=NORMAL)
            self.turno = 0
            self.seleccion_boton3 = "x"
        self.state_bot3 = True    
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton4(self):
        if self.turno == 0:
            self.boton4.config(text="O", state=DISABLED)
            self.turno_O.config(state=DISABLED)
            self.turno_x.config(state=NORMAL)
            self.turno = 1
            self.seleccion_boton4 = "o"
        else:
            self.boton4.config(text="X", state=DISABLED)
            self.turno_x.config(state=DISABLED)
            self.turno_O.config(state=NORMAL)
            self.turno = 0
            self.seleccion_boton4 = "x"
        self.state_bot4 = True    
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton5(self):
        if self.turno == 0:
            self.boton5.config(text="O", state=DISABLED)
            self.turno_O.config(state=DISABLED)
            self.turno_x.config(state=NORMAL)
            self.turno = 1
            self.seleccion_boton5 = "o"
        else:
            self.boton5.config(text="X", state=DISABLED)
            self.turno_x.config(state=DISABLED)
            self.turno_O.config(state=NORMAL)
            self.turno = 0
            self.seleccion_boton5 = "x"
        self.state_bot5 = True    
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton6(self):
        if self.turno == 0:
            self.boton6.config(text="O", state=DISABLED)
            self.turno_O.config(state=DISABLED)
            self.turno_x.config(state=NORMAL)
            self.turno = 1
            self.seleccion_boton6 = "o"
        else:
            self.boton6.config(text="X", state=DISABLED)
            self.turno_x.config(state=DISABLED)
            self.turno_O.config(state=NORMAL)
            self.turno = 0
            self.seleccion_boton6 = "x"
        self.state_bot6 = True    
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
        
    def Codigo_boton7(self):
        if self.turno == 0:
            self.boton7.config(text="O", state=DISABLED)
            self.turno_O.config(state=DISABLED)
            self.turno_x.config(state=NORMAL)
            self.turno = 1
            self.seleccion_boton7 = "o"
        else:
            self.boton7.config(text="X", state=DISABLED)
            self.turno_x.config(state=DISABLED)
            self.turno_O.config(state=NORMAL)
            self.turno = 0
            self.seleccion_boton7 = "x"
        self.state_bot7 = True   
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
        
    def Codigo_boton8(self):
        if self.turno == 0:
            self.boton8.config(text="O", state=DISABLED)
            self.turno_O.config(state=DISABLED)
            self.turno_x.config(state=NORMAL)
            self.turno = 1
            self.seleccion_boton8 = 'o'
        else:
            self.boton8.config(text="X", state=DISABLED)
            self.turno_x.config(state=DISABLED)
            self.turno_O.config(state=NORMAL)
            self.turno = 0
            self.seleccion_boton8 = "x"
        self.state_bot8 = True    
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton9(self):
        if self.turno == 0:
            self.boton9.config(text="O", state=DISABLED)
            self.turno_O.config(state=DISABLED)
            self.turno_x.config(state=NORMAL)
            self.turno = 1
            self.seleccion_boton9 = "o"
        else:
            self.boton9.config(text="X", state=DISABLED)
            self.turno_x.config(state=DISABLED)
            self.turno_O.config(state=NORMAL)
            self.turno = 0
            self.seleccion_boton9 = 'x'
        self.state_bot9 = True    
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
        
    def Codigo_boton_reset(self):
        
        #con este metodo reiniciamos a su estado original todos las variables y elementos del juego
        self.boton1.config(text="", state=NORMAL,bg="white")
        self.boton2.config(text="", state=NORMAL,bg="white")
        self.boton3.config(text="", state=NORMAL,bg="white")
        self.boton4.config(text="", state=NORMAL,bg="white")
        self.boton5.config(text="", state=NORMAL,bg="white")
        self.boton6.config(text="", state=NORMAL,bg="white")
        self.boton7.config(text="", state=NORMAL,bg="white")
        self.boton8.config(text="", state=NORMAL,bg="white")
        self.boton9.config(text="", state=NORMAL,bg="white")
        
        self.state_bot1 = False
        self.state_bot2 = False
        self.state_bot3 = False
        self.state_bot4 = False
        self.state_bot5 = False
        self.state_bot6 = False
        self.state_bot7 = False
        self.state_bot8 = False
        self.state_bot9 = False
    
        self.seleccion_boton1 = "1"
        self.seleccion_boton2 = "2"
        self.seleccion_boton3 = "3"
        self.seleccion_boton4 = "4"
        self.seleccion_boton5 = "5"
        self.seleccion_boton6 = "6"
        self.seleccion_boton7 = "7"
        self.seleccion_boton8 = "8"
        self.seleccion_boton9 = "9"
    
        self.turno = random.randint(0, 1)
    
        if self.turno == 0:
            self.turno_x.config(state=DISABLED)
            self.turno_O.config(state=NORMAL)
            self.turno_computadora = 1
        else:
            self.turno_O.config(state=DISABLED)
            self.turno_x.config(state=NORMAL)
            self.turno_computadora = 0
         
        self.rango_random = [1, 2, 3, 4, 5, 6, 7, 8, 9]    
    
    def Mensaje_Ganador(self, a):#metodo para mostrar un mensaje en pantalla con el ganador de la partida
        messagebox.showinfo("Ganador!","EL ganador es : " + a.upper() )
    
    def Mensaje_Empate(self):#metodo para mostrar un mensaje en pantalla si hubo empate
        messagebox.showinfo("Empate!","Empate" )
    
    def Ganador(self):
        
        """_summary_
           Con este metodo se comprueban las condiciones para dar un ganador mediante la variable seleccion_boton la cual contiene 
           en cada caso si tiene X o O.
           Cuando se encuentra una coincidencia ganadora se pintan de verde los botones que coinciden y el resto se deshabilita y se muestra 
           un mensaje con el ganador.
           """
        if self.seleccion_boton1 == self.seleccion_boton2 == self.seleccion_boton3:
           self.boton1.config(bg=self.asd.from_rgb((0, 80, 0)))
           self.boton2.config(bg=self.asd.from_rgb((0, 80, 0)))
           self.boton3.config(bg=self.asd.from_rgb((0, 80, 0)))
              # Deshabilito
           self.boton4.config(state=DISABLED)
           self.boton5.config(state=DISABLED)
           self.boton6.config(state=DISABLED)
           self.boton7.config(state=DISABLED)
           self.boton8.config(state=DISABLED)
           self.boton9.config(state=DISABLED)
           
           Cerito.Mensaje_Ganador(self, self.seleccion_boton1)
    
        elif self.seleccion_boton4 == self.seleccion_boton5 == self.seleccion_boton6:
            
            self.boton4.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton5.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton6.config(bg=self.asd.from_rgb((0, 80, 0)))
               #Deshabilito
            self.boton1.config(state=DISABLED)
            self.boton2.config(state=DISABLED)
            self.boton3.config(state=DISABLED)
            self.boton7.config(state=DISABLED)
            self.boton8.config(state=DISABLED)
            self.boton9.config(state=DISABLED)
    
            Cerito.Mensaje_Ganador(self, self.seleccion_boton4)
    
        elif self.seleccion_boton7 == self.seleccion_boton8 == self.seleccion_boton9:
            self.boton7.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton8.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton9.config(bg=self.asd.from_rgb((0, 80, 0)))
                 #Deshabilito
            self.boton1.config(state=DISABLED)
            self.boton2.config(state=DISABLED)
            self.boton3.config(state=DISABLED)
            self.boton4.config(state=DISABLED)
            self.boton5.config(state=DISABLED)
            self.boton6.config(state=DISABLED)
    
            Cerito.Mensaje_Ganador(self, self.seleccion_boton7)
    
        elif self.seleccion_boton1 == self.seleccion_boton4 == self.seleccion_boton7:
            
            self.boton1.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton4.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton7.config(bg=self.asd.from_rgb((0, 80, 0)))
                 #Deshabilito
            self.boton2.config(state=DISABLED)
            self.boton3.config(state=DISABLED)
            self.boton5.config(state=DISABLED)
            self.boton6.config(state=DISABLED)
            self.boton8.config(state=DISABLED)
            self.boton9.config(state=DISABLED)
    
            Cerito.Mensaje_Ganador(self, self.seleccion_boton1)
    
        elif self.seleccion_boton2 == self.seleccion_boton5 == self.seleccion_boton8:
            self.boton2.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton5.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton8.config(bg=self.asd.from_rgb((0, 80, 0)))
               #Deshabilito
            self.boton1.config(state=DISABLED)
            self.boton3.config(state=DISABLED)
            self.boton4.config(state=DISABLED)
            self.boton6.config(state=DISABLED)
            self.boton7.config(state=DISABLED)
            self.boton9.config(state=DISABLED)
    
            Cerito.Mensaje_Ganador(self, self.seleccion_boton2)
    
        elif self.seleccion_boton3 == self.seleccion_boton6 == self.seleccion_boton9:
            self.boton3.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton6.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton9.config(bg=self.asd.from_rgb((0, 80, 0)))
                #Deshabilito
            self.boton1.config(state=DISABLED)
            self.boton2.config(state=DISABLED)
            self.boton4.config(state=DISABLED)
            self.boton5.config(state=DISABLED)
            self.boton7.config(state=DISABLED)
            self.boton8.config(state=DISABLED)
    
            Cerito.Mensaje_Ganador(self, self.seleccion_boton3)
    
        elif self.seleccion_boton1 == self.seleccion_boton5 == self.seleccion_boton9:
            self.boton1.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton5.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton9.config(bg=self.asd.from_rgb((0, 80, 0)))
               #Deshabilito
            self.boton2.config(state=DISABLED)
            self.boton3.config(state=DISABLED)
            self.boton4.config(state=DISABLED)
            self.boton6.config(state=DISABLED)
            self.boton7.config(state=DISABLED)
            self.boton8.config(state=DISABLED)
    
            Cerito.Mensaje_Ganador(self, self.seleccion_boton1)
    
        elif self.seleccion_boton7 == self.seleccion_boton5 == self.seleccion_boton3:
            self.boton7.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton5.config(bg=self.asd.from_rgb((0, 80, 0)))
            self.boton3.config(bg=self.asd.from_rgb((0, 80, 0)))
               #Deshabilito
            self.boton1.config(state=DISABLED)
            self.boton2.config(state=DISABLED)
            self.boton4.config(state=DISABLED)
            self.boton6.config(state=DISABLED)
            self.boton8.config(state=DISABLED)
            self.boton9.config(state=DISABLED)
    
            Cerito.Mensaje_Ganador(self, self.seleccion_boton7)
            
        #comprobamos si todos fueron presionados y no se cumplieron las condiciones anteriores para dar un ganador entonces empate
        elif self.state_bot1 == self.state_bot2 == self.state_bot3 == self.state_bot4 == self.state_bot5 == self.state_bot6 == self.state_bot7 == self.state_bot8 == self.state_bot9 == True:
            Cerito.Mensaje_Empate(self)
            
            
    
    
    