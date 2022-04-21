
def flood_fill(img, row, col, p):
    start = img[row][col]
    queue = [(row, col)]
    visited = set()

    while len(queue) > 0:
        row, col = queue.pop(0)
        visited.add((row, col))
        img[row][col] = p

        for row, col in neighbors(img, row, col, start):
            if (row, col) not in visited:
                queue.append((row, col))
    return img

def neighbors(img, row, col, start):
    indices = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    return [(row, col) for row, col in indices if isValid(img, row, col) and img[row][col]==start]

def isValid(img, row, col):
    return row >= 0 and col >= 0 and row < len(img) and col < len(img[0])

if __name__ == '__main__':
   arr = [
       [1, 0, 2, 2, 0],
       [0, 2, 0, 2, 0],
       [2, 2, 2, 2, 2],
       [0, 0, 2, 0, 2],
       [1, 0, 0, 0, 0],
   ]
#    flood_fill()
   print(flood_fill(arr, 2, 2, 4))