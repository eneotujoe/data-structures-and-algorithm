def task_1(message, K):
    message = message.split(' ')
    output = []
    n = 0
    for i, c in enumerate(message):
        n = len(message[i])
        if n < K:
            output.append(c)

    print(*output)







if __name__ == '__main__':
    message = 'Converts the first character to upper case'

    print(task_1(message, 8))
