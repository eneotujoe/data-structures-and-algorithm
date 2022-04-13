def bubble_sort(arr):
    size = len(arr)

    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        
        if not swapped:
            break

if __name__=='__main__':
    arr = [200, 100, 600, 300, 500, 400]
    bubble_sort(arr)
    print(arr)
