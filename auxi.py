import logging

# Keys
PATIENT_PRIVATE_KEY_PATH = "keys/patient_keys/private.pem"
PATIENT_PUBLIC_KEY_PATH = "keys/patient_keys/public.pem"
SYSTEM_PUBLIC_KEY_PATH = "keys/system_keys/public.pem"
SYSTEM_PRIVATE_KEY_PATH = "keys/system_keys/private.pem"
DOCTOR_PRIVATE_KEY_PATH = "keys/doctor_keys/private.pem"
DOCTOR_PUBLIC_KEY_PATH = "keys/doctor_keys"

# First process (create and encrypt document)
SIGNATURE_PATH = "output/1-encrypt/signature"
ENCRYPTED_KEY_FOR_SYSTEM_PATH = "output/1-encrypt/encrypted_key"
ENCRYPTED_DATA_FOR_SYSTEM_PATH = "output/1-encrypt/encrypted_data"

# Seconds process (decrypt, encrypt and send document to doctor)
ENCRYPTED_KEY_FOR_DOCTOR_PATH = "output/2-to_doctor/encrypted_key"
ENCRYPTED_DATA_FOR_DOCTOR_PATH = "output/2-to_doctor/encrypted_data"

# Third process (decrypt document for doctor)
DECRYPTED_DDJJ_PATH = "output/3-decrypt/decrypted_ddjj.json"

def load_file(path):
  with open(path, "rb") as data_file:
    return data_file.read()

def write_file(path, data):
  with open(path, "wb") as data_file:
    data_file.write(data)

def initialize_log():
	logging.basicConfig(
		format='%(asctime)s %(levelname)-8s %(message)s',
		level=logging.INFO,
		datefmt='%Y-%m-%d %H:%M:%S',
	)
