# Este script genera las claves pública y privada RSA y las almacena en /keys

# Generamos clave RSA privada
openssl genrsa -out keys/patient_keys/private.pem 2048
# Obtenemos la clave pública
openssl rsa -in keys/patient_keys/private.pem -outform PEM -pubout -out keys/patient_keys/public.pem

# Repetimos para el sistema y el doctor
openssl genrsa -out keys/system_keys/private.pem 2048
openssl rsa -in keys/system_keys/private.pem -outform PEM -pubout -out keys/system_keys/public.pem

openssl genrsa -out keys/doctor_keys/private.pem 2048
openssl rsa -in keys/doctor_keys/private.pem -outform PEM -pubout -out keys/doctor_keys/public.pem