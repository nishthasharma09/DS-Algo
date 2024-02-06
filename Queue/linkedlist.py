class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    def __str__(self) -> str:
        return str(self.value)
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()
    
    def __str__(self) -> str:
        values = [str(x) for x in self.LinkedList]
        return ' '.join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "Empty Linked List"
        else:
            tempNode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = tempNode.next
            return tempNode

    
customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
print(customQueue)