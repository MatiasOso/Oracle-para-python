#Para un usuario, crea un formulario que pida 
#nombre, apellido, edad, sexo, correo, contraseña, username, hobbies.
#Al presionar el botón, almacena los datos en un diccionario, y posteriormente, genera la consulta 
#para insertar los datos en una tabla de una base de datos.

import tkinter


def mifuncion():
    print(caja.get())

ventana = tkinter.Tk()
ventana.title("Puntajes_mo")
ventana.geometry("500x500")

nombre = tkinter.Label(ventana, text="Ingrese su nombre:")
nombre.grid(column=0, row=0)
caja = tkinter.Entry(ventana)
caja.grid(column=1, row=0)

apellido = tkinter.Label(ventana, text="Ingrese su apellido:")
apellido.grid(column=0, row=1)
caja2 = tkinter.Entry(ventana)
caja2.grid(column=1, row=1)

edad= tkinter.Label(ventana, text="Ingrese su edad:")
edad.grid(column=0, row=2)
caja3 = tkinter.Entry(ventana)
caja3.grid(column=1, row=2)

sexo= tkinter.Label(ventana, text="Ingrese su sexo:")
radio=tkinter.Radiobutton(ventana, text="Masculino", value=1)
radio.grid(column=0, row=3)
radio2=tkinter.Radiobutton(ventana, text="Femenino", value=2)
radio2.grid(column=1, row=3)

correo= tkinter.Label(ventana, text="Ingrese su correo:")
correo.grid(column=0, row=4)
caja4 = tkinter.Entry(ventana)
caja4.grid(column=1, row=4)

"""
aceptar = tkinter.Button(ventana, text="Aceptar", command=mifuncion)
aceptar.grid(column=2, row=0)
radio = tkinter.Radiobutton(ventana, text="Opcion 1")
radio.grid(column=3, row=3)
check = tkinter.Checkbutton(ventana, text="Opcion 2")
check.grid(column=3, row=3)
listas = tkinter.Listbox(ventana)
listas.insert(1, "Opcion 1")
listas.insert(2, "Opcion 2")
texto = tkinter.Text(ventana, height=10, width=30)
texto.insert(tkinter.END, "Hola Mundo")
texto.grid(column=0, row=2)"""
ventana.mainloop()

#DEFINIR PARA GUARDAR EN ORACLE