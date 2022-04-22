m=int(input())
n=int(input())
text=input()

def add_0(n,text,size):
    for i in range(len(text)):
        if len(text[i]) != size:
            text[i] += '\0'
    while (len(text) % n != 0):
        text.append('\0'*size)
    return text

def encrypt(m,n, text,size):
    text = [text[i:i + size] for i in range(0, len(text), size)]
    text = add_0(n,text,size)
    matrix=[['']*n for i in range(m)]
    i=0
    j=0
    counter=-1
    for k in range(len(text)):
        matrix[i][j]=text[k]
        j+=1
        if i==0 or i==m-1:
            counter *= -1
        i+=counter
    cipher=""
    for i in range(m):
        for j in range(n):
            if matrix[i][j] !='':
                cipher += matrix[i][j]
    return cipher

def dencrypt(m,n, text,size):
    text = [text[i:i + size] for i in range(0, len(text), size)]
    text = add_0(n,text,size)
    matrix = [[''] * n for i in range(m)]
    i=0
    j=0
    counter=-1
    for k in range(len(text)):
        matrix[i][j]= '\0'
        j+=1
        if i==0 or i==m-1:
            counter *=-1
        i+=counter
    text_counter=0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '\0':
                matrix[i][j] = text[text_counter]
                text_counter+=1
    i = 0
    j = 0
    counter = -1
    cipher = ""
    for k in range(len(text)):
        cipher += matrix[i][j]
        j += 1
        if i == 0 or i == m - 1:
            counter *= -1
        i += counter
    return cipher


a=encrypt(m,n,text,1)
print(a)
print(dencrypt(m,n,a,1))