
def XOR_cipher(string, key):
    # преобразуем строку и ключ в байтовые строки
    string_bytes = string.encode()
    key_bytes = key.encode()
    
    # создаем список для хранения зашифрованных символов
    encrypted = []
    
    # применяем операцию XOR к каждому байту строки и ключа
    for i in range(len(string_bytes)):
        # используем оператор ^ для выполнения операции XOR
        # и преобразуем результат в символ с помощью функции chr
        encrypted.append(chr(string_bytes[i] ^ key_bytes[i % len(key_bytes)]))
    
    # объединяем зашифрованные символы в строку и возвращаем ее
    return ''.join(encrypted)
def XOR_uncipher(string, key):
    # вызываем функцию XOR_cipher с зашифрованной строкой и ключом
    # для получения исходной строки
    return XOR_cipher(string, key)
string = "Hello, world!"
key = "secret"

encrypted = XOR_cipher(string, key)
print(encrypted)
