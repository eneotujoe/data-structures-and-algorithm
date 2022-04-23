
def closest_numbers(arr):
    
    arr.sort()

    min_abs_diff = float('inf')
    
    for i in range(2, len(arr)):
        min_abs_diff = min(min_abs_diff, abs(arr[i] - arr[i-1]))
        
    for i in range(1, len(arr)):
        if (arr[i] - arr[i-1]) == min_abs_diff:
            return arr[i-1], arr[i]
        


if __name__ == '__main__':

    numbers = [5, 2, 3, 4, 1]

    print(closest_numbers(numbers))
