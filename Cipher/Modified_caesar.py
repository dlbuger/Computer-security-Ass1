from check import check
def get_words():
    words = []
    with open('laji/words.txt', 'r') as f:
        for line in f:
            words.append(list(line.strip('\n').split(',')))

    return words

def cipher_M(message):
    pass

def left_rightloop(s, n):                          #left positive right negative
    if len(s) == 0:
        return ''
    move = s[0:n]
    residue = s[n:]
    return ''.join([residue, move])



def get_modeifed_caesar(message,key,word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a = word.lower().replace(' ', '') + 'abcdefghijklmnopqrstuvwxyz'
    rainbow = ""
    for i in a:
        if i not in rainbow:
            rainbow += i
    # print(rainbow)
    new_string = left_rightloop(rainbow, key)
    # print(new_string)
    new_message = ''
    for w in message:
        if (w == ' '):
            new_message += ' '
            continue
        for i in range(len(new_string)):
            if(new_string[i] == w.lower()):
                new_message += alphabet[i]
    return new_message.upper()

def cipher_M(message):
    words = get_words()
    for word in words:
        for i in range(26):
            a = get_modeifed_caesar(message,i , ''.join(word))
            if(check(a)):
                return a + ', M, ' + ''.join(word) +', '+str(i)

    return None
print(cipher_M('etwje wxrepdfhfg exutx jqp'))
