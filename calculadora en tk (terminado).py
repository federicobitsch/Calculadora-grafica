from platform import python_compiler
from tkinter import *
from tkinter import messagebox
interfaz =Tk()

def cambio():
    precioAux=precio.get() #Estoy llamando la funcion PRECIO
    pagoAux=pago.get() #estoy llamando la funcion Pago
    cambioAux=pagoAux-precioAux
    faltanteAux=precioAux-pagoAux


    if cambioAux <0:
        messagebox.showinfo(title="DINERO INSUFICIENTE",message="Falta dinero en el pago, El Dinero faltante es de $ " + str(float(faltanteAux)))
    elif cambioAux ==0:
        messagebox.showinfo(title="PAGO SIN CAMBIO",message="Se ha pagado exacto, *NO es necesario dar cambio* ")
    elif cambioAux >0:
        messagebox.showinfo(title="SU VUELTO  " ,message='Su vuelto es de $' + str(float(cambioAux)))


interfaz.geometry("500x300+100+100")
interfaz.title("$$ Primer proyecto de cambio $$") #TITULO
lbltitle=Label(text="***¿CUANTO CAMBIO DAR EN UNA COMPRA?***",font=("AR CENA", 14)).pack()

lblIngrese=Label(text="Ingrese el precio del articulo: ",font=("Agency FB",16)).place(x=10,y=45)
precio = DoubleVar()
txtIngrese=Entry(interfaz,textvariable=precio).place(x=270,y=48)

lblPago=Label(text="¿Cuanto ha pagado el cliente?: ",font=("Agency FB",16)).place(x=10,y=75)
pago=DoubleVar()
txtPago=Entry(interfaz,textvariable=pago).place(x=270,y=78)

botonResultado=Button(interfaz,text="Calcular",command=cambio,font=("Arial",16)).place(x=10,y=110) 


interfaz.mainloop()
