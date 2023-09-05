# Definimos el diccionario de credenciales
roles={
    "1":"Administrador",
    "2":"Técnico",
    "3":"Usuario"
}
credenciales = {
    ["1","admin", "1234"],
    ["2","tecnico", "5678"],
    ["3","usuario", "9012"],
    ["1","admin2","4321"]
}
nombre_usuario = ""
contraseña = ""
rol_usuario = ""


# Definimos la función `login()`, que se encarga de verificar las credenciales del usuario
def login():
    global nombre_usuario
    global contraseña
    global rol_usuario

    # Mostramos las opciones de rol
    for rol in roles:
        print(f"{rol}: {roles[rol]}")

    # Solicitamos al usuario que ingrese su rol
    rol_usuario = input("Seleccione un rol: ")

    # Verificamos si el rol es válido
    if rol_usuario in roles:
        # Obtenemos las credenciales del rol seleccionado
        credenciales_del_rol = credenciales[roles[rol_usuario]]

        # Solicitamos al usuario que ingrese su nombre de usuario
        nombre_usuario = input("Ingrese su nombre de usuario: ")

        # Solicitamos al usuario que ingrese su contraseña
        contraseña = input("Ingrese su contraseña: ")

        # Verificamos si las credenciales son válidas
        if credenciales_del_rol[0] == nombre_usuario and credenciales_del_rol[1] == contraseña:
            print("Inicio de sesión exitoso!")
            return True
        else:
            print("Credenciales incorrectas.")
            return False
    else:
        print("Rol no válido.")
        return False

# Definimos la función `menu()`, que se encarga de mostrar el menú principal
def menu():
    # Creamos un diccionario con las opciones del menú principal
    options = {
        "1": "Opción 1",
        "2": "Opción 2",
        "3": "Opción 3",
        "4": "Salir"
    }

    # Mostramos el menú al usuario
    for option in options:
        print(f"{option}: {options[option]}")

    # Solicitamos al usuario que seleccione una opción
    selected_option = input("Seleccione una opción: ")

    # Ejecutamos la acción asociada a la opción seleccionada
    if selected_option in options:
        options[selected_option]()
    else:
        print("Opción no válida.")

# Llamamos a la función `login()` para iniciar sesión
while not login():
    pass

# Llamamos a la función `menu()` para mostrar el menú principal
while True:
    menu()