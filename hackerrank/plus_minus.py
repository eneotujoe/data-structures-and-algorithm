def plus_minus(arr):
    positive_count = len(list(filter(lambda x: x>0, arr)))
    negative_count = len(list(filter(lambda x: x<0, arr)))
    zero_count = len(list(filter(lambda x: x==0, arr)))
    print(f'{positive_count/len(arr):.6f}\n{negative_count/len(arr):.6f}\n{zero_count/len(arr):.6f}')
    


if __name__ == '__main__':

    arr = [-4, 3, -9, 0, 4, 1]
    print(plus_minus(arr))
