
def cyclic_rotation(A, K):
    return A[-K:] + A[0:-K]




    
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(arr)
    print(cyclic_rotation(arr, 2))
