#!/usr/bin/env python3
import logging
import argparse
import json
from model.asymmetric_cipher.AES_cipher import AESCipher
from model.asymmetric_cipher.RSA_cipher import RSACipher
from auxi import *

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--medic-dni", default="36716274", help="DNI of the medic")
    return parser.parse_args()

def transform_data(symmetric_encrypted_key, encrypted_data, iv, doctor_key_path):
    RSA_cipher = RSACipher()
    AES_cipher = AESCipher()

    # Desencriptamos la clave simétrica con la clave privada del Sistema de Cifrado
    # ya que la misma había sido encriptada con la pública.
    symmetric_decrypted_key = RSA_cipher.decrypt(symmetric_encrypted_key, SYSTEM_PRIVATE_KEY_PATH)

    # Desencriptamos la DDJJ con la clave simétrica y algoritmo AES
    ddjj_decrypted_data = AES_cipher.decrypt(encrypted_data, symmetric_decrypted_key, iv)

    # Volvemos a cifrar con AES y generamos una nueva clave simétrica
    encrypted_data_for_doctor, symmetric_key_for_doctor, iv = AES_cipher.encrypt(ddjj_decrypted_data)
    # En este caso la clave simétrica se encripta con la clave pública del
    # doctor, de manera que solo él pueda leer la DDJJ
    symmetric_key_for_doctor_encrypted = RSA_cipher.encrypt(symmetric_key_for_doctor, doctor_key_path)

    write_file(ENCRYPTED_DATA_FOR_DOCTOR_PATH, encrypted_data_for_doctor)
    write_file(ENCRYPTED_KEY_FOR_DOCTOR_PATH, symmetric_key_for_doctor_encrypted + iv)

def main():
    initialize_log()

    try:
        args = parse_arguments()
        f = open("doctors.json")
        keys = json.load(f)
        
        foundKey = False
        keyPath = DOCTOR_PUBLIC_KEY_PATH
        for dni_key in keys["medics"]:
            if dni_key["DNI"] == args.medic_dni:                
                keyPath += "/" + dni_key["KEY"]
                foundKey = True
                break
                
        if not foundKey:
            logging.error('Unauthorized DNI')
            return

        # TODO: el doctor debería indicar qué DDJJ y en base a alguna
        # identificación busca el correspondiente
        # archivo encriptado + clave simétrica encriptada
        # en vez de estar hardcodeado
        encrypted_data = load_file(ENCRYPTED_DATA_FOR_SYSTEM_PATH)
        symmetric_key = load_file(ENCRYPTED_KEY_FOR_SYSTEM_PATH)
        symmetric_encrypted_key = symmetric_key[:-16]
        iv = symmetric_key[-16:]

        transform_data(symmetric_encrypted_key, encrypted_data, iv, keyPath)

        logging.info('Finished step 2 - OK')
    except Exception as e:
        logging.error('Fatal error: {}'.format(e))

main()
