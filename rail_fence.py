
def add_0(n,text,size):
    for i in range(len(text)):
        if len(text[i]) != size:
            text[i] += '\0'
    while (len(text) % n != 0):
        text.append('\0'*size)
    return text

def encrypt_rail(m,n, text,size):
    text = [text[i:i + size] for i in range(0, len(text), size)]
    text = add_0(n,text,size)
    matrix=[['']*n for i in range(m)]

    cipher = ""
    for t in range(n-1,len(text)+1,n):
        i = 0
        j = 0
        counter = -1
        for k in range(t+1):
            if j==n or i==m:
                break
            if t==n-1:
                matrix[i][j] = text[k]
            else:
                matrix[i][j] = text[k+t-n+1]
            j+=1
            if i==0 or i==m-1:
                counter *= -1
            i+=counter
        for i in range(m):
            for j in range(n):
                if matrix[i][j] !='':
                    cipher += matrix[i][j]

    return cipher

def dencrypt_rail(m,n, text,size):
    text = [text[i:i + size] for i in range(0, len(text), size)]
    text = add_0(n,text,size)
    matrix = [[''] * n for i in range(m)]

    text_counter=0
    cipher = ""
    for t in range(n-1, len(text)+1, n-1):
        i = 0
        j = 0
        counter = -1
        for k in range(t+1):
            if j == n or i == m:
                break
            matrix[i][j]= '\0'
            j+=1
            if i==0 or i==m-1:
                counter *=-1
            i+=counter

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '\0' and text_counter!=len(text):
                    matrix[i][j] = text[text_counter]
                    text_counter+=1
        i = 0
        j = 0
        counter = -1
        for k in range(n):
            cipher += matrix[i][j]
            j += 1
            if i == 0 or i == m - 1:
                counter *= -1
            i += counter

    return cipher
