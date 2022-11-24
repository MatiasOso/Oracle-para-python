import cx_Oracle
import os


os.environ['TNS_ADMIN'] =r'C:/Users/Usuario/Desktop/Oracle/wallet' #C:\Users\Usuario\Desktop\Oracle\wallet
connection=cx_Oracle.connect('ADMIN','TI2002-sec-213','db-225')
cursor=connection.cursor()
for result in cursor.execute('select * from puntajes_mo'):
    print("Usuario "+ result[1]+ "Puntaje "+ str(result[2]))

