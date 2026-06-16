import csv
def buscar_apellido(apellido): #Buscar por apellido
    with open("data_store/datos.csv","r",newline="", encoding="UTF-8") as archivo:
        info=csv.DictReader(archivo)
        for palabra in info:
            if palabra['apellido'] == apellido:
                return True
    return False

def buscar_dni(documento): #buscar por documento
    with open("data_store/datos.csv", "r", newline="", encoding="UTF-8") as archivo:
        info=csv.DictReader(archivo)
        for dni in info:
            if dni['id'] == documento:
                return True
    return False

def actualizar_dias(dias, id): #Actulizar dias de vacaciones
    lista=[]
    encabezado=["apellido","id","dias_disponibles"]
    with open("data_store/datos.csv", "w", newline="", encoding="UTF-8") as archivo:
        info=csv.DictWriter(archivo,fieldnames=encabezado)
        for datos in info:
            lista.append(datos)
        for elemento in lista:
            if elemento['id'] == id:
                elemento['dias_disponibles'] == dias
                info.writeheader()
                info.writerows(lista)
                return True

def restantes(id):
    with open("data_store/datos.csv","r",newline="",encoding="UTF-8") as archivo:
        info=csv.DictReader(archivo)
        for dias in info:
            if dias['id'] == id:
                return dias['dias_disponibles']
