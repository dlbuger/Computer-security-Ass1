def check(message):
    dic = []
    with open('laji/dict_en.txt', 'r') as f:
        for line in f:
            dic.append(list(line.strip('\n').split(',')))
    new_message = message.replace(' ','').lower()

    while(1):
        if(new_message == ''):
            return 1
        flag = 0
        for i in range(len(dic)):
            word = dic[len(dic)-i-1]
            word = ''.join(word)
            if(new_message.startswith(word)):
                new_message = new_message[len(word):]
                #print(new_message)
                flag = 1
        if(flag == 0):
            return 0
