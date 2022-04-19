
def closestNumbers(numbers):

    if len(numbers) < 1: return

    numbers.sort()

    min_diff = numbers[1] - numbers[0]
    
    for i in range(2, len(numbers)):
        min_diff = min(min_diff, numbers[i] - numbers[i-1])
        
    for i in range(1, len(numbers)):
        if (numbers[i] - numbers[i-1]) == min_diff:
            print(f'({numbers[i-1]}, {numbers[i]})')
        



if __name__ == '__main__':

    numbers = [6, 2, 4, 10]

    closestNumbers(numbers)
