
def max_product_of_three(A):
    n = len(A)
    A.sort()
    prod_list = []

    for i in range(1, 4):
        prod = A[n-i] * A[n-i-1] * A[n-i-2]
        prod_list.append(prod)
    return max(prod_list)

      
if __name__ == '__main__':
    arr = [-3, 1, 2, -2, 5, 6]
    # max_product_of_three(arr)
    print(max_product_of_three(arr))
