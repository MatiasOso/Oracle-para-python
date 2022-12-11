import tkinter as tk
from tkinter import ttk
import cx_Oracle
import os


os.environ['TNS_ADMIN']='C:/Users/Usuario/Desktop/Oracle/wallet' 
connection=cx_Oracle.connect('ADMIN','TI2002-sec-213','db20220606233104_high')
cursor=connection.cursor()
#Cajero
class InfoProd ():
    def __init__(self) :
        self.root = tk.Tk()
        self.root.title('InfoPROD')
        self.root.geometry('400x200')
        self.root.resizable(0, 0)
        self.__create_widgets()
        self.root.mainloop()
    def __create_widgets(self):
        ttk.Label(self.root,text='CodProd').grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.root,text='Nombre').grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.root,text='PrecioVta').grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.root,text='Stock').grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.root,text='PrecioCto').grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.root,text='VentasHoy').grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.root,text='Venta ultimos 30 dias').grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
        

if __name__ == "__main__":
    app = InfoProd()
    app.mainloop()
