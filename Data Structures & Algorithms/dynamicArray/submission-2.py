class DynamicArray:
    
    def __init__(self, capacity: int):
        self.ar= []
        self.tail = 0
        self.size = capacity
        for i in range(capacity):
            self.ar.append(0)

    def get(self, i: int) -> int:
        return self.ar[i]

    def set(self, i: int, n: int) -> None:
        self.ar[i] = n

    def pushback(self, n: int) -> None:
        if self.tail == self.size:
            self.resize()
        self.ar.insert(self.tail, n)
        self.tail += 1

    def popback(self) -> int:
        out = self.ar[self.tail-1]
        self.tail -= 1
        return out

    def resize(self) -> None:
        for i in range(self.size):
            self.size += 1
            self.ar.append(0)

    def getSize(self) -> int:
        return self.tail
    
    def getCapacity(self) -> int:
        return self.size