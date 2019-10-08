import sys

dic = []
with open('laji/dict_en.txt', 'r') as f:
    for line in f:
        dic.append(list(line.strip('\n').split(',')))
for word in dic:
    word = ''.join(word)
    print(word)
    'abc'.startswith(word)