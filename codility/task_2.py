from collections import Counter

def task_2(P, S):
    A = P + S
    N = 0
    
    for index, num in enumerate(A):
        num_count = A.count(num)
        if num_count == 1:
            N +=1
    
    return N

      
if __name__ == '__main__':
    P = [1, 4, 1]
    S = [1, 5, 1]
    print(task_2(P, S))
