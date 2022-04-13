def insertion_sort(arr):
    
    i = 1
    while i < len(arr):
        x = arr[i]
        j = i - 1

        while j >=0 and arr[j] > x:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = x
        i += 1



if __name__=='__main__':
    nums = [600, 100, 300, 500, 200, 400]
    insertion_sort(nums)
    print(nums)