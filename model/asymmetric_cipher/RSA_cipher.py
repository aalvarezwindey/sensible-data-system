from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import logging

class RSACipher:
  def encrypt(self, data, public_key_path):
    public_key = self._load_public_key(public_key_path)
    return public_key.encrypt(
      data,
      padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
        )
      )

  def decrypt(self, ciphertext, private_key_path):
    private_key = self._load_private_key(private_key_path)
    return private_key.decrypt(
      ciphertext,
      padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
        )
      )

  def _load_public_key(self, path):
    with open(path, "rb") as key_file:
      return serialization.load_pem_public_key(key_file.read())

  def _load_private_key(self, path, password=None):
    with open(path, "rb") as key_file:
      return serialization.load_pem_private_key(key_file.read(), password=password)
