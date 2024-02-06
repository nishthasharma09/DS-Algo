class Stack:
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        temp = self.list.reverse()
        temp = [str(i) for i in self.list]
        return '\n'.join(temp)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    def push(self, value):
        if self.isFull():
            return "Stack is Full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"
    
customStack = Stack(2)
customStack.push(1)
customStack.push('hello')
print(customStack.push(2))
customStack.push(3)
print(customStack)
    
