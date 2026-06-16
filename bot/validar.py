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

def texto(apellido):
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
