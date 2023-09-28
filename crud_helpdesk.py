# instalar 'pip install pyodbc'
import pyodbc
import getpass
from datetime import datetime


# DATOS DE CONECCIÓN
#conexion al servidor por autenticación de sql server
server = 'TMC\SQLEXPRESS'  #aqui pone el nombre del servidor
db = 'dbhelpdesk'          #aqui pone el nombre de la base de datos
user = 'tmc'               #aqui pone el nombre del usuario de sql (login)
password = '55262152'      #aqui la contraseña del usuario sql (login)
driver = '{SQL Server}'  

# CONEXIÓN
def conexion():
    try:
        conexion = pyodbc.connect('DRIVER='+driver+'; SERVER='+server+';DATABASE='+db+';UID='+user+';PWD='+password)
        return conexion
    except Exception as ex:
        print('Error:'+str(ex))
    return conexion

# CONSULTAR (SELECT)
def ConsultarRoles():
    con = conexion()
    cursor = con.cursor()
    cursor.execute("select * from roles")  
    rows = cursor.fetchall() 
    print("""
    =============================================================
                            Lista de Roles
    =============================================================
    """)
    for fila in (rows):
        print(fila[0]," ",fila[1])
    cursor.close() 
    con.close()
    return rows

def ConsultarEstados():
    con = conexion()
    cursor = con.cursor()
    cursor.execute("select * from estados")  
    rows = cursor.fetchall()
    print("""
    =============================================================
                            Lista de Estados
    =============================================================
    """) 
    for fila in rows:
        print(fila)
    cursor.close() 
    con.close()
    return rows

def ConsultarTipoCasos():
    con = conexion()
    cursor = con.cursor()
    cursor.execute("select * from tipo_caso")  
    rows = cursor.fetchall()
    print("""
    =============================================================
                        Lista de Tipos de Casos
    =============================================================
    """) 
    for fila in rows:
        print(fila)
    cursor.close() 
    con.close()
    return rows

# REGISTRAR (INSERT)
#ROLES
def insertRoles(rol):
    con=conexion()
    cursor=con.cursor()
    cursor.execute('insert into roles(nombre_rol) values(?)',rol)
    cursor.commit()
    cursor.close()
    con.close()
    return True
def registrarRol():
    print("""
    =============================================================
                        Registro de Roles
    =============================================================
    """)
    nom_rol= input('Nombre del nuevo Rol: ')
    mensaje = "Inserción Exitosa" if insertRoles(nom_rol) else "Error al insertar!" #operador ternario
    return print(mensaje) 

#ESTADOS
def insertEstado(status):
    con=conexion()
    cursor=con.cursor()
    cursor.execute('insert into estados(estado) values(?)',status)
    cursor.commit()
    cursor.close()
    con.close()
    return True
def registrarEstado():
    print("""
    =============================================================
                        Registro de Estados
    =============================================================
    """)
    status = input('Nombre del nuevo Estado: ')
    mensaje = "Inserción Exitosa" if insertEstado(status) else "Error al insertar!" #operador ternario
    return print(mensaje)

#TIPO_CASO
def insertTipoCaso(tipo,descripcion):
    con=conexion()
    cursor=con.cursor()
    cursor.execute('insert into tipo_caso(tipo,descripcion) values(?,?)',tipo,descripcion)
    cursor.commit()
    cursor.close()
    con.close()
    return True
def registrarTipoCaso():
    print("""
    =============================================================
                    Registro de Tipos de Caso
    =============================================================
    """)
    tipo=input('Nombre del nuevo tipo de caso: ')
    descripcion=input('Ingrese una descripción para este nuevo tipo de caso: ')
    mensaje = "Inserción Exitosa" if insertTipoCaso(tipo,descripcion) else "Error al insertar!" #operador ternario
    return print(mensaje)

def insertUsuario(nombre,apellido,edad,telefono,direccion,fechaNacimiento,rol,password,activo):
    con=conexion()
    cursor =con.cursor()
    #set dateformat dmy;
    cursor.execute('''
                   insert into usuarios(nombre,apellido,edad,telefono,direccion,fecha_nacimiento,id_rol,passwords,activo) 
                   values(?,?,?,?,?,?,?,?,?)''',nombre,apellido,edad,telefono,direccion,fechaNacimiento,rol,password,activo)
    cursor.commit()
    cursor.close()
    con.close()
    return True
def registrarUsuario():
    print("""
    =============================================================
                        Registro de Usuarios
    =============================================================
    """)
    nom=input('Ingrese el Nombre de Usuario: ')
    ape=input('Ingrese el Apellido de Usuario: ')
    edad=input('Ingrese la edad: ')
    tel=input('Ingrese un telefono: ')
    direc=input('Ingrese la dirección: ')
    fecha = input('Ingrese la fecha de nacimiento (dd/mm/yyyy): ')
    fecha_dt = datetime.strptime(fecha, '%d/%m/%Y')
    print("Selecciona un Rol de la lista indicando el número: ")
    ConsultarRoles()
    rol=input("Indique el número de Rol: ")
    print("Ingrese su contraseña:")
    passw = getpass.getpass()
    activo='SI'
    mensaje="Registro exitoso." if insertUsuario(nom,ape,edad,tel,direc,fecha_dt,rol,passw,activo) else "Error al registrar!"
    return print(mensaje)
# ACTUALIZAR (UPDATE)

# ELIMINAR (DELETE)
registrarRol()
registrarUsuario()