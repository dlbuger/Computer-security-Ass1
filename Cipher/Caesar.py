import sys
from check import check
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

def cipher_C(message):
    for i in range(26):
        if(check(getTranslatedMessage(message,i))):
            return getTranslatedMessage(message,i).upper() +', C, -'+ str(i)
        if (check(getTranslatedMessage(message, -i))):
            return getTranslatedMessage(message, -i).upper() + ', C, ' + str(i)

def read_from_dic():
    with open('laji/dict_en.txt', 'r') as f:
        return f



