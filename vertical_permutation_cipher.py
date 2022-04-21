import numpy as np
key=input()
text=input()

def encrypt(key, text):
    m = int(key[0])
    k = int(key[2])
    key=list(key[4:])

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


print(encrypt(key,text))