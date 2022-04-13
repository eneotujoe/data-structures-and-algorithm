# from collections import Counter

def odd_occurrence_array(A):

    # for x, y in Counter(A).items():
    #     if y % 2:
    #         print(x)
      

    for i, num in enumerate(A):
        unpaired = A.count(num)
        if unpaired == 1:
            print(A[i])

      
if __name__ == '__main__':
    arr = [9, 3, 9, 3, 9, 7, 9]
    odd_occurrence_array(arr)
