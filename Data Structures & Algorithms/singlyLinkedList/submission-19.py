class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 

class LinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None
    
    def get(self, index: int) -> int:
        N = self.Head
        if N == None:
            return -1
            
        for i in range(index):
            if N.next:
                 N = N.next
            else:
                return -1
        return N.val

    def insertHead(self, val: int) -> None:
        NewNode = Node(val)
        if self.Head == None:
            self.Head = NewNode
            self.Tail = self.Head
        else:
            NewNode.next = self.Head
            self.Head = NewNode

    def insertTail(self, val: int) -> None:
        NewNode = Node(val)
        if self.Tail == None:
            self.Tail = NewNode
            self.Head = self.Tail
        else:
            self.Tail.next = NewNode
            self.Tail = NewNode
        

    def remove(self, index: int) -> bool:
        N = self.Head
        # At the start
        if not N:
            return False
        if index == 0 and N:
            self.Head = N.next
            return True
        # in betweem
        for i in range(index-1):
            if N:
                N = N.next
            else:
                return False

        if N and N.next:
            if N.next == self.Tail:
                self.Tail = N
            right = N.next.next
            N.next = right
            return True

        return False
        
           
    def getValues(self) -> List[int]:
        # iterating through and adding  all values to an array
        # start from head, move over add and repeat
        N = self.Head
        out = [] 
        while N:
            out.append(N.val)
            N = N.next

        return out 
        
