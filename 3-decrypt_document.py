#!/usr/bin/env python3

import logging
import argparse
from model.digital_signer.digital_signer import DigitalSigner
from model.asymmetric_cipher.AES_cipher import AESCipher
from model.asymmetric_cipher.RSA_cipher import RSACipher
from aux import *

def parse_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument("-k", "--key", default=ENCRYPTED_KEY_FOR_DOCTOR_PATH, help="encrypted symmetric key (file path)")
  parser.add_argument("-d", "--data", default=ENCRYPTED_DATA_FOR_DOCTOR_PATH, help="encrypted data (file path)")
  parser.add_argument("-s", "--signature", default=SIGNATURE_PATH, help="digital signature for the data (file path)")
  parser.add_argument("-p", "--patient-key", default=PATIENT_PUBLIC_KEY_PATH, help="patient public key (file path)")
  parser.add_argument("-m", "--medic-key", default=DOCTOR_PRIVATE_KEY_PATH, help="doctor private key (file path)")
  parser.add_argument("-o", "--output", default=DECRYPTED_DDJJ_PATH, help="output for decrypted data (file path)")
  return parser.parse_args()

def decrypt_data(encrypted_key, encrypted_data, iv, doctor_key_path, output_path):
    RSA_cipher = RSACipher()
    AES_cipher = AESCipher()

    decrypted_key = RSA_cipher.decrypt(encrypted_key, doctor_key_path)
    decrypted_data = AES_cipher.decrypt(encrypted_data, decrypted_key, iv)
    write_file(output_path, decrypted_data)

def verify_signature(patient_key, output, signature):
  DigitalSigner().verify_sign(
      public_key_path=patient_key,
      data_path=output,
      base64_sign_path=signature
    )

def main():
  initialize_log()

  try:
    args = parse_arguments()
    encrypted_data = load_file(args.data)
    symmetric_key = load_file(args.key)
    encrypted_key = symmetric_key[:-16]
    iv = symmetric_key[-16:]

    decrypt_data(encrypted_key, encrypted_data, iv, args.medic_key, args.output)
    verify_signature(args.patient_key, args.output, args.signature)

    logging.info('Finished step 3 - OK')
  except Exception as e:
    logging.error('Fatal error: {}'.format(e))

main()
