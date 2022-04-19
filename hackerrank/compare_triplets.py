
def compare_triplets(a, b):
    total_a_point = 0
    total_b_point = 0
    
    for a, b in zip(a, b):
        # print(a, b)
        if a > b:
            total_a_point += 1
        if a < b:
            total_b_point += 1

    return total_a_point, total_b_point




if __name__ == '__main__':

    a = [1, 2, 3]
    b = [3, 2, 1]

    print(compare_triplets(a, b))
