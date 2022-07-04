import random
import RGB
from tkinter import *
from tkinter import messagebox
from mis_librerias.Centrar_Ventana import centrar_ventana


class Cerito():
    
    def __init__(self):
       
       self.turno = random.randint(0,1)#variable to determine the turn ("X" or "O"), start random
       self.asd = RGB
       self.turno_computadora = 5
       self.rango_random = [1,2,3,4,5,6,7,8,9] #this list contains the range of numbers that the computer can take to press a button 
       
       #the computer will take the opposite turn of the get with the random method
       if self.turno == 0:
           self.turno_computadora = 1
       else:
           self.turno_computadora = 0
       
       
       self.raiz = Tk()
       self.raiz.resizable(0,0)
       self.raiz.title("Cerito")
       self.raiz.geometry(centrar_ventana(300,400,self.raiz))
       
       self.frame = Frame(self.raiz)
       self.frame.config(bg = self.asd.from_rgb((84,146,203)))
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
       
       
       #this variable save the selection of each button("X" or "O")
       self.seleccion_boton1 = "1"
       self.seleccion_boton2 = "2"
       self.seleccion_boton3 = "3"
       self.seleccion_boton4 = "4"
       self.seleccion_boton5 = "5"
       self.seleccion_boton6 = "6"
       self.seleccion_boton7 = "7"
       self.seleccion_boton8 = "8"
       self.seleccion_boton9 = "9"
       
       #flag variable to know if the button was pressed or not
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
           
       """
       The numbers of the buttons 1 2 3 
                                  4 5 6 
                                  7 8 9  
       """ 
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
       
       self.botones = [self.boton1, self.boton2, self.boton3, self.boton4, self.boton5, self.boton6, self.boton7, self.boton8, self.boton9]
       
       #button to reset the window
       image_reset = PhotoImage(file="imagenes/reset.png")
       boton_reset =Button(self.frame,image=image_reset,command=self.Codigo_boton_reset)
       boton_reset.config(width=30,height=30)
       boton_reset.place(x=210,y=30)
       
       self.raiz =mainloop()    
    
    #the computer select a random button between 1 and 9 and press the button calling his function
    def Inteligencia_computadora(self):
         
        boton_a_presionar = random.choice(self.rango_random)
         
        if boton_a_presionar == 1 and self.state_bot1 == False:#if the value of the variable boton_a_presionar is 1 and the button is not pressed
           Cerito.Codigo_boton1(self)
        
        elif boton_a_presionar == 2 and self.state_bot2 == False:
            Cerito.Codigo_boton2(self)
        
        elif boton_a_presionar == 3 and self.state_bot3 == False:
            Cerito.Codigo_boton3(self)
        
        elif boton_a_presionar == 4 and self.state_bot4 == False:
             Cerito.Codigo_boton4(self)
        
        elif boton_a_presionar == 5 and self.state_bot5 == False:
             Cerito.Codigo_boton5(self)
        
        elif boton_a_presionar == 6 and self.state_bot6 == False:
             Cerito.Codigo_boton6(self)
        
        elif boton_a_presionar == 7 and self.state_bot7 == False:
             Cerito.Codigo_boton7(self) 
        
        elif boton_a_presionar == 8 and self.state_bot8 == False:
             Cerito.Codigo_boton8(self)
        
        elif boton_a_presionar == 9 and self.state_bot9 == False:
             Cerito.Codigo_boton9(self)
           
        else:
            pass  
                                                          
    #Functions of buttons
    """
    To press each button :
    1-depending of wath tun is on, we add the simbol(X o O) to the button and turn off him to can't press again . 
    2-change the turn
    """                   
    def Codigo_boton1(self):
        if self.state_bot1 == False:#if the button was not pressed
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
        self.state_bot1 = True #set True to know that the button was pressed
        self.rango_random.remove(1)#take off the button of the range that the computer can choice    
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
           Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton2(self):
        if self.state_bot2 == False:
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
        self.rango_random.remove(2)    
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton3(self):
        if self.state_bot3 == False:
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
        self.rango_random.remove(3)   
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton4(self):
        if self.state_bot4 == False:
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
        self.rango_random.remove(4)  
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton5(self):
        if self.state_bot5 == False:
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
        self.rango_random.remove(5)  
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton6(self):
        if self.state_bot6 == False:
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
        self.rango_random.remove(6)  
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
        
    def Codigo_boton7(self):
        if self.state_bot7 == False:
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
        self.rango_random.remove(7)
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
        
    def Codigo_boton8(self):
        if self.state_bot8 == False:
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
        self.rango_random.remove(8)  
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
    
    def Codigo_boton9(self):
        if self.state_bot9 == False:
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
        self.rango_random.remove(9)    
        Cerito.Ganador(self)
        if self.turno == self.turno_computadora:
            Cerito.Inteligencia_computadora(self)
     
    #whit this method reset all the components to the original state   
    def Codigo_boton_reset(self):
        for boton in self.botones:
            boton.config(text="", state=NORMAL,bg="white")
        
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
    
    def Mensaje_Ganador(self, a):#show the winner
        messagebox.showinfo("Ganador!","EL ganador es : " + a.upper() )
    
    def Mensaje_Empate(self):
        messagebox.showinfo("Empate!","Empate" )
    
    def Ganador(self):
        
        """_summary_
           *with this method check the conditions to give a winner through the variable seleccion_boton who contain  X o O.
           *when we found a winner coincidence turn on green the buttons and turn off the others and show the winner message
           """
        if self.seleccion_boton1 == self.seleccion_boton2 == self.seleccion_boton3:
           self.boton1.config(bg=self.asd.from_rgb((0, 80, 0)))
           self.boton2.config(bg=self.asd.from_rgb((0, 80, 0)))
           self.boton3.config(bg=self.asd.from_rgb((0, 80, 0)))
              # turn off
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
               #turn off
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
                 #turn off
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
                 #turn off
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
               #turn off
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
                #turn off
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
               #turn off
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
               #turn off
            self.boton1.config(state=DISABLED)
            self.boton2.config(state=DISABLED)
            self.boton4.config(state=DISABLED)
            self.boton6.config(state=DISABLED)
            self.boton8.config(state=DISABLED)
            self.boton9.config(state=DISABLED)
    
            Cerito.Mensaje_Ganador(self, self.seleccion_boton7)
            
        #if all the buttons was pressed and there is not winner coincidence 
        elif self.state_bot1 == self.state_bot2 == self.state_bot3 == self.state_bot4 == self.state_bot5 == self.state_bot6 == self.state_bot7 == self.state_bot8 == self.state_bot9 == True:
            Cerito.Mensaje_Empate(self)
            
            
    
    
    