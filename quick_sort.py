
def swap(array, lo, hi):
    (array[lo], array[hi]) = (array[hi], array[lo])


def partition(array, lo, hi):
    pivot = array[hi]

    i = lo - 1

    for j in range(lo, hi):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    
    swap(array, i+1, hi)

    return i + 1

def quick_sort(array, lo, hi):
    if lo < hi:
        p = partition(array, lo, hi)
        quick_sort(array, lo, p - 1)
        quick_sort(array, p + 1, hi)



if __name__=='__main__':
    nums = [400, 100, 600, 300, 500, 200]
    quick_sort(nums, 0, len(nums)-1)
    print(nums)