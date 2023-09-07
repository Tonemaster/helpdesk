
#esta libreria me sirve para aplicar a los texto que no se deben ver en consola, ejemplo: las contraseñas
import getpass
#importo las entidades del archivo entidades.py
from entidades import Usuarios,Roles,Status,Tipo_casos,new_tipo_caso,Casos,new_caso

# Función para consultar por nombre
def consultar_por_nombre(nombre_usuario, diccionario):
  for id, datos_usuario in diccionario.items():
    if datos_usuario[1] == nombre_usuario:
      return datos_usuario
  return None

def validar_login (rol,nombre_usuario,clave):
    #limpiamos
    datos_usuario=""
    # Obtenemos los datos del usuario
    datos_usuario = consultar_por_nombre(nombre_usuario, Usuarios)

    print(datos_usuario)
    

    if datos_usuario is not None:
        # Imprimimos los datos del usuario
        nombre_usuario = datos_usuario[1]
        if datos_usuario[2]==clave:
           pass
        else:
           print("Contraseña incorrecta!")
           return False 
        if datos_usuario[3]==rol:
           pass
        else:
           print("Rol incorrecto!")
           return False        
        
    else:
        print("El usuario no existe!")
        return False
    return True

#while True :


def login():
    # Pedimos al usuario que seleccione su rol
    print("Selecciona tu rol:")
    for item in Roles.items():
        print(item[0],": ",item[1][1])
    rol_selec = int(input("Rol: "))
        # Pedimos al usuario que ingrese su nombre de usuario
    print("Ingresa tu nombre de usuario:")
    nombre_user = input()
        # Pedimos al usuario que ingrese su contraseña
    print("Ingresa su contraseña:")
    password = getpass.getpass()
    print("")

    if validar_login(rol_selec,nombre_user,password):
        print()
        print("Inicio de sesión correcto")
        print()
        print("\033[1;30;42m"+"Bienvenido a helpdesk."+"\033[0;37m")
        if rol_selec == 2:
            print("Acciones permitidas")
            for item in Tipo_casos.items():
                print(item[0],": ",item[1][1])
            print(Roles[2][1])
            print(rol_selec)
            return True
        if rol_selec == 3:
            print("Seleccione Novedad a Reportar")
            for item in Tipo_casos.items():
                print(item[0],": ",item[1][2])
                print(Roles[2][1])
            print(rol_selec)
            caso = int(input("Codigo caso: "))
            return True
    else:
        print("Inicio de sesión incorrecto!")
        print("")
        return False
            
while not login():
    pass  