import leer_y_actualizar, validar

print("\t\tSISTEMA PARA GESTIONAR LICENCIA ONLINE")
print()
print("Hola, soy tu asistente virtual para que puedas solicitar tu licencia! Espero que te encuentre bien! ☺")
print("Comenzare a pedirte tus datos, simplemente sera tu Apellido y tu Documento Nacional de Identidad")

while True:
    condi_0 = False
    condi_1 = False
    condi_2 = False
    apellido_empleado=input("Dime, cual es tu apellido?\n>>>").capitalize()
    apellido=validar.texto(apellido_empleado)
    if apellido:
        condi_1=leer_y_actualizar.buscar_apellido(apellido_empleado)
    print("\nMuy bien ! Ahora dime cual es tu Numero de documento (Sin puntos)")
    documento_empleado=input("Ingresa el numero: ")
    documento=validar.entero(documento_empleado)
    if documento:
        condi_2=leer_y_actualizar.buscar_dni(documento_empleado)
    if validar.iguales(apellido_empleado,documento_empleado):
        condi_0 = True
    if condi_0 and condi_1 and condi_2:
        break
    else:
        print("\nUps, ocurrio un error! Asegurate de poner datos correctamente, intentemos nuevamente!")

print("\nPerfecto, tus datos fueron validados correctamente, continuamos...\n")
print("Muy bien, estamos cerca de terminar con tu solicitud!\n")
print("Sabes cuantos dias de vacaciones solicitaras?")
condi_3 = False
condi_4 = False
cantidad=input("Dime cuantos dias: ")
validar_dias=validar.vacaciones(cantidad)
if validar_dias:
    condi_3 = True
    restante=validar.dias_disponibles(cantidad,documento_empleado)
    if restante >= 0:
        condi_4=True
if condi_3 and condi_4:
    print("\nPerfecto, estoy trabajando en tu solicitud\n")
    print("\nYa casi estamos\n")
    print("\nPerfecto, solicitud aprobada!!\n\n")
    leer_y_actualizar.actualizar_dias(restante,documento_empleado)
    disponible=leer_y_actualizar.restantes(documento_empleado)
    print()
    print(f"Me agradada informale señor {apellido_empleado} que solicito {cantidad} dias de vaciones, y le quedan {disponible} dias para tener otras vacaciones!\n")
    print("\nAnte cualquier duda no dude en comunicarse con su jefe/encargado\n")
    print("\nMe despido, que tenga buen dia!\n")
elif condi_3 == True and condi_4 == False:
    print("\nNo dispones de esa cantidad de dias para salir de vacacaciones, intentalo nuevamente mas tarde!\nHasta pronto!")
else:
    print("Vaya, te equivocaste, porfavor intenta nuevamente mas tarde!\nHasta pronto!")

