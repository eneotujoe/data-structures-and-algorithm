# FIFO (First In First Out)
# queue = []
# queue.insert(0, 'orange')
# queue.insert(0, 'apple')
# queue.insert(0, 'banana')
# print(queue)
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue)

# from collections import deque

# queue = deque()

# queue.append('orange')
# queue.append('apple')
# queue.append('banana')
# print(queue)
# print(queue.popleft())

from queue import Queue

q = Queue(maxsize=3)

q.put('orange')
q.put('apple')
q.put('banana')
print(q.qsize())


if __name__=='__main__':
    pass