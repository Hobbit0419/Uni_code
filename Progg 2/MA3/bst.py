""" bst.py

Student: Anton Lindbro
Mail: anton.lindbro.8243@student.uu.se
Reviewed by: Julius Edqvist
Date reviewed: 9/10-24
"""


from linked_list import LinkedList
from random import randint


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k): #
        return self._contains(self.root, k)
        
    def _contains(self, r, k):
        if r is None:
            return False
        elif k == r.key:
            return True
        elif k < r.key:
            return self._contains(r.left, k)
        else:
            return self._contains(r.right, k)
        
        
    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                 #            
        return self._height(self.root)
    
    def _height(self, r):
        if r is None:
            return 0
        else:
            return 1 + max(self._height(r.left), self._height(r.right))

    def _minimum(self, r):
        root = r
        while root.left is not None:
            root = root.left
        return root
    
    def remove(self, key): #
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      #
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                m = self._minimum(r.right).key
                r.key = m
                r.right = self._remove(r.right, m)
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):                #            
        return '<' + ', '.join(str(value) for value in self) + '>'

    def to_list(self):                      #O(n)  
        result = []
        for value in self:
            result.append(value)
        return result

    def to_LinkedList(self):                 # O(n²)
        result = LinkedList()
        for value in self:
            result.insert(value)
        return result


def random_tree(n):                               # Useful
    result = BST()
    
    for i in range(n):
        result.insert(randint(0, 9))
    return result

def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    
    print(t.__str__())

    print('height  : ', t.height())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? Yes
2. computing height? No
3. contains? Yes
4. insert? No
5. remove? Yes

"""
