# Jason McKinlay
# Memory Manager Library
# Dynamic Memory Allocation 

class Node:
    def __init__(self, value=None):  
        self.next = None
        self.value = value
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__

class Malloc_Library:

    """
    ** This is NOT a comprehensive test sample, test beyond this doctest
        >>> lst = Malloc_Library()
        >>> lst
        <BLANKLINE>
        >>> lst.malloc(5)
        >>> lst
        None -> None -> None -> None -> None
        >>> lst[0] = 23
        >>> lst
        23 -> None -> None -> None -> None
        >>> lst[0]
        23
        >>> lst[1]
        >>> lst.realloc(1)
        >>> lst
        23
        >>> lst.calloc(5)
        >>> lst
        0 -> 0 -> 0 -> 0 -> 0
        >>> lst.calloc(10)
        >>> lst[3] = 5
        >>> lst[8] = 23
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0 -> 0 -> 0 -> 0 -> 23 -> 0
        >>> lst.realloc(5)
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0
        >>> other_lst = Malloc_Library()
        >>> other_lst.realloc(9)
        >>> other_lst[0] = 12
        >>> other_lst[5] = 56
        >>> other_lst[8] = 6925
        >>> other_lst[10] = 78
        Traceback (most recent call last):
            ...
        IndexError
        >>> other_lst.memcpy(2, lst, 0, 5)
        >>> lst
        None -> None -> None -> 56 -> None
        >>> other_lst
        12 -> None -> None -> None -> None -> 56 -> None -> None -> 6925
        >>> temp = lst.head.next.next
        >>> lst.free()
        >>> temp.next is None
        True
    """

    def __init__(self):
        self.head = None
    
    def __repr__(self):
        current = self.head
        out = []
        while current != None:
            out.append(str(current.value))
            current = current.next
        return " -> ".join(out)

    __str__ = __repr__
    
    def __len__(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    
    def __setitem__(self, pos, value):
        current = self.head
        if pos >= self.__len__():
            raise IndexError
        count = 0
        while count != pos:
            count += 1
            current = current.next
        current.value = value


    def __getitem__(self, pos):
        current = self.head
        if pos >= self.__len__():
            raise IndexError("Index out of range")
        count = 0
        while count != pos:
            count += 1
            current = current.next
        return current.value
    

    def malloc(self, size):
        self.head = Node()
        current = self.head
        count = 0
        while count < size - 1:
            current.next = Node()
            count += 1
            current = current.next

    def calloc(self, size):
        self.head = Node(0)
        current = self.head
        count = 0
        while count < size - 1:
            current.next = Node(0)
            count += 1
            current = current.next

    def free(self):
        current = self.head
        while current is not None:
            temp = current.next
            current.next = None
            current = temp


    def realloc(self, size):
        if self.__len__() == 0:
            self.malloc(size)

        elif size > self.__len__():
            current = self.head
            count = 0

            while count < size - 1:
                if count < self.__len__() - 1:
                    current = current.next
                else:
                    current.next = Node()
                    current = current.next
                count += 1

        else:
            current = self.head
            count = 0
            while count < size - 1:
                current = current.next
                count += 1
            current.next = None

    def memcpy(self, ptr1_start_idx, pointer_2, ptr2_start_idx, size):
        if size > self.__len__():
            size = self.__len__()

        current1 = self.head
        count = 0
        if ptr1_start_idx < self.__len__():
            while count < ptr1_start_idx: # traverse the list until you get to ptr1 index
                current1 = current1.next
                count += 1

        current2 = pointer_2.head
        count = 0
        if ptr2_start_idx < pointer_2.__len__():
            while count < ptr2_start_idx: # traverse the other list until you get to ptr2 index
                current2 = current2.next
                count += 1 
                
        current2.value = current1.value
        if size > pointer_2.__len__() - count - 1: # if size is bigger than remaining length of list
            while count < pointer_2.__len__() - 1:
                current2 = current2.next
                current1 = current1.next
                current2.value = current1.value
                count += 1
            current2.next = None
        else:
            count = 0
            while count < size:
                current2 = current2.next
                current1 = current1.next
                current2.value = current1.value
                count += 1
            current2.next = None

def run_tests():
    import doctest
    doctest.testmod(verbose=True)
     

if __name__ == "__main__":
     run_tests()