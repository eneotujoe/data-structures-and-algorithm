
def find_median(arr):
    
    arr.sort()
    n = len(arr)
    if n%2 != 0:
        return arr[n//2]
    else:
        return arr[((n/2) + ((n-1)/2))/2]


if __name__ == '__main__':

    arr = [5, 3, 1, 2, 4]

    print(find_median(arr))
