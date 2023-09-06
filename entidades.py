#Entidad Roles
Roles = {}
    #inicializamos con estos roles
Roles = {
    1: (1,"Administrador"),
    2: (2,"Técnico"),
    3: (3,"Usuario")
}
    #metodo para crear un nuevo rol
def new_rol (nombre_rol):
    id_rol = len(Roles) + 1
    rol = {
        "id_rol": id_rol,
        "nombre_rol": nombre_rol,
    }
    Roles[id_rol] = rol
    return id_rol

#Entidad Status
Status = {}
    #inicializamos con estos Status
Status = {
    1: (0, "Abierto"),
    2: (1, "En Progreso"),
    3: (2, "Resuelto")
}
    #metodo para crear un nuevo status
def new_status (status):
    id_status = len(Status) + 1
    stu = {
        "id_status": id_status,
        "nombre_rol": status,
    }
    Status[id_status] = stu
    return id_status

#Entidad Usuarios
Usuarios = {}
    #inicializamos con estos Status
Usuarios = {
    1: (1,"admin","1234",1),
    2: (2,"tecnico","5678",2),
    3: (3,"wilson","0000",3),
    4: (4,"harol","9999",3)
    }
    #metodo para crear un nuevo usuario
def new_usuario(nombre_usurio,password,id_rol):
    id_usuario = len(Usuarios) + 1
    user = {
        "id_usuario": id_usuario,
        "nombre_usuario": nombre_usurio,
        "password": password,
        "id_rol": id_rol,
    }
    Usuarios[id_usuario] = user
    return id_usuario

#Entidad Tipo_casos
Tipo_casos = {}
    #inicializamos con estos tipos de casos
Tipo_casos = {
    1: (1,"Fallo de software","si su equipo presenta errores al iniciar algun programa o el sistema no corre de forma correcta."),
    2: (2,"Daño de hardware","si su equipo no enciende o tiene algun componente fisico que presente fallas.")
}
    #metodo para crear un nuevo tipo de caso
def new_tipo_caso(tipo,descripcion):
    id_tipo = len(Tipo_casos) + 1
    tp = {
        "id_tipo": id_tipo,
        "tipo": tipo,
        "descripcion": descripcion,
    }
    Tipo_casos[id_tipo] = tp
    return id_tipo

#Entidad Casos
Casos = {}
    #metodo para crear un nuevo caso
def new_caso (id_tipo_caso,descripcion,id_user_solicitante):
    id_caso = len(Casos) + 1
    caso = {
        "id_caso": id_caso,
        "id_tipo_caso": id_tipo_caso,
        "descripcion": descripcion,
        "id_user_solicitante": id_user_solicitante,
        "id_user_tec": None,
        "id_status": 0,
    }
    Casos[id_caso]= caso
    return id_caso