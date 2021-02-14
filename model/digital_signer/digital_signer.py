import OpenSSL
from OpenSSL import crypto
import base64
import logging

class DigitalSigner:
  def __init__(self):
    pass

  def sign(self, private_key_path, data, output_path):
    logging.debug('private_key_path {}'.format(private_key_path))
    logging.debug('output_path {}'.format(output_path))

    with open(private_key_path, "rb") as private_key_file:
      key = private_key_file.read()
      logging.debug('key readed \n{}\n'.format(key))
      pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)
      logging.debug('pkey loaded\n{}\n'.format(pkey))

      data_bytes = data
      signed_data = OpenSSL.crypto.sign(pkey, data_bytes, "sha256")
      logging.debug('signed_data\n{}'.format(signed_data))
      encoded_signed = base64.b64encode(signed_data)
      logging.debug('encoded_signed\n{}'.format(encoded_signed))

      with open(output_path, "w") as output_file:
        output_file.write(encoded_signed.decode('utf-8'))

  def verify_sign(self, public_key_path, data_path, base64_sign_path):
    logging.debug('public_key_path {}'.format(public_key_path))
    logging.debug('data_path {}'.format(data_path))

    with open(public_key_path, "rb") as public_key_file:
      key = public_key_file.read()
      logging.debug('key readed \n{}\n'.format(key))
      pkey = crypto.load_publickey(crypto.FILETYPE_PEM, key)
      logging.debug('pkey loaded\n{}\n'.format(pkey))

      with open(base64_sign_path, "r") as base64_sign_file:
        sign = base64.b64decode(base64_sign_file.read())
        logging.debug('sign decoded\n{}'.format(sign))

        with open(data_path) as data_file:
          data = data_file.read()
          logging.debug('data loaded\n{}'.format(data))
          data_bytes = bytes(data, encoding='utf-8')
          certificate_x509 = OpenSSL.crypto.X509()
          certificate_x509.set_pubkey(pkey)
          OpenSSL.crypto.verify(certificate_x509, sign, data_bytes, "sha256")
