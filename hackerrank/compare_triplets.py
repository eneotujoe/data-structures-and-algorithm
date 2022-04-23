
def compare_triplets(a, b):
    alice = bob = 0
    
    for x, y in zip(a, b):
        # print(a, b)
        if x > y:
            alice += 1
        elif x < y:
            bob += 1

    return alice, bob




if __name__ == '__main__':

    a = [1, 2, 3]
    b = [3, 2, 1]

    print(compare_triplets(a, b))
