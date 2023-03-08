#Please install the "cryptography" module
from cryptography.fernet import Fernet
 
'''
#Making a function to create a key.key file where the key is, call it and then comment all of it out to just have one key
def writeKey():
  key = Fernet.generate_key()
  with open("key.key", "wb") as keyFile:
    keyFile.write(key)
writeKey()'''

def loadKey():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key

#Encryption initialisation
key = loadKey()
fer = Fernet(key)

#Function to view the passwords
def view():
  with open("passwords.txt", "r") as file:
    for line in file.readlines():
      data = line.rstrip()
      user, pwd = data.split(":")
      print("User:" , user , ", Password:" , fer.decrypt(pwd.encode()).decode())

#Function to add passwords
def add():
  name = input("Account Name: ")
  password = input("Password: ")

  with open("passwords.txt", "a") as file:
    file.write(name + ":" + fer.encrypt(password.encode()).decode() + "\n")

while True:
  print("Would you like to add or view your passwords?")
  mode = input('Type "add", "view" or "q" to quit: ').lower()
  if mode == "q":
    break
  
  if mode == "view":
    view()
  elif mode == "add":
    add()
  else:
    print("Invalide mode")
    continue

#Fernet cryptography module docs: https://cryptography.io/en/latest/fernet/