# Sensible Data System

## Descripción

El sistema apunta a resolver la distribución de información sensible.  
Utiliza encriptación para que la información sensible solo pueda ser accedida por personas u organismos autorizados y garantizar la confidencialidad. Adicionalmente, emplea la firma digital para poder verificar la integridad y autenticidad de la información.

## Caso de uso

En este caso tomaremos como caso la encriptación de información clínica de pacientes. Sin embargo, podría utilizarse en sistemas de distinta naturaleza (por ejemplo, declaraciones juradas de funcionarios) sin mayores cambios.

## Componentes

El sistema se divide en:

* **Cliente**: se encarga de la carga de los datos de los pacientes, los cuales son considerados sensibles. Estos datos son firmados por el paciente, para poder verificar su integridad y autenticidad.

* **Sistema de cifrado**: este sistema almacena los datos sensibles. Recibe los datos firmados por los pacientes y los encripta, para garantizar la confidencialidad. Para ello, utiliza su clave pública, de manera que el descifrado solo sea posible utilizando la clave privada del sistema.  
Este sistema acepta solicitudes de la información guardada. Para ello, valida la identidad del médico solicitante. Para realizar esta validación, se solicita la clave pública al médico solicitante y se verifica mediante una whitelist de certificados que se consideran válidos. Al enviar la información, el sistema envía el mismo archivo que el paciente cargó y firmó. Para enviarlo y garantizar que únicamente el médico solicitante pueda acceder a la información, el archivo se encripta utilizando la clave pública del médico, de manera que solo pueda desencriptarse con la clave privada.

* **Sistema de descifrado**: este sistema es ejecutado por el médico solicitante. Mediante su clave privada, desencripta el archivo solicitado y verifica la firma digital del paciente.

## Diagrama

![Vista general](https://user-images.githubusercontent.com/19544797/102728307-e2934100-4309-11eb-84fb-b28d33ba835a.jpg)

## Implementación

### Firmador digital
Primero se puede generar un archivo con "datos sensibles" firmado. Para ello se debe ejecutar el `digital_signer`:
1. Ubicado en la raíz del proyecto ejecutar `./digital_signer.sh` esto iniciará una consola bash en un contenedor de Docker.
2. Desde la consola se puede ejecutar `./generate_keys.sh` para generar las claves pública y privada RSA necesarias para la firma digital. Las mismas se verán en el host OS en `/digital_signer/keys`.
3. Ejecutar `./signer -h` para ver los comandos disponibles del firmador digital. Por ejemplo se puede ejecutar `./signer -i covid_ddjj.example.json` lo cuál generará el archivo de la firma digital en `/digital_signer/output/sign_base64`.
