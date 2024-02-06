#without size limit

class Queue:
    def __init__(self) -> None:
        self.list = []

    def __str__(self) -> str:
        value = [str(x) for x in self.list]
        return ' '.join(value)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.list.append(value)
        return "Element added at the end"
    
    def dequeue(self):
        if self.isEmpty():
            return "Empty list"
        else:
            return self.list.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Empty list"
        else:
            return self.list[0]
    
    def delete(self):
        self.list = []
            

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
customQueue.dequeue()
print(customQueue.peek())
