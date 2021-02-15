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

  parser.add_argument("-p", "--patient-private-key", default=PATIENT_PRIVATE_KEY_PATH, help="private key path to sign the data")
  parser.add_argument("-s", "--system-public-key", default=SYSTEM_PUBLIC_KEY_PATH, help="private key path to encrypt the data")
  parser.add_argument("-i", "--input", help="input data json file path to be signed, if not set the survey will be asked")
  parser.add_argument("-o", "--output", default=SIGNATURE_PATH, help="output path for the digital sign")

  return parser.parse_args()

def sign_data(data, private_key_path, output_path):
  DigitalSigner().sign(
      private_key_path=private_key_path,
      data=data,
      output_path=output_path
    )

def encrypt_data(data, private_key_path):
  RSA_cipher = RSACipher()
  AES_cipher = AESCipher()
  encrypted_data, key, iv = AES_cipher.encrypt(data)
  encrypted_key = RSA_cipher.encrypt(key, private_key_path)

  write_file(ENCRYPTED_DATA_FOR_SYSTEM_PATH, encrypted_data)
  write_file(ENCRYPTED_KEY_FOR_SYSTEM_PATH, encrypted_key+iv)

def main():
  initialize_log()

  try:
    args = parse_arguments()
    if not args.input:
      data = CovidSurvey().run()
    else:
      data = load_file(args.input)

    sign_data(data, args.patient_private_key, args.output)
    encrypt_data(data, args.system_public_key)

    logging.info('Finished step 1 - OK')
  except Exception as e:
    logging.error('Fatal error: {}'.format(e))

main()
