# Sensible Data System

## Descripción

El sistema permite la encriptación de información sensible de las personas. De manera que solo pueda ser accedida por personas u organismos autorizados. Por ejemplo:

* Declaraciones juradas
* Información clínica

## Componentes

El sistema se divide en:
* **Cliente**: para la carga de los datos sensibles y firmados por el autor. Por ejemplo podría ser utilizado por personal médico si el sistema resolviese el almacenado de información médica sensible o el mismo paciente. Estos datos deben ser almacenados encriptados con la clave pública del sistema de cifrado.

* **Sistema de cifrado**: este sistema es el que almacena los datos sensibles encriptados, mediante su clave privada puede desencriptar los datos sensibles y generar con ellos un archivo en un formato legible por el organismo o persona autorizada. Devuelve el mismo encriptado por la clave pública que esta persona provee. El sistema debe validar los pedidos de estos archivos únicamente permitiendo el acceso por el personal autorizado.

* **Sistema de descifrado**: mediante la clave privada del organismo autorizado, desencripta el archivo generado por el sistema de cifrado.

![Vista general](https://user-images.githubusercontent.com/45921171/102136261-ec173780-3e37-11eb-96cf-40ca2ebf3f91.jpg)
