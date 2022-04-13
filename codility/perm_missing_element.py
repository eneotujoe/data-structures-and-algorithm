

def perm_missing_element(A):

    sum_N = (len(A) + 1) * (len(A) + 2) // 2
    sum_A = sum(A)
    missing_num = sum_N - sum_A

    return missing_num

if __name__ == '__main__':
    arr = [2, 3, 1, 5]
    print(perm_missing_element(arr))
