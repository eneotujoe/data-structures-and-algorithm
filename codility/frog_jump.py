

def frog_jump(X, Y, D):
    step = X
    while step < Y:
        step += D
    return step // D


if __name__ == '__main__':
    print(frog_jump(10, 85, 30))
