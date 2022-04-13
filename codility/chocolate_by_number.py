

def gcd(a, b):

    while b != 0:
        t = b
        b = a % b
        a = t

    return a

def chocolate_by_number(N, M):

    div = gcd(N, M)

    return N // div


if __name__ == '__main__':

    print(chocolate_by_number(10, 4))
