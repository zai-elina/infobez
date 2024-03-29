
def add_0(text,size,key):
    for i in range(len(text)):
        if len(text[i]) != size:
            text[i] += '\0'
    while (len(text) % len(key) != 0):
        text.append('\0' * size)
    return text

def encrypt_simple(key, text, size):
    text = [text[i:i + size] for i in range(0, len(text), size)]
    text = add_0(text,size,key)
    i=0
    encrypted_text=""
    while i<len(text):
        help=[0]*len(key)  # заносится зашифрованный блок, временно заносим в него перемещенные символы
        for j in range(len(key)):
            help[int(key[j])] = text[i + j]
        for k in help:
            encrypted_text += k
        i+=len(key)
    # encrypted_text=encrypted_text.replace('\0','')
    return encrypted_text

def dencrypt_simple(key,text,size):
    text = [text[i:i + size] for i in range(0, len(text), size)]
    text = add_0(text,size,key)
    i=0
    dencrypted_text=""
    while i<len(text):
        help=[0]*len(key)  #заносим элементы в расшифрованном состоянии
        for j in range(len(key)):
            help[j] = text[i + int(key[j])]  #по ключу востанавливаем порядок
        for k in help:
            dencrypted_text += k
        i+=len(key)
    # dencrypted_text = dencrypted_text.replace('\0', '')
    return dencrypted_text

