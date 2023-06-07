string =str(input("Введите вашу фразу:"))
key= str(input("Введите ваш ключ:"))
def XOR_cipher(string, key):
    string_bytes = string.encode()
    key_bytes = key.encode()
    encrypted = []
    for i in range(len(string_bytes)):
        encrypted.append(chr(string_bytes[i] ^ key_bytes[i % len(key_bytes)]))
    return ''.join(encrypted)
def XOR_uncipher(string, key):
    return XOR_cipher(string, key)
encrypted = XOR_cipher(string, key)
print(encrypted)
decrypted = XOR_uncipher(string,key)
print(decrypted)
