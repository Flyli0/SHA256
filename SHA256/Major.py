def maj(x, y, z):
    major = (x & y) ^ (x & z) ^ (y & z)
    return major 
