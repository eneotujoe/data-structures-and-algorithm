class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key



if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    print(root.left)