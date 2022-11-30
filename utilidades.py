from datetime import datetime
import re
from os import system, name

def convertir_entero (stringValue):
  """ 
	Función encarga de convertir a entero

	Parameters
	-----------------
	stringValue : str

	Returns
	------------------
	int 
	"""
  # No permitir ingreso
  try:
    entero = int(stringValue)
    return entero
  except ValueError:
    return 0
  
def validar_tipo_documento (stringTipo):
  """ 
	Función validar el tipo de documento

	Parameters
	-----------------
	stringTipo : str

	Returns
	------------------
	bool 
	"""
  lista_tipo = ["CC", "CE", "TI", "PA"]
  
  if stringTipo in lista_tipo:
    return True
  else:
    return False
  
def validar_numero_documento (stringNumero):
  """ 
	Función validar el numero de documento

	Parameters
	-----------------
	stringNumero : str

	Returns
	------------------
	bool 
	"""
  if stringNumero.isdigit() and len(stringNumero) > 6 and len(stringNumero) < 13 and stringNumero[0] != "0":
    return True
  else:
    return False

def validar_nombre (stringNombre):
  """ 
	Función validar el nombre del usuario

	Parameters
	-----------------
	stringNombre : str

	Returns
	------------------
	bool 
	"""
  if stringNombre.isalpha() and len(stringNombre) < 31 and stringNombre !="":
    return True
  else:
    return False

def validar_fecha (stringFecha, formato):
  """ 
	Función validar las fecha

	Parameters
	-----------------
	stringFecha : str

	Returns
	------------------
	bool 
	"""
  try:
    stringFecha = datetime.strptime(stringFecha, formato)
    return True
  except ValueError:
    return False
  
def validar_rh (stringSangre):
  """ 
	Función validar las fecha

	Parameters
	-----------------
	stringSangre : str

	Returns
	------------------
	bool 
	"""
  lista_grupo_sanguineo = ["O","A","B"]
  lista_positivo_negativo = ["+","-"]
  
  if len(stringSangre) == 2 and stringSangre[0] in lista_grupo_sanguineo and stringSangre[1] in lista_positivo_negativo:
    return True
  else:
    return False
  
def validar_correo (stringCorreo):
  """ 
	Función validar correo

	Parameters
	-----------------
	stringCorreo : str

	Returns
	------------------
	bool 
	"""
  patron = '^[(a-z0-9\_\-\.)]{3,10}@[(a-z0-9\_\-)]{3,}\.[(a-z)]{2,3}'
  if re.search(patron, stringCorreo) and len(stringCorreo) < 51:
    return True
  else:
    return False
  
  

def validar_telefono (stringTelefono):
  """ 
	Función validar telefono

	Parameters
	-----------------
	stringTelefono : str

	Returns
	------------------
	bool 
	"""
  if stringTelefono.isdigit() and len(stringTelefono) > 6 and len(stringTelefono) < 11:
    return True
  else:
    return False
  
def buscar_documento (tipo,documento, lista):
  """ 
	Función buscar documento

	Parameters
	-----------------
	stringDocumento : str

	Returns
	------------------
	bool 
	"""
  documento_existe = False
  for elemento in lista:
    if elemento["numero_documento"] == documento and elemento["tipo_documento"] == tipo:
      documento_existe = True
  return documento_existe

def buscar_usuario (tipo,documento, lista):
  """ 
	Función buscar usuario

	Parameters
	-----------------
	tipo : str
    documento : str
    lista : list

	Returns
	------------------
	dict

	"""
  usuario = None
  for elemento in lista:
    if elemento["numero_documento"] == documento and elemento["tipo_documento"] == tipo:
      return elemento
  return usuario

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def buscar_usuario(_filtro,_busqueda,_lista):
    lista_resultado=[]
    for usuario in _lista:
        if usuario[_filtro] == _busqueda:
            lista_resultado.append(usuario)
    return (lista_resultado,True)