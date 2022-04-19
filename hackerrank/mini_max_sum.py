
def mini_max_sum(arr):
    arr2 = arr.copy()

    arr.remove(min(arr))
    arr2.remove(max(arr2))
    max_sum = sum(arr)
    min_sum = sum(arr2)

    # for i, num in enumerate(arr):
    #     if num == min_val:
    #         arr.pop(i)
    #         max_sum = sum(arr)
    # for i, num in enumerate(arr2):
    #     if num == max_val:
    #         arr2.pop(i)
    #         min_sum = sum(arr2)

    print(f'{min_sum} {max_sum}')


if __name__ == '__main__':

    arr = [1, 3, 5, 7, 9]
    print(mini_max_sum(arr))
