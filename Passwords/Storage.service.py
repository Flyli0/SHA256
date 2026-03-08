from Passwords.generator import generate
from PBKDF2.PBKDF2 import pbkdf2
import json
import time

salt = generate(128)
name = input("Input your Username \n")
key = input("Insert your secret key \n")
b_key = key.encode('utf-8')


encrypted = pbkdf2(b_key, salt, 100000, len(b_key))

store = {"Username": name,
         "Salt": salt.hex(),
         "Hash": encrypted.hex()
         }

json_store = json.dumps(store, indent=4)

with open("storage.json", "a") as f:
    f.write(json_store + "\n")
