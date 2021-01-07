t=int(input()) 
n=int(input())
s=input()

# Alphabets from a to p are encoded using 4 bit binary digits. The program aims at decoding the encoded key to retrieve the hidden message.

reference = {
    key: val for key, val in zip(
        [bin(num).replace('0b', '').rjust(4, '0') for num in range(16)],
        'abcdefghijklmnop',
    )}

def decoder(n,s):
    i=0
    sliced_string=[]
    while i in range(0,n):
        k=s[i:i+4]
        i=i+4
        sliced_string.append(k)
    listToStr = ''.join([reference[j] for j in sliced_string])
    print(listToStr)

if __name__=='__main__':
    decoder(n,s)

