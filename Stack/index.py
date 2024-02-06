class Stack:
    def __init__(self) -> None:
        self.list = []
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def push(self, value):
        self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            return "Empty List"
        else:
            removed = self.list.pop()
            return removed
    
    def delete(self):
        self.list = []
    
    def peek(self):
        return self.list[-1]
    
customStack = Stack()
