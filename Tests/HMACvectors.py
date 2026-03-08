from HMAC.HMAC import hmac


key = "0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b"
data = "Hi There"
correct = "b0344c61d8db38535ca8afceaf0bf12b881dc200c9833da726e9376c2e32cff7"
data = data.encode('utf-8')
correct = bytes.fromhex(correct)
key = bytes.fromhex(key)
res = hmac(key, data)
if res.hex() == correct.hex():
    print("CORRECT!")
