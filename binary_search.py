from timeit import timeit


@timeit
def linear_search(arr, x):
    for index, element in enumerate(arr):
        if element == x:
            return index 

    return -1

@timeit
def binary_search(arr, x):

    low_index = 0
    mid_index = 0
    high_index = len(arr) - 1

    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        mid_num = arr[mid_index]

        if mid_num == x:
            return mid_index

        if mid_num < x:
            low_index = mid_index + 1
        else:
            high_index =mid_index + 1

    return -1




if __name__=='__main__':
    print(linear_search([x for x in range(1, 1000000)], 99999))
    print(binary_search([x for x in range(1, 1000000)], 99999))