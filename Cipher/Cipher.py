import sys
def getTranslatedMessage(message, key):
     translated = ''

     for symbol in message:

         if symbol.isalpha():

             num = ord(symbol)

             num += key



             if symbol.isupper():

                 if num > ord('Z'):

                     num -= 26

                 elif num < ord('A'):

                     num += 26

             elif symbol.islower():

                 if num > ord('z'):

                     num -= 26

                 elif num < ord('a'):

                     num += 26



             translated += chr(num)

         else:

             translated += symbol

     return translated

def cipher(message):
    for i in range(26):
        if(check(getTranslatedMessage(message,i))):
            return getTranslatedMessage(message,i).upper() +', C, -'+ str(i)
        if (check(getTranslatedMessage(message, -i))):
            return getTranslatedMessage(message, -i).upper() + ', C, ' + str(i)

def read_from_dic():
    with open('laji/dict_en.txt', 'r') as f:
        return f
def check(message):
    dic = []
    with open('laji/dict_en.txt', 'r') as f:
        for line in f:
            dic.append(list(line.strip('\n').split(',')))
    new_message = message.replace(' ','').lower()
    # print('low:'+new_message)
    while(1):
        if(new_message == ''):
            return 1
        flag = 0
        for i in range(len(dic)):
            word = dic[len(dic)-i-1]
            word = ''.join(word)
            if(new_message.startswith(word)):
                new_message = new_message[len(word):]
                # print(new_message)
                flag = 1
        if(flag == 0):
            return 0

print(cipher('dghtx dwhsu rwhfw lrq'))
