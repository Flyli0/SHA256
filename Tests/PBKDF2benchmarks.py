from Passwords.generator import generate
from PBKDF2.PBKDF2 import pbkdf2
import time

passwords = [generate(128) for password in range(10)]
salts = [generate(128) for salt in range(10)]

start = time.perf_counter()
for i in range(10):
    print(f"------------------------------------PASSWORD {i} --------------------------------------------------")
    encrypted = pbkdf2(passwords[i],salts[i],100000,len(passwords[i]))
end = time.perf_counter()

print(f"Average time for 10 runs : {(end-start)/10}")