def insertion_sort(n, arr):

    x = arr[-1]
    i = n-2

    while (x < arr[i]) and (i >= 0):
        arr[i+1] = arr[i]
        print(*arr)
        i -= 1

    arr[i+1] = x
    print(*arr)
    print(i)




if __name__=='__main__':
    nums = [1, 2, 4, 5, 3]
    insertion_sort(len(nums), nums)
    # print(nums)
