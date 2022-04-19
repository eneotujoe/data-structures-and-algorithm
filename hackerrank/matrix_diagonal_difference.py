
def matrix_diagonal_difference(arr):
    n = len(arr)
    prim_diag_sum = 0
    sec_diag_sum = 0
    for i in range(n):
        for j in range(n):
            if i==j:
                prim_diag_sum += arr[i][j]
            if (i+j) == (n-1):
                sec_diag_sum += arr[i][j]

    return abs(prim_diag_sum - sec_diag_sum)






if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    print(matrix_diagonal_difference(arr))
