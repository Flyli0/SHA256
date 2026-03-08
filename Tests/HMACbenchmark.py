from HMAC.HMAC import hmac
from Passwords.generator import generate
import time

passwords = [generate(128) for password in range(10)]
message = [generate(128) for salt in range(10)]

start = time.perf_counter()
for i in range(10):
    hmac(passwords[i], message[i])
end = time.perf_counter()

print(f"time taken on average: {(end-start)/10}")
