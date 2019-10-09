import math
from check import check
def decryptMessage(message, key):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list

    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = math.ceil(len(message) / key)

    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1  # point to next column

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)
def cipher_T(message):
    new_line = [''] * len(message)
    for i in range(len(message)):
        if(message[i] == ' '):

            new_line[i] = ' '

    for i in range(1, len(message)+1):
        new_message = decryptMessage(message.lower().replace(' ',''), i)
        # print(new_message)
        if(check(new_message)):

            k = 0
            for j in range(len(new_line)):
                if(new_line[j] == ' '):
                    continue
                else:
                    # print(new_line)
                    new_line[j] = new_message[k]
                    k += 1
            # print(new_line)
            return ''.join(new_line).upper() + ', T, '+ str(i)



print(cipher_T('saupw nrsed cesht oi'))