
# Euclidean Algorithm

def gcd(a, b):

    while b != 0:
        t = b
        b = a % b
        a = t

    return a


    # if a == 0:
    #     return b

    # return gcd(b % a, a)


if __name__ == '__main__':

    print(gcd(252, 105))
