
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    
            

if __name__=='__main__':
    nums = [600, 100, 300, 500, 200, 400]
    selection_sort(nums)
    print(nums)