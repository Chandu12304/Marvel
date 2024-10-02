from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'mySecretPassword' #16 byte password

cipher = AES.new(key,AES.MODE_CBC)

plainText = b'this is my secret message to encrypt'

cipherText = cipher.encrypt(pad(plainText,AES.block_size))

print(cipherText)

# Automatically generated initialization vector to randomize the cipher text
print(cipher.iv)

# storing in file
with open('cipher_file','wb') as c_file:
    c_file.write(cipher.iv)
    c_file.write(cipherText)