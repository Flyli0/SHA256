from Passwords.RandomBytes import random_bytes


def generate(size_bits):  # using our generator create keys of different size
    size_bytes = size_bits // 8
    key = random_bytes(size_bytes)
    return key  # hexadecimal representation
