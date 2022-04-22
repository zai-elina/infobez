import numpy as np
key=input()
text=input()

def encrypt(key, text,size):
    m = int(key[0])
    k = int(key[2])
    key = list(key[4:])
    text = [text[i:i + size] for i in range(0, len(text), size)]
    for i in range(len(text)):
        if len(text[i]) != size:
            text[i] += '\f'
    while (len(text) % (m*k) != 0):
        text.append('\f' * size)

    i = 0
    encrypted_text=""
    while i<len(text):
        matrix = np.array(list(text[i:(m*k+i)]))
        matrix = matrix.reshape(m,k)
        help= np.copy(matrix)
        for j in range(len(key)):
            help[:,int(key[j])] = matrix[:,j]
        encrypted_text += ''.join(list(np.concatenate(help.T)))
        i += m*k
    return encrypted_text

def dencrypt(key, text,size):
    m = int(key[0])
    k = int(key[2])
    key = list(key[4:])
    text = [text[i:i + size] for i in range(0, len(text), size)]

    i = 0
    dencrypted_text=""
    while i<len(text):
        matrix = np.array(list(text[i:(m*k+i)]))
        matrix = matrix.reshape(k,m)
        matrix =matrix.T
        help= np.copy(matrix)
        for j in range(len(key)):
            help[:,j] = matrix[:,int(key[j])]
        dencrypted_text += ''.join(list(np.concatenate(help)))
        i += m*k

    return dencrypted_text


new_text=encrypt(key,text,1)
print(new_text)
print(dencrypt(key,new_text,1))