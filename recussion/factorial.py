
factorial_cache = {}

def factorial(n):

    if n in factorial_cache:
        return factorial_cache[n]
    
    if n < 0:
        return -1
    elif n <= 1:
        return 1
    elif n > 1:
        val = n * factorial(n-1)
        factorial_cache[n] = val
        return val

        

    
if __name__=='__main__':
        
    for n in range(0, 1000):
        print(f'{n} - {factorial(n)}')