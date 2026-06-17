import leer_y_actualizar, validar

print("\t\tSISTEMA PARA GESTIONAR LICENCIA ONLINE")
print()
print("Hola, soy tu asistente virtual para que puedas solicitar tu licencia! Espero que te encuentre bien! ☺")
print("Comenzare a pedirte tus datos, simplemente sera tu Apellido y tu Documento Nacional de Identidad")

while True:
    condi_0 = False #Condicion de que el apellido y el DNI sean de la misma fila
    condi_1 = False #Condicion que valida si se ingreso una cadena de texto
    condi_2 = False #Condicion que valida si se ingreso un numero entero de longitud = 8
    name=input("Dime, cual es tu apellido?\n>>>").capitalize()
    apellido=validar.texto(name) #Devuelve true o false, valida que sea una cadena de texto
    if apellido: #true
        condi_1=leer_y_actualizar.buscar_apellido(name)
    print("\nMuy bien ! Ahora dime cual es tu Numero de documento (Sin puntos)")
    id=input("Ingresa el numero: ")
    documento=validar.entero(id) #Devuelve True o false, valida que sea un numero de longitud 8
    if documento: #true
        condi_2=leer_y_actualizar.buscar_dni(id)
    if validar.iguales(name,id): #Valida que el nombre y el dni sean de la misma fila (es decir mismo empleado), devuelve true o false
        condi_0 = True
    
    #Compuerta exclusiva de datos validos
    if condi_0 and condi_1 and condi_2: 
        break
    else:
        print("\nUps, ocurrio un error! Asegurate de poner datos correctamente, intentemos nuevamente!")



print("\nPerfecto, tus datos fueron validados correctamente, continuamos...\n")
print("Muy bien, estamos cerca de terminar con tu solicitud!\n")
print(f"\tTienes {leer_y_actualizar.restantes(id)} dias disponibles para salir de vacaciones!\n")
print("Sabes cuantos dias de vacaciones solicitaras?")
condi_3 = False #Condicion que valida que la longitud del numero sea menoy o igual que 2
condi_4 = False #Condion que valida si el numero de dias solicitados esta dentro de los dias que dispone
days=input("Dime cuantos dias: ")
validar_dias=validar.vacaciones(days)
if validar_dias:
    condi_3 = True # Dias de longitud 2
    restante=validar.dias_disponibles(days,id) #Puede devolver un numero entero mayor a 0 o un False
    if restante > 0: #si devuelve un entero
        condi_4=True #Devuelve los dias de vacaciones que le quedan al empleado

#Conpuerta exclusiva de dias disponibles
if condi_3 and condi_4: #Datos disponibles ? SI
    print("\nPerfecto, estoy trabajando en tu solicitud\n")
    print("\nYa casi estamos\n")
    print("\nPerfecto, solicitud aprobada!!\n\n")
    leer_y_actualizar.actualizar_dias(restante,id) #Actualiza el archivo csv con la cantidad nueva de dias disponibles que le queda de vacaiones
    disponible=leer_y_actualizar.restantes(id) #Guarda la cantidad actual de dias de cavaciones que le quedan para mostrar por mensaje
    print()
    print(f"Me agradada informale señor {name} que solicito {days} dias de vaciones, y le quedan {disponible} dias para tener otras vacaciones!\n")
    print("\nAnte cualquier duda no dude en comunicarse con su jefe/encargado\n")
    print("\nMe despido, que tenga buen dia!\n")
elif condi_3 == True and condi_4 == False: #DATOS DISPONIBLES ? NO
    print("\nNo dispones de esa cantidad de dias para salir de vacacaciones, intentalo nuevamente mas tarde!\nHasta pronto!")
else: #DATOS DISPONIBLES ? NO
    print("Vaya, te equivocaste, porfavor intenta nuevamente mas tarde!\nHasta pronto!")

