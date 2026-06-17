import csv

def entero(documento): #Documento
    if len(documento) == 8:
        try:
            documento=int(documento)
            if documento > 0:
                return True
            else:
                return False
        except:
            return False
    else:
        return False

def vacaciones(dias): #Cantidad de dias solicitados
    if len(dias) <= 2:
        try:
            dias=int(dias)
            if dias > 0:
                return True
            else:
                return False
        except:
            return False
    else:
        return False

def texto(apellido): #Verifica que el apellido sea una cadena de texto
    if len(apellido) > 0 and len(apellido) <=20:
        separar=apellido.split()
        for palabra in separar:
            if palabra.isalpha() == True:
                pass
            else:
                return False
        return True
    else:
        return False

def dias_disponibles(dias,documento): #Validacion de cantidad de dias de vacaciones
    total=0
    with open("data_store/datos.csv", "r", newline="", encoding="UTF-8") as archivo:
        info=csv.DictReader(archivo)
        for empleado in info:
            if empleado['id'] == documento:
                resta1= empleado['dias_disponibles']
                total = int(resta1) - int(dias) 
                if total >= 0:
                    return total
                else:
                    return None

def iguales(apellido,documento): #Para verificar que el apellido y el numero de documento sean los mismos
    with open("data_store/datos.csv","r",newline="", encoding="UTF-8") as archivo:
        info=csv.DictReader(archivo)
        for dato in info:
            if dato['id'] == documento and dato['apellido'] == apellido:
                return True
    return False