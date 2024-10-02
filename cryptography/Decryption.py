from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'mySecretPassword'

with open('cipher_file','rb') as c_file:
    iv = c_file.read(16)
    cipherText = c_file.read()

cipher = AES.new(key,AES.MODE_CBC, iv)

plainText = unpad(cipher.decrypt(cipherText),AES.block_size)

print(plainText) # in byte format
print(plainText.decode()) # message which was encrypted