# Este script genera las claves pública y privada RSA y las almacena en /keys

# Generamos clave RSA privada
openssl genrsa -out keys/patient_private_key.pem 2048

# Obtenemos la clave pública del paciente
openssl rsa -in keys/patient_private_key.pem -outform PEM -pubout -out keys/patient_public_key.pem