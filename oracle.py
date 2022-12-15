import cx_Oracle
import os
import tkinter as tk
from tkinter import ttk

os.environ['TNS_ADMIN']='C:/Users/Usuario/Desktop/Oracle/wallet' 
connection=cx_Oracle.connect('ADMIN','TI2002-sec-213','db20220606233104_high')
cursor=connection.cursor()
"""for result in cursor.execute('select * from MSF'):
    print("Usuario "+ result[1]+ " Puntaje "+ str(result[2]))"""

Administrador = False
class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.__create_widgets()

    def __create_widgets(self):
        # Username
        ttk.Label(self, text='Acceder').grid(column=0, row=0, sticky=tk.W)
        self.cajaUsername = ttk.Entry(self, width=30)
        self.cajaUsername.focus()
        self.cajaUsername.grid(column=1, row=0, sticky=tk.W)

        # Password:
        self.cajaPassword = ttk.Label(self, text='Password').grid(column=0, row=1, sticky=tk.W)
        self.cajaPassword = ttk.Entry(self, width=30, show='*')
        self.cajaPassword.grid(column=1, row=1, sticky=tk.W)
        #boton = ttk.Button(text="Acceder", command=lambda: self.ValidarUsuario())#self.cajaUsername.get(), self.cajaPassword.get()))
        boton = ttk.Button(text="Acceder", command=lambda: self.ValidarUsuario())
        boton.grid(row=3,column=1)
        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)
    def ValidarUsuario(self):
        for result in cursor.execute("select * from Osomens where usuario ='" + self.cajaUsername.get() +"' and contraseña='" + self.cajaPassword.get()+"'" ):
           #print("Usuario "+ result[0]+ " Contraseña "+ str(result[4]))	
            if result[0]=="ADMIN" and result[4]==self.cajaPassword.get():
                app= admin()
                app.mainloop()
                Administrador == True
            elif result[0]=="Cajero" and result[4]==self.cajaPassword.get():
                app= cajero()
                #app.mainloop()
            else:
                self.destroy()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('User Login')
        self.geometry('400x150')
        self.resizable(0, 0)
        self.__create_widgets()
    def __create_widgets(self):
        ttk.Label(self, text='Acceder').grid(column=0, row=0, sticky=tk.W)
        self.cajaUsername = ttk.Entry(self, width=30)
        self.cajaUsername.focus()
        self.cajaUsername.grid(column=1, row=0, sticky=tk.W)

        # Password:
        self.cajaPassword = ttk.Label(self, text='Password').grid(column=0, row=1, sticky=tk.W)
        self.cajaPassword = ttk.Entry(self, width=30, show='*')
        self.cajaPassword.grid(column=1, row=1, sticky=tk.W)
        ttk.Button(self, text='Salir',command=lambda: self.destroy()).grid(column=2, row=4)

    def __create_widgets(self):
        # create the input frame
        input_frame = InputFrame(self)
        input_frame.grid(column=0, row=0)
        # create the button frame
        #button_frame = ButtonFrame(self)
        #button_frame.grid(column=1, row=0)
    def ValidarUsuario(self, username, password):
        print("Conectando a Oracle")
 

class ProdModifier(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Buscador de productos')
        self.geometry('300x100')
        self.resizable(0, 0)
        self.__create_widgets()
    def destroy(self):
        super().destroy()  
    def __create_widgets(self):
        CodProd=ttk.Label(self.root,text='CodProd').grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        Nombre=ttk.Label(self.root,text='Nombre').grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        PrecioVta=ttk.Label(self.root,text='PrecioVta').grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        Stock=ttk.Label(self.root,text='Stock').grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        PrecioCto=ttk.Label(self.root,text='PrecioCto').grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.cajaCodProd = ttk.Entry(self.root, width=30)
        self.cajaCodProd.grid(column=1, row=0, sticky=tk.W)
        self.cajaNombre = ttk.Entry(self.root, width=30)
        self.cajaNombre.grid(column=1, row=1, sticky=tk.W)
        self.cajaPrecioVta = ttk.Entry(self.root, width=30)
        self.cajaPrecioVta.grid(column=1, row=2, sticky=tk.W)
        self.cajaStock = ttk.Entry(self.root, width=30)
        self.cajaStock.grid(column=1, row=3, sticky=tk.W)
        self.cajaPrecioCto = ttk.Entry(self.root, width=30)
        self.cajaPrecioCto.grid(column=1, row=4, sticky=tk.W)
        ttk.Button(self.root, text='Salir',command=lambda: self.destroy()).grid(column=2, row=4)

    #Crear procedimiento para buscar el producto
    

class registroAdm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Registrar')
        self.geometry('400x300')
        self.resizable(0, 0)
        self.__create_widgets()
    def registrar(self):
        cursor.execute("insert into Osomens values ('"+self.usuario.get()+"','"+self.nombre.get()+"','"+self.apellido.get()+"','"+self.email.get()+"','"+self.password.get()+"')")
        #ingreso = "insert into usuario values ('"+self.tipo.get()+"','"+self.nombre.get()+"','"+self.apellido.get()+"','"+self.email.get()+"','"+self.password.get()+"')"
        #print(ingreso)
    def __create_widgets(self):
        tk.Label(self,text='Ingrese los datos del nuevo usuario').grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        tk.Label(self,text='Usuario').grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        tk.Label(self,text='Nombre').grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        tk.Label(self,text='Apellido').grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        tk.Label(self,text='Email').grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        tk.Label(self,text='Contraseña').grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.usuario = tk.Entry(self, width=30)
        self.usuario.grid(column=1, row=1, sticky=tk.W)
        self.nombre = tk.Entry(self, width=30)
        self.nombre.grid(column=1, row=2, sticky=tk.W)
        self.apellido = tk.Entry(self, width=30)
        self.apellido.grid(column=1, row=3, sticky=tk.W)
        self.email = tk.Entry(self, width=30)
        self.email.grid(column=1, row=4, sticky=tk.W)
        self.password = tk.Entry(self, width=30, show='*')
        self.password.grid(column=1, row=5, sticky=tk.W)
        #self.usuario.focus()
        # ingresar datos a la base de datos
        button = ttk.Button(text="Acceder", command=lambda: self.registro())
        button.grid(column=1, row=6)
        #ttk.Button(self, text='Registrar',command=lambda: registrar).grid(column=1, row=6)
        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)
    
        
class admin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Administrador')
        self.geometry('400x100')
        self.resizable(0, 0)
        self.__create_widgets()
    def __create_widgets(self):
        #Seleccione
        ttk.Label(self, text='Seleccione una opcion').grid(column=0, row=0, sticky=tk.W)

        #Registrar
        #Enter to ProdSearch
        ttk.Button(self, text='Productos', command=lambda: cajero()).grid(column=4, row=5)
        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)
        ttk.Button(self, text='Registrar', command=lambda: registroAdm()).grid(column=5, row=5)
        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)
        ttk.Button(self, text='Salir', command=lambda: self.destroy()).grid(column=6, row=5)
    
            
    def destroy(self):
        super().destroy()


class InfoProd ():
    def __init__(self) :
        self.root = tk.Tk()
        self.root.title('InfoPROD')
        self.root.geometry('400x200')
        self.root.resizable(0, 0)
        self.__create_widgets()
        self.root.mainloop()
    def __create_widgets(self):
        CodProd=ttk.Label(self.root,text='CodProd').grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        Nombre=ttk.Label(self.root,text='Nombre').grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        PrecioVta=ttk.Label(self.root,text='PrecioVta').grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        Stock=ttk.Label(self.root,text='Stock').grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        PrecioCto=ttk.Label(self.root,text='PrecioCto').grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        VentasHoy=ttk.Label(self.root,text='VentasHoy').grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        Venta30=ttk.Label(self.root,text='Venta ultimos 30 dias').grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
        #Como llamo para que me imprima el valor que se busco en la base de datos?
        self.CodProd = tk.Entry(self, width=30)
        self.CodProd.grid(column=1, row=0, sticky=tk.W)
    def Resultados():
        cursor4=connection.cursor("select * from MSF where codprod="+cajero.CodProd.get()+";" )
        for result in cursor4:
            print(result)


# ------------------------------------------- CAJERO A PARTIR DE AQUI ------------------------------------------
# ------------------------------------------- CAJERO A PARTIR DE AQUI ------------------------------------------
# ------------------------------------------- CAJERO A PARTIR DE AQUI ------------------------------------------

class cajero():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Cajero')
        self.root.geometry('300x100')
        self.root.resizable(0, 0)
        self.__create_widgets()
        self.root.mainloop()
    def buscador(self):
        cursor1=connection.cursor()
        for result in cursor1.execute("select * from MSF where codprod = '"+self.codprod.get()+"'"):
            print("El producto es: "+result[1]+ " y quedan " + str(result[3])+" unidades")   
            if result[3] > 0:
                print("Hay stock")
                app = Vender()

            elif result[3] == 0:
                print("No hay stock o no existe el producto")
            elif Administrador == True:
                app = ProdModifier()


    def __create_widgets(self):
        #Register Button
        #Seleccione
        ttk.Label(self.root, text='Ingrese el Codigo del producto').grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        #tk.Button(self.root, text='Buscar').grid(column=2, row=1)
        if Administrador == False:
            ttk.Button(self.root, text='Buscar', command=lambda: self.buscador()).grid(column=2, row=1)
            self.codprod = tk.Entry(self.root, width=30)
            self.codprod.focus()
            self.codprod.grid(column=0, row=1, sticky=tk.W)
        if Administrador == True:
            ttk.Button(self.root, text='Buscar', command=lambda: ProdModifier()).grid(column=2, row=1)
            self.codprod = tk.Entry(self.root, width=30)
            self.codprod.focus()
            self.codprod.grid(column=0, row=1, sticky=tk.W)


    def destroy(self):
        self.root.destroy()    

class Vender():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Venta')
        self.root.geometry('400x200')
        self.root.resizable(0, 0)
        self.__create_widgets()
        self.root.mainloop()
        self.__vender()
    def __create_widgets(self):
        #Register Button
        #Seleccione
        ttk.Label(self.root,text='Nombre del producto: ').grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.root, text='Cantidad').grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.root, text='Precio x unidad').grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.root, text='Cantidad que desea vender:').grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.nombre = ttk.Label(self.root,command= lambda: self.buscador())
        self.nombre.grid(column=1, row=0, sticky=tk.W)
        self.cantidad = tk.Entry(self.root, width=30)
        self.cantidad.grid(column=1, row=1, sticky=tk.W)
        self.precio = tk.Entry(self.root, width=30)
        self.precio.grid(column=1, row=2, sticky=tk.W)
        self.cntxventa = tk.Entry(self.root, width=30)
        self.cntxventa.grid(column=1, row=3, sticky=tk.W)
        ttk.Button(self.root, text='Vender').grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        ttk.Button(self.root, text='Salir').grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
    def nombre(self):
        for result in cursor.execute("select nombre from MSF where codprod = '"+self.codprod.get()+"'"):
            print(result[1])

    def __vender(self):
        print(self.nombre.get())
        print(self.cantidad.get())
        print(self.precio.get())
        print(self.total.get())
        cursor3=connection.cursor("execute StockOso("+self.codprod+","+self.cantidad+")") #(id,cantidad)
        
    def destroy(self):
        self.root.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()