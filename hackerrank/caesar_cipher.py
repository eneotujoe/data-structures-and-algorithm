

def caesar_cipher(s, k):

    s_list = list(s)
    for i, char in enumerate(s):
        char = s_list[i]

        if char.isalpha():
            if (char.isupper()):
                s_list[i] = chr((ord(char) + k-65) % 26 + 65)
            else:
               s_list[i] = chr((ord(char) + k - 97) % 26 + 97)

    return ''.join(s_list)


if __name__ == '__main__':
    txt = 'middle-Outz'
    print(caesar_cipher(txt,2))
