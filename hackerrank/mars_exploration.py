

def mars_exploration(s):

    s_list = list('SOS') * len(s)
    s_pair = zip(s_list, s)
    counter = 0
    for i, j in s_pair:
        if i != j:
            counter +=1

    return counter


if __name__ == '__main__':
    txt = 'SOSTOT'
    print(mars_exploration(txt))
