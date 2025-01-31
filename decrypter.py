import os
import pyaes

##Abre arquvio criptografado

file_name = input("Digite o nome do arquivo a ser descriptografado: ")
#Verifica se o arquivo existe
if not os.path.exists(file_name):
    file_name="teste.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

##Chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

##Descriptografa conteudo
decrypt_data = aes.decrypt(file_data)

##Remove o arquivo criptografado
os.remove(file_name)

##Cria arquivo descriptografado
new_file_name = file_name.replace(".ransomwaretroll", "")
new_file =new_file_name
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()

