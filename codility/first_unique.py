from collections import Counter
def first_unique(A):

    for index, num in enumerate(A):
        num_count = A.count(num)
        if num_count == 1:
            return A[index]

    return -1

    # num_count = Counter(A)
    # return next((num for num in A if num_count[num] == 1), -1)

      
if __name__ == '__main__':
    arrs = [[4, 10, 5, 4, 2, 10], [1, 4, 3, 3, 1, 2], [6, 4, 4, 6]]

    for arr in arrs:
        print(first_unique(arr))
    # first_unique(arr)
    # print(first_unique([6, 4, 4, 6]))
