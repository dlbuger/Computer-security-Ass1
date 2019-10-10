from Caesar import cipher_C
from Modified_caesar import cipher_M
from Columnar_Transposition import cipher_T

def get_input(index):
    if(index == ''):
        index = 'laji/input.txt'
    words = []
    with open(index, 'r') as f:
        for line in f:
            words.append(list(line.strip('\n').split(',')))

    return words
def main():
    index = input('Please input index:')

    for word in get_input(index):

        tem1 = cipher_C(''.join(word))

        tem2 = cipher_T(''.join(word))
        tem3 = cipher_M(''.join(word))
        if(tem1 == None and tem2 == None and tem3 == None ):
            print(None)
        if (tem1 != None):
            print( tem1)
        if(tem2 != None):
            print( tem2)
        if(tem3 != None):
            print( tem3)
print(main())