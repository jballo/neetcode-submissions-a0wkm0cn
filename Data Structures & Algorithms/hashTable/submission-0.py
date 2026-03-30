class Pair:
    def __init__(self, key, val):
        self.key, self.val = key, val

TOMBSTONE = Pair(None, None)

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.table = [None] * capacity

    def hash(self, key):
        return key % self.cap

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while True:
            if self.table[index] != None and self.table[index] is not TOMBSTONE and self.table[index].key == key:
                self.table[index] = Pair(key, value)
                return
            elif self.table[index] == None or self.table[index] is TOMBSTONE:
                self.table[index] = Pair(key,value)
                self.size += 1
                if self.size >= (self.cap // 2):
                    self.resize()
                return

            index = (index + 1) % self.cap


    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.table[index] != None:
            if self.table[index] is not TOMBSTONE and self.table[index].key == key:
                return self.table[index].val
            
            index = (index + 1) % self.cap

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)

        while self.table[index] != None:
            if self.table[index] is not TOMBSTONE and self.table[index].key == key:
                self.table[index] = TOMBSTONE
                self.size -= 1
                return True
            index = (index + 1) % self.cap

        return False


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        oldTable = self.table
        oldCap = self.cap

        self.table = [None] * (oldCap * 2)
        self.cap = oldCap * 2
        self.size = 0

        for i in range(len(oldTable)):
            if oldTable[i] != None and oldTable[i] is not TOMBSTONE:
                self.insert(oldTable[i].key, oldTable[i].val)
