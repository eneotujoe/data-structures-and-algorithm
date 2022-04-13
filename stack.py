# LIFO (Last In First Out)

# from collections import deque

# simple stack using deque
# class Stack:

#     def __init__(self):
#         self.stack = deque()

#     def push(self, val):
#         self.stack.append(val)

#     def pop(self):
#         self.stack.pop()

#     def size(self):
#         return len(self.stack)
        
#     def empty(self):
#         return len(self.stack)==0

# using linked list
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def __str__(self) -> str:
        current = self.head.next
        output = ''
        while current:
            output += str(current.value) + '->'
            current = current.next
        return output

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty == 0:
            raise Exception('Cannot peek from an empty stack')
        return self.head.next.value

    def push(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.is_empty == 0:
            raise Exception('Cannot pop from an empty stack')
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

if __name__=='__main__':
    # print(dir(deque))
    stack = Stack()
    stack.push(200)
    stack.push(2000)
    stack.push(20000)
    print(stack.peek())
    print(stack)