"""
Author:JiaxiChen
"""

c1 = "0101001010000111000110011001010100010100100100110001010001000111110111100011010001111111001101100111001011010110101100000101100100001101111111111011010001110011111001101100001010110000111100001101100101010010110110000111000100110100111110010011011000100101111100110110000111001100111111101100011010111011100101110000101111001100001001000101100001001011100101100001001010000111111001010001001101101100110000111110000001100110100111010100000110101011111011010010111101111010110001100100011101110111101110111011110010110011010000111010111100001111101000100000001010000110"
c2 = "0111001100110011110100101010111011100111101011101000111111101110110000011001001011010001010101011010000111000000110001010101011001110010000000000011010001110000011111110010100000110111010100110001110110100001101011111010100111001100110110000111011110011101110000101100000001010010101111011000110000101011111111010110010100010000001110110010001010000001100011000111010011111110010100100011010010110011101111010001111101111000001011110110110111010100101101010001101010111011010011011010100100110011011010010010100101001011110111101011011010101001011001110101010101000110"
c3 = "0010001110000001000110011001011100010011110001100001000101001100100110100010100001010101001000110110010111010111111111110001011000010111101001001011010001101010111011111100111011111110101011001100011101010011100011000000010100010100111110000111000100100000101100000011001110001111110101011111010011111100100000000001010111001000011001010111111001000100100010010100100011011100111011110001101000111001100110011111001001110001110110100100101111111001111100000111010000110010100101000101100000110010101101111011101011100111000001111111101001000111111010110001000111010101"
c4 = "0000111100100011100111111111110010111100111010111101111011111100100000111101110111000010000111011111010110010010100100000100111000100100010111010111000001100111001110000111011001110100010100110101101011110110101111001111111010001101100110000110101010011101101100011000000000010001101111011101011101111100111111010010001001001111011111100011001111010100110110110011000011100001010000110110111011100111101011000100101000110111011111000010101110001001101100100101110010101011000100011110011001110110001101010011000100011110100010001110001011101000001101110001010101011001"


def axorb(a, b):
    tempText = []
    for x, y in zip(a, b):
        tempText.append(int(x) ^ int(y))
    return "".join(map(lambda x: str(x), tempText))


# Press the green button in the gutter to run the script.
def binToAscii(message):
    return ''.join(chr(int(message[i * 8: i * 8 + 8], 2)) for i in range(len(message) // 8))


def xorAllMessage(messageList):
    messageXor = []
    for i in range(3):
        for j in range(i + 1, 4):
            zeroHead = True
            readyCheck = binToAscii(axorb(messageList[i], messageList[j]))
            for k in readyCheck:
                if ord(k) < 127:
                    continue
                else:
                    zeroHead = False
                    break
            if zeroHead == True:
                print("{} and {} are padded with same key".format(i + 1, j + 1))
                messageXor.append(readyCheck)
    return messageXor


def guessMessage(guess, message):
    messagelen = len(message)
    guesslen = len(guess)
    for i in range(messagelen - guesslen + 1):
        tempmessage = ""
        for j in range(guesslen):
            checkzero = chr(ord(message[i + j]) ^ ord(guess[j]))
            tempmessage += checkzero
        print("Position {} to {}: {}".format(i + 1, i + guesslen, tempmessage))


if __name__ == '__main__':
    messageList = []
    messageList.append(c1)
    messageList.append(c2)
    messageList.append(c3)
    messageList.append(c4)
    mxormList = xorAllMessage(messageList)
    while True:
        messageChoose = input("1: First pair 2: Second Pair Jiaxi: quit\n")
        if len(messageChoose) == 1 and (1 <= int(messageChoose) <= 2) :
            message = mxormList[int(messageChoose) - 1]
        elif messageChoose == "Jiaxi":
            break
        else:
            print("invalid, try again!")
            continue
        while True:
            userInput = input("Enter a message to guess, 'Jiaxi' to ChooseMessage:  ")
            if userInput == 'Jiaxi':
                break
            else:
                guessMessage(userInput, message)
