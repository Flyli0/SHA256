from HMAC.HMAC import hmac


def extract(salt:bytes, key:bytes):  # function of HKDF extract
    prk = hmac(salt,key)  # it is just hmac of salt as a key and key as a text
    return prk
