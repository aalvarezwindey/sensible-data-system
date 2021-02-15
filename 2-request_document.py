#!/usr/bin/env python3
import logging
import argparse
import tempfile
from model.covid_survey.covid_survey import CovidSurvey
from model.digital_signer.digital_signer import DigitalSigner
from model.asymmetric_cipher.AES_cipher import AESCipher
from model.asymmetric_cipher.RSA_cipher import RSACipher
from auxi import *

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--doctor-public-key", default=DOCTOR_PUBLIC_KEY_PATH, help="private key path to sign the data")
    return parser.parse_args()

def transform_data(encrypted_key, encrypted_data, iv, doctor_key_path):
    RSA_cipher = RSACipher()
    AES_cipher = AESCipher()

    sys_decrypted_key = RSA_cipher.decrypt(encrypted_key, SYSTEM_PRIVATE_KEY_PATH)
    sys_decrypted_data = AES_cipher.decrypt(encrypted_data, sys_decrypted_key, iv)

    sys_encrypted_data, key, iv = AES_cipher.encrypt(sys_decrypted_data)
    sys_encrypted_key = RSA_cipher.encrypt(key, doctor_key_path)

    write_file(ENCRYPTED_DATA_FOR_DOCTOR_PATH, sys_encrypted_data)
    write_file(ENCRYPTED_KEY_FOR_DOCTOR_PATH, sys_encrypted_key+iv)
    
def main():
    initialize_log()

    try:
        args = parse_arguments()
        encrypted_data = load_file(ENCRYPTED_DATA_FOR_SYSTEM_PATH)
        symmetric_key = load_file(ENCRYPTED_KEY_FOR_SYSTEM_PATH)
        encrypted_key = symmetric_key[:-16]
        iv = symmetric_key[-16:]

        transform_data(encrypted_key, encrypted_data, iv, args.doctor_public_key)

        logging.info('Finished step 2 - OK')
    except Exception as e:
    
        logging.error('Fatal error: {}'.format(e))

main()
