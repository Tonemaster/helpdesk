# instalar 'pip install pyodbc'
import pyodbc

#conexion al servidor por autenticación de sql server
server = 'TMC\SQLEXPRESS'  #aqui pone el nombre del servidor
db = 'dbhelpdesk'          #aqui pone el nombre de la base de datos
user = 'tmc'               #aqui pone el nombre del usuario de sql
password = '55262152'      #aqui la contraseña del usuario sql
driver = '{SQL Server}'    


try:
    conexion = pyodbc.connect('DRIVER='+driver+'; SERVER='+server+';DATABASE='+db+';UID='+user+';PWD='+password)
    print('Se conectó')

    cursor = conexion.cursor()
    cursor.execute("select * from usuarios")   
    rows = cursor.fetchall() 
    for row in rows:
        print(row)

    cursor.close()    

except Exception as ex:
    print('Error:'+str(ex))
finally:
    conexion.close()
    print("Conexión finalizada")