from PBKDF2.PBKDF2 import pbkdf2

password = b"password"
salt = b"salt"

res = pbkdf2(password, salt, 1, 20)
print(res.hex())
