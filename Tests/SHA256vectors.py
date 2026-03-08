from SHA256.SecureHashingAlgorithm import sha_256

correct = {"abc": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
           "": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
           "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq": "248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1"
           }

for it in correct.items():
    key = it[0].encode('utf-8')
    if sha_256(key).hex() == it[1]:
        print("CORRECT")
