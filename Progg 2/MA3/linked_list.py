""" linked_list.py

Student: Anton Lindbro
Mail: anton.lindbro.8243@student.uu.se
Reviewed by: Julius Edqvist
Date reviewed: 9/10-24
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):          #   
        length = 0
        f = self.first
        while f:
            length += 1
            f = f.succ
        return length
        

    def mean(self):               
        sum = 0
        f = self.first
        while f:
            sum += f.data
            f = f.succ
        return sum/self.length()

    def remove_last(self):#
        value = 0
        if self.first == None:
            raise ValueError('Can not remove element from empty list!')
        elif self.length() == 1:
            value = self.first.data
            self.first = None
        else:
            f = self.first
            while f.succ.succ:
                f = f.succ
            value = f.succ.data
            f.succ = None
        
        return value

    def remove(self, x):         # 
        if self.first is None:
            return False
        
        if self.first.data == x:
            self.first = self.first.succ
            return True
        
        else:
            f = self.first
            while f.succ is not None:
                if f.succ.data == x:
                    f.succ = f.succ.succ
                    return True
                f = f.succ
            return False


    def to_list(self):            #
        f = self.first
        
        def _to_list(node):
            if node is None:
                return []
            else:
                return [node.data] + _to_list(node.succ)
        return _to_list(f)

    def remove_all(self, x):      #
        def _remove_all(node, x):
            if node is None:
                return None, 0
            
            if node.data == x:
                succ_node, count = _remove_all(node.succ, x)
                return succ_node, count + 1
            else:
                succ_node, count = _remove_all(node.succ, x)
                node.succ = succ_node
                return node, count
        self.first, removed_count = _remove_all(self.first, x)
        return removed_count


    def __str__(self):            #
        return '(' + ', '.join(str(value) for value in self) + ')'

    def copy_slow(self):               #
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 
        O(n^2)
    '''

    def copy(self):               # Should be more efficient
        if not self.first:
            return LinkedList()
        else:
            result = LinkedList()
            
            result.first = self.Node(self.first.data)
            
            current_new = result.first
            current_old = self.first.succ
            
            while current_old:
                current_new.succ = self.Node(current_old.data)
                
                current_new = current_new.succ
                current_old = current_old.succ
            
            return result
            
    ''' Complexity for this implementation:
        O(n)
    '''

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    print(lst.length())
    print(lst.mean())
    print(lst.__str__())
    lst.remove_last()
    print(lst.__str__())
    lst.remove_all(1)
    print(lst.__str__())
    print(lst.to_list())
    print(lst.copy().__str__())

    # Test code:


if __name__ == '__main__':
    main()
