import os
import cx_Oracle
from tkinter import *
import tkinter as tk
from tkinter import ttk

ventana = Tk()
ventana.geometry("700x500")
ventana.configure(bg="white")

os.environ['TNS_ADMIN']='C:/Users/Usuario/Desktop/Oracle/wallet' 
conexion = cx_Oracle.connect('ADMIN','TI2002-sec-213','db20220606233104_high')
ventana = Tk()


