
def flood_fill(image, sr, sc, newColor):
    start = image[sr][sc]
    queue = [(sr, sc)]
    visited = set()

    while len(queue) > 0:
        sr, sc = queue.pop(0)
        visited.add((sr, sc))
        image[sr][sc] = newColor

        for sr, sc in neighbors(image, sr, sc, start):
            if (sr, sc) not in visited:
                queue.append((sr, sc))
    return image

def neighbors(image, sr, sc, start):
    indices = [(sr-1, sc), (sr+1, sc), (sr, sc-1), (sr, sc+1)]
    return [(sr, sc) for sr, sc in indices if isValid(image, sr, sc) and image[sr][sc]==start]

def isValid(image, sr, sc):
    return sr >= 0 and sc >= 0 and sr < len(image) and sc < len(image[0])

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