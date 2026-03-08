from HMAC.HMAC import hmac
from SHA256.Constants import HASH_LENGTH
import math


def expand(output_length: int, info: str, prk: bytes):  # function for the HKDF expansion
    N = math.ceil(output_length / HASH_LENGTH)
    T = b""  # empty string for intermediate expansion results in bytes
    OKM = b""  # empty string for final result in bytes b'' formatting
    info = info.encode("utf-8")
    for i in range(1, N + 1):  # the main cycle
        T = hmac(prk, T + info + bytes([i]))  # main function using HMAC of the prk result from extract function
        OKM += T  # updating final value
    return OKM[:output_length]  # setting required output length
