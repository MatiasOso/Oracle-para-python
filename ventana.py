import tkinter as tk
from tkinter import ttk
import cx_Oracle
import os


os.environ['TNS_ADMIN']='C:/Users/Usuario/Desktop/Oracle/wallet' 
connection=cx_Oracle.connect('ADMIN','TI2002-sec-213','db20220606233104_high')
cursor=connection.cursor()
#Registro      

class ProdModifier(tk.Tk):
    def __init__(self,container):
        super().__init__(container)
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


if __name__ == "__main__":
    app =ProdModifier(container=None)
    app.mainloop()
