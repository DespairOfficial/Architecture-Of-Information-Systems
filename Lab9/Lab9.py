# [65;90]
# [97;122]
#[128;159]
#[160-175;224-239]
import os
text = []
encodedText = []
decodedText = []
key = -1
text = input("Enter some text: ")
key = input('Enter the key: ')
key = int(key)
with open('key.txt', 'r') as f:
    f.read()
with open('key.txt', 'w') as f:
    f.write(str(key))
for i in text:
    if(ord(i)>= 65 and ord(i)<=90):
        i = (ord(i)+ key%26) 
        if(i>90):
            i= (i  - 26)
        encodedText.append(chr(i))
    elif(ord(i)>= 97 and ord(i)<=122):
        i = (ord(i)+ key%26) 
        if(i>122):
            i= (i  - 26)
        encodedText.append(chr(i))
    else:
        encodedText.append(i)
print(''.join(encodedText))

os.system('CLS')
print(''.join(encodedText))
keyNotEntered = True
while(keyNotEntered):
    tryKey = input("Enter key: ")
    tryKey = int(tryKey)
    if(key == tryKey):
        keyNotEntered = False
        for i in encodedText:
            if(ord(i)>= 65 and ord(i)<=90):
                i = (ord(i)- key%26) 
                if(i<65):
                    i= (i + 26)
                decodedText.append(chr(i))
            elif(ord(i)>= 97 and ord(i)<=122):
                i = (ord(i) - key%26) 
                if(i<97):
                    i= (i  + 26)
                decodedText.append(chr(i))
            else:
                decodedText.append(i)
    else:
        print('That is not the key, try again: ')
print(''.join(decodedText))
