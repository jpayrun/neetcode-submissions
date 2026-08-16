class Node:

    def __init__(self, data: int, next = None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.count = 0
    
    def get(self, index: int) -> int:
        if index >= self.count:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.data
        

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.count+=1
        

    def insertTail(self, val: int) -> None:
        if self.count == 0:
            self.insertHead(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
        self.count+=1
        

    def remove(self, index: int) -> bool:
        if index >= self.count:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.count-=1
        return True
        

    def getValues(self) -> List[int]:
        res = [0] * self.count
        cur = self.head
        for i in range(self.count):
            res[i] = cur.data
            cur = cur.next
        return res

    def __len__(self):
        return self.count
