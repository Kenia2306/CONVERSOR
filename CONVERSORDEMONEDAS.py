from tkinter import*
from PIL import ImageTk,Image


root=Tk()
root.title("CONVERSOR")
root.geometry("500x500")
ventanaPrincipal=Frame(root,width=1000,height=1000,bg="pink")
ventanaPrincipal.grid()


def ConversorDeMoneda():

        if (Moneda1.get()=="USD"):
            if(Moneda2.get()=="MXN"):
                R1=Numero1.get()*18.4935
                
                pass
        if (Moneda1.get()=="USD"):
            if(Moneda2.get()=="ARG"):
                R1=Numero1.get()*200.74
                
                pass
        pass
        if (Moneda1.get()=="MXN"):
            if(Moneda2.get()=="USD"):
                R1=Numero1.get()*0.0541
                
                pass
        pass

        if (Moneda1.get()=="MXN"):
            if(Moneda2.get()=="ARG"):
                R1=Numero1.get()*10.8537
                
                pass
        pass

        if (Moneda1.get()=="ARG"):
            if(Moneda2.get()=="USD"):
                R1=Numero1.get()*0.005
                
                pass
        pass

        if (Moneda1.get()=="ARG"):
            if(Moneda2.get()=="MXN"):
                R1=Numero1.get()*0.0921
                
                pass
        pass
        return SPR1.set(R1)
        pass

Titulo=Label(ventanaPrincipal,text="Convertidor de Monedas",font=("Times",20,"bold"),background="pink",foreground="black", width=18,height=2,justify=CENTER,).place(x=120,y=1)

NumeroA=Label(ventanaPrincipal,text="Numero A:",font=("Times",16,"bold"),background="pink",foreground="black", width=8,height=2,justify=CENTER ).place(x=1,y=108)

Numero1=IntVar()

textNumeroA=Entry(ventanaPrincipal,font=("Times",12),textvariable=Numero1).place(x=160,y=119)

Moneda1=StringVar()
Moneda1.set("Moneda")
drop=OptionMenu(root,Moneda1,"USD","MXN","ARG").place(x=80,y=200)


Moneda2=StringVar()
Moneda2.set("Moneda")
drop=OptionMenu(root,Moneda2,"USD","MXN","ARG").place(x=280,y=200)

ResltadoMoneda=Label(ventanaPrincipal,text="Resultado: ",font=("Times",16,"bold"),background="pink",foreground="black",width=8,height=2, justify=CENTER,).place(x=1,y=370)

SPR1=StringVar()


Resultadofinal=Label(ventanaPrincipal,textvariable=SPR1,font=("Times",14,"bold"),background="pink",foreground="black", width=19,height=4, justify=CENTER,).place(x=150,y=350)


ButtonRegistrar=Button(ventanaPrincipal,font=("Times",14,"bold"),text="REGISTRAR",command=ConversorDeMoneda).place(x=160,y=300)

root.mainloop()