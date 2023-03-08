# Passwords manager

## !!!WARNING!!! DO NOT USE IT AS AN ACTUAL PASSWORDS MANAGER! IT IS ONLY AN EXERCICE TO LEARN A BIT ABOUT ENCRYPTION AND DECRYPTION THEREFORE IT IS NOT 100% SAFE
But you can still use it to check out the code and play around with it.

Quick notes:
- To use this program, please install the "cryptography" module ("pip install cryptography" in the terminal)
- In order to create the key.key file, I created a function, called it and then comment all of this out to only have one key and not have errors.
- If you want to have your own key:
  - Delete the key.key file
  - Delete the comments quotation marks in the main.py code around lines 4 to 10
  - Run the program (a key.key file should be created)
  - Put back the comments quotation marks like so:

`
'''
def writeKey():
  key = Fernet.generate_key()
  with open("key.key", "wb") as keyFile:
    keyFile.write(key)
writeKey()'''
`
