def swap(arr, low, high):
    arr[high], arr[low] = arr[low], arr[high]

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        heapify(arr, i, 0)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, n, largest)



if __name__=='__main__':
    nums = [400, 100, 600, 300, 500, 200]
    heap_sort(nums)
    print(nums)