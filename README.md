# Sensible Data System

## Descripción

El sistema apunta a resolver la distribución de información sensible.
Utiliza encriptación para que la información sensible solo pueda ser accedida por personas u organismos autorizados y garantizar la confidencialidad. Adicionalmente, emplea la firma digital para poder verificar la integridad y autenticidad de la información.

## Caso de uso

En este caso tomaremos como caso la encriptación de información clínica de pacientes. Sin embargo, podría utilizarse en sistemas de distinta naturaleza (por ejemplo, declaraciones juradas de funcionarios) sin mayores cambios.

## Componentes

El sistema se divide en:

* **Cliente**: se encarga de la carga de los datos de los pacientes, los cuales son considerados sensibles. Estos datos son firmados por el paciente, para poder verificar su integridad y autenticidad.

* **Sistema de cifrado**: este sistema almacena los datos sensibles. Recibe los datos firmados por los pacientes y los encripta, para garantizar la confidencialidad. Para ello, encripta los datos con una clave simétrica aleatoria utilizando el algoritmo de AES, luego con su clave pública de RSA encripta esta clave y persiste ambos archivos.
Este sistema acepta solicitudes de la información guardada: primero valida la identidad del médico solicitante. Para realizar esta validación, se solicita la clave pública al médico solicitante y se verifica mediante una whitelist de certificados que se consideran válidos o bien también puede ingresar un dato más fácilmente recordable por el personal médico como puede ser su DNI o su matrícula y que el sistema tenga asociado ese dato a la clave pública correspondiente. Al enviar la información, el sistema envía el mismo archivo que el paciente cargó y firmó. Para enviarlo y garantizar que únicamente el médico solicitante pueda acceder a la información, el Sistema de Cifrado lleva a cabo el mismo proceso que antes:

1. Desencripta la clave simétrica con su privada RSA.
2. Desencripta la DDJJ del paciente con la clave simétrica.
3. Encripta la DDJJ con una nueva clave simétrica aleatoria.
4. Encripta la clave simétrica con la pública RSA del médico.

* **Sistema de descifrado**: este sistema es ejecutado por el médico solicitante. Mediante su clave privada, desencripta la clave simétrica para poder desencriptar los datos mediante el algoritmo AES.

## Diagrama

![Vista general](https://user-images.githubusercontent.com/19544797/102728307-e2934100-4309-11eb-84fb-b28d33ba835a.jpg)

## Implementación

Para la implementación de este sistema se separó la lógica en tres scripts:
* `1-encrypt_document.py`: Es la interfaz con el cliente, al que se le hacen preguntas sobre síntomas del COVID-19 y las respuestas junto con la firma del paciente son guardadas de manera segura por el Sistema de Cifrado.
  * **Ejecución**: `./1-encrypt-document.py -h` para ver los distintos argumentos con que se puede invocar el programa
* `2-request_document.py`: Es la interfaz con el personal médico, el mismo provee una identificación al fin de que el Sistema de Cifrado pueda determinar si está autorizado a recibir la DDJJ del paciente. En caso de estar autorizado el Sistema de Cifrado provee los datos encriptados para el médico, la firma y la clave simétrica encriptada.
  * **Ejecución**: `./2-request_document.py -h` para ver los distintos argumentos con que se puede invocar el programa
* `3-decrypt-document.py`: Representa el sistema que los médicos podrían tener instalados localmente, al cual le proveen la salida del script anterior y adicionalmente la clave privada del médico para poder desencriptar la clave simétrica que se usó para encriptar la DDJJ y la clave pública del paciente para verificar su firma.
  * **Ejecución**: `./3-decrypt-document.py -h` para ver los distintos argumentos con que se puede invocar el programa
