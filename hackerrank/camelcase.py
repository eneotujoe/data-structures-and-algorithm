

from curses.ascii import isupper


def camelcase(s):

    s_list = list(s)
    word_count = len(list(filter(lambda x: x.isupper(), s_list))) + 1
    
    return word_count


if __name__ == '__main__':
    txt = 'saveChangesInTheEditor'
    print(camelcase(txt))
