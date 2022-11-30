# nota: 4.5

import utilidades as util
from datetime import datetime
from time import sleep

lista_usuarios = []
lista_citas = []
menu = 0

while (menu != 4):
  print("""
----------------------------------------------------------------------
  Bienvenido al sistema de agendamiento de citas
----------------------------------------------------------------------
        1. Registrar persona
        2. Visualizar listado de las personas
        3. Asignar una cita
        4. Salir de la aplicación
  """)
  
  menu = util.convertir_entero(input("Seleccione una opción: "))
  
  util.clear()

  if (menu == 1):
    #Capturar los datos validados con diccionario
    dicc_datos = {"tipo_documento":"", "numero_documento":"", "nombre":"", "apellido":"", "fecha_nacimiento":"", "rh_grupo":"", "email":"", "telefono":"", "cita":"Sin cita"}
	  
    validar_tipo_documento = False
    while (validar_tipo_documento == False):
      tipo = input("Ingrese el tipo de documento, solo se acepta: CC, CE, TI, PA: ").upper()
      validar_tipo_documento = util.validar_tipo_documento(tipo)
  
    validar_documento = False
    while ( validar_documento == False):
      documento = input("Ingrese el número de documento: ")
      validar_documento = util.validar_numero_documento(documento)    
      usuario_existe = util.buscar_documento(tipo, documento, lista_usuarios )
      if usuario_existe == True:
          print("El documento que digito ya existe existe")
          validar_documento = False
    
    validar_nombre = False
    while ( validar_nombre == False):
      nombre = input("Ingrese su nombre: ")
      validar_nombre = util.validar_nombre(nombre)
    
    validar_apellido = False
    while ( validar_apellido == False):
      apellido = input("Ingrese su apellido: ")
      validar_apellido = util.validar_nombre(apellido)
    
    validar_fecha = False
    while (validar_fecha == False):
      fecha_temp = input("Ingrese la fecha de nacimiento: con el formato AAAA-MM-DD: ")
      validar_fecha = util.validar_fecha(fecha_temp, '%Y-%m-%d')
    
    validar_rh = False
    while ( validar_rh == False):
      rh = input("Ingrese el grupo sanguineo, primer carácter solo permite O, A, B, el segundo carácter solo permite (+) o (-) : ").upper()
      validar_rh = util.validar_rh(rh)
    
    validar_correo = False
    while ( validar_correo == False):
      correo = input("Ingrese el correo electrónico: ").lower()
      validar_correo = util.validar_correo(correo)

    validar_telefono = False
    while( validar_telefono == False):
      telefono = input("Ingrese el número telefónico: ")
      validar_telefono = util.validar_telefono(telefono)
    
    #Creación de diccionario de registro    
    dicc_datos["tipo_documento"] = tipo
    dicc_datos["numero_documento"] = documento
    dicc_datos["nombre"] = nombre
    dicc_datos["apellido"] = apellido
    dicc_datos["fecha_nacimiento"] = fecha_temp
    dicc_datos["rh_grupo"] = rh
    dicc_datos["email"] = correo
    dicc_datos["telefono"] = telefono

    #Agregar a las lista de usuarios
    lista_usuarios.append(dicc_datos)

    print("\nUsuario registrado con exito")
    
  elif (menu == 2):
    print("""
----------------------------------------------------------------------
                  Visualización listado de personas:
----------------------------------------------------------------------
""" )
    titulo = f"Posicion \t Tipo documento \t\t Número documento \t\t Nombres y apellidos \t\t Edad \t\t Fecha/hora Cita"
    print(titulo)
    
    for posicion, usuario in enumerate(lista_usuarios):
      #Calcular edad
      fecha_nacimiento = datetime.strptime(usuario['fecha_nacimiento'],'%Y-%m-%d')
      edad = datetime.now().year - fecha_nacimiento.year
      
      #Buscar si tiene citas asociadas
      fecha_cita = ""
      for cita in lista_citas:
        if cita[0] == usuario['numero_documento']:
          fecha_cita = cita[1]

      registro = f"{posicion+1} \t\t {usuario['tipo_documento']} \t\t {usuario['numero_documento']} \t\t {usuario['nombre']} {usuario['apellido']} \t\t {edad} años \t\t {fecha_cita}"
      print(registro)

      input("\nOprima tecla enter para continuar...")

  elif (menu == 3):

    validar_tipo_documento = False
    while (validar_tipo_documento == False):
      tipo = input("Ingrese el tipo de documento, solo se acepta: CC, CE, TI, PA: ").upper()
      validar_tipo_documento = util.validar_tipo_documento(tipo)
  
    validar_documento = False
    while ( validar_documento == False):
      documento = input("Ingrese el número de documento: ")
      validar_documento = util.validar_numero_documento(documento)    
    
    #Buscar el usuario
    usuario_existe = util.buscar_documento(tipo, documento, lista_usuarios )
    if usuario_existe == True:
      validar_fecha = False
      while (validar_fecha == False):
        fecha_temp = input("Ingrese la fecha/hora de la cita: con el formato AAAA-MM-DD HH:MM :")
        validar_fecha = util.validar_fecha(fecha_temp, '%Y-%m-%d %H:%M')      
        #Validar fecha de cita
        if validar_fecha :
          if datetime.strptime(fecha_temp, '%Y-%m-%d %H:%M') <= datetime.now():
            print("No es posible asignar la cita en la fecha indicada")
            validar_fecha = False
          else:
            validar_fecha = True
      
      fecha_cita = datetime.strptime(fecha_temp, '%Y-%m-%d %H:%M')
      tupla_cita = (tipo, documento, fecha_temp)
      lista_citas.append(tupla_cita)

      # Buscar usuario para extraer datos
      usuario = util.buscar_usuario(tipo, documento, lista_usuarios)
      print("\nEstimado {0} {1} su cita fue asignada correctamente para el día, {2}, a las {3} horas.".format(usuario["nombre"], usuario["apellido"], fecha_cita.strftime("%Y-%m-%d"), fecha_cita.strftime("%H:%M")))
    else:
      print("El usuario no esta registrado...")
              
  elif (menu == 4):
    print("Saliendo de la aplicación")
  else:
    print("Opción no válida")
  
  sleep(2)
  util.clear()

with open('lista_usuarios.txt','w') as f:
    json.dump(lista_usuarios,f,indent= 4)
with open('lista_citas.txt','w') as f:
    json.dump(lista_citas,f,indent= 4)

menu2 = 0
while (menu2 != 7):
    print("""
    ------------------------------------------------------------------------
    Menu de Busqueda
    ------------------------------------------------------------------------
    1. busqueda por nombre
    2. busqueda por apellido
    3. busqueda por RH
    4. busqueda por documento
    5. busqueda por correo electronico
    6. busqueda por telefono
    7. salir del menu de busqueda""")
    menu2 = util.convertir_entero(input("Seleccione una opción: "))

    util.clear()
    if menu2 == 1:
        busqueda_nombre = False
        while (busqueda_nombre == False):
            busqueda_nombre = util.buscar_usuario("nombre",input("ingrese el nombre: "),lista_usuarios)
            print(busqueda_nombre)
    if menu2 == 2:
        busqueda_apellido = False
        while (busqueda_apellido == False):
            busqueda_apellido = util.buscar_usuario("apellido",input("ingrese el apellido: "),lista_usuarios)
            print(busqueda_apellido)
    if menu2 == 3:
        busqueda_RH = False
        while(busqueda_RH == False):
            busqueda_RH = util.buscar_usuario("rh_grupo",input(
                "Ingrese el grupo sanguineo, primer carácter solo permite O, A, B, el segundo carácter solo permite (+) o (-) : ").upper(),lista_usuarios)
            validar_rh = util.validar_rh(rh)
            print(busqueda_RH)
    if menu2 == 4:
        validar_tipo_documento = False
        while (validar_tipo_documento == False):
            tipo = input("Ingrese el tipo de documento, solo se acepta: CC, CE, TI, PA: ").upper()
            validar_tipo_documento = util.validar_tipo_documento(tipo)
        validar_documento = False
        while (validar_documento == False):
            documento = util.buscar_usuario("numero_documento",input("Ingrese el número de documento: "),lista_usuarios)
            validar_documento = util.validar_numero_documento(documento)
            usuario_existe = util.buscar_documento(tipo, documento, lista_usuarios)
            if usuario_existe == True:
                print("El documento que digito ya existe existe")
                validar_documento = False

    if menu2 == 5:
        busqueda_correo = False
        while (busqueda_correo == False):
            busqueda_correo = util.buscar_usuario("email",input("Ingrese el correo electrónico: ").lower(),lista_usuarios)
            validar_correo = util.validar_correo(correo)
    if menu2 == 6:
        busqueda_telefono = False
        while (busqueda_telefono == False):
            busqueda_telefono = util.buscar_usuario("telefono",input("Ingrese el número telefónico: "),lista_usuarios)
            validar_telefono = util.validar_telefono(telefono)
    if menu2 == 7:
        print("Saliendo de la aplicación")
    else:
        print("Opción no válida")

    sleep(2)
    util.clear()

lista_apellidos_ordenados=[]
for usuario in busqueda_apellido:
    lista_apellidos_ordenados.append(usuario["apellido"])
    lista_apellidos_ordenados.sort()
    print(lista_apellidos_ordenados)
