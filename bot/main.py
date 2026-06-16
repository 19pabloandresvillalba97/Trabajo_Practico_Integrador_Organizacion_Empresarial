import leer_y_actualizar, validar

print("\t\tSISTEMA PARA GESTIONAR LICENCIA ONLINE")
print()
print("Hola, soy tu asistente virtual para que puedas solicitar tu licencia! Espero que te encuentre bien! ☺")
print("Comenzare a pedirte tus datos, simplemente sera tu Apellido y tu Documento Nacional de Identidad")

while True:
    condi_1 = False
    condi_2 = False
    apellido_empleado=input("Dime, cual es tu apellido?\n>>>").capitalize()
    apellido=validar.texto(apellido_empleado)
    if apellido:
        condi_1=leer_y_actualizar.buscar_apellido(apellido_empleado)
    print("Muy bien ! Ahora dime cual es tu Numero de documento (Sin puntos)")
    documento_empleado=input("Ingresa el numero: ")
    documento=validar.entero(documento_empleado)
    if documento:
        condi_2=leer_y_actualizar.buscar_dni(documento_empleado)
    if condi_1 and condi_2:
        break
    else:
        print("\nUps, asegurate de poner datos correctamente, intentemos nuevamente!")

print("Perfecto, tus datos fueron validados correctamente, continuamos...\n")
