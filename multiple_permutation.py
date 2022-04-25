from rail_fence import encrypt_rail, dencrypt_rail
from simple_permutation_cipher import encrypt_simple, dencrypt_simple
from vertical_permutation_cipher import encrypt_vertical, dencrypt_vertical
import random
import re

def encrypt_multiple(text,choice_00):
    lst=list(range(1, 5, 1))
    random.shuffle(lst)
    for i in lst:
        if i == 4:
            i = random.randint(1, 4)
        if i==1:
            n = random.randint(1, 10)
            key = [str(i) for i in range(0, n, 1)]
            random.shuffle(key)
            key = ''.join(key)
            size=random.randint(1, 5)
            print(key, " ", size)
            text=encrypt_simple(key,text,size)
            if choice_00 == '1':
                s=text.replace('\0','')
                if '\a' in text:
                    s=s.replace('\a','')
                print(s)
            else:
                print(text)
        if i==2:
            m = str(random.randint(1, 9))
            n = random.randint(2, 9)
            k = str(n)
            help = [str(i) for i in range(0, n, 1)]
            random.shuffle(help)
            help = ''.join(help)
            key="{0}*{1} {2}".format(m,k,help)
            size = random.randint(1, 5)
            print(key, " ", size)
            text = encrypt_vertical(key, text, size)
            if choice_00 == '1':
                s = text.replace('\a', '')
                s = s.replace('\0', '')
                print(s)
            else:
                print(text)
        if i==3:
            m = random.randint(1, 10)
            n = random.randint(3, 10)
            size = random.randint(1, 5)
            print(m, " ", n, " ", size)
            text = encrypt_rail(m,n, text, size)
            if choice_00 == '1':
                s = text.replace('\0', '')
                if '\a' in text:
                    s=s.replace('\a','')
                print(s)
            else:
                print(text)
        i+=1
