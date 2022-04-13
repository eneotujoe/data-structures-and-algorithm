def linear_search(arr, x):
    for index, element in enumerate(arr):
        if element == x:
            return index 

    return -1

    

if __name__=='__main__':
    print(linear_search([2, 3, 4, 5, 6, 7, 8], 5))