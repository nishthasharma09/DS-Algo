class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = next
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self) -> str:
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.pop()
print(customStack)