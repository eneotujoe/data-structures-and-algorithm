
import time
 

def timeit(func):
     
    def inner(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {(end - begin)*1000} milliseconds')
        return result
 
    return inner