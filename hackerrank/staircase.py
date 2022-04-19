def staircase(n):
    step = [' '* (n-i) + '#'*i for i in range(1, n+1)]       

    print(*step, sep='\n')


if __name__ == '__main__':
    print(staircase(6))
