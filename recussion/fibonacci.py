from functools import lru_cache


fibonacci_cache = {}

@lru_cache
def fibonacci(n):
    if type(n) != int or n < 0:
        raise TypeError('Number must be a positive integer')
        
    # if n in fibonacci_cache:
    #     return fibonacci_cache[n]
    # if n == 0:
    #     return 0
    # elif n == 1 or n == 2:
    #     return 1
    # elif n > 2:
    #     value =  fibonacci(n-1) + fibonacci(n-2)
    #     fibonacci_cache[n] = value
    #     return value

    
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        value =  fibonacci(n-1) + fibonacci(n-2)
        return value

def fibonacci_ratio(n):
    if n == 0:
        print('Number must be greater than zero')
    else:
        return fibonacci(n+1)/fibonacci(n)

if __name__=='__main__':
    
    for n in range(0, 100):
        # print(f'{n} - {fibonacci(n)}')
        print(f'Fibonacci Ratio - {fibonacci_ratio(n)}')

    # print(fibonacci(8))

