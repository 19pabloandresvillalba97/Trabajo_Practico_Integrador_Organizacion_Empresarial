## Despliegue y funcionamiento del chatbot de solicitud de vacaciones

Para interactuar con el chatbot de solicitud de vacaciones, el empleado deberá ingresar al sitio web de la empresa:

*https://www.solucionesdelnorte.com.ar*

Una vez dentro del portal, deberá seleccionar la opción *"Solicitar Vacaciones Online"*.

Al acceder a dicha sección, se iniciará la interacción con el chatbot, el cual solicitará los datos necesarios para validar la identidad del empleado:

* DNI
* Apellido

Luego de verificar la información ingresada, el chatbot permitirá realizar la solicitud de vacaciones y mostrará al usuario la información correspondiente obtenida desde la base de datos de la empresa.

Al finalizar el proceso, el sistema informará si la solicitud fue *aprobada* o *rechazada*. En caso de aprobación, la base de datos se actualizará automáticamente registrando la nueva solicitud y descontando los días de vacaciones utilizados.

### Estructura del programa

El chatbot está compuesto por tres módulos principales:

*1. Módulo principal*

* Gestiona el inicio y la finalización de la interacción.
* Coordina el flujo general de la conversación.
* Permite la comunicación entre el usuario y el sistema.
* Informa el resultado final de la solicitud de vacaciones.

*2. Módulo de validación de datos*

* Verifica que los datos ingresados por el usuario sean correctos y cumplan con los formatos establecidos.
* Comprueba, por ejemplo, que el DNI contenga exactamente ocho dígitos y que los campos obligatorios no estén vacíos.
* Evita el ingreso de información inválida que pueda afectar el funcionamiento del sistema.

*3. Módulo de acceso y actualización de datos*

* Lee la información almacenada en la base de datos (archivo CSV).
* Consulta los datos del empleado para validar su identidad y obtener la información necesaria para la solicitud.
* Actualiza automáticamente los registros cuando una solicitud es aprobada, modificando la cantidad de días de vacaciones disponibles.

Gracias a esta estructura modular, el sistema resulta más organizado, facilita el mantenimiento del código y permite futuras ampliaciones de funcionalidades de manera sencilla.
