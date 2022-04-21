

def mars_exploration(s):

    sos_message = list('SOS') * len(s)
    message_pair = zip(sos_message, s)
    counter = 0
    for i, j in message_pair:
        if i != j:
            counter +=1

    return counter


if __name__ == '__main__':
    txt = 'SOSTOT'
    print(mars_exploration(txt))
