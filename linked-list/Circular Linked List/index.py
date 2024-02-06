class Node:
    def __init__(self, value) -> None:
        self.value = value

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCircularLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        print('Created')
    
    def reverseList(self):
        head = self.head

        node = head
        prevNode = head
        nextNode = node.next
        while nextNode is not None:
            nextNode.next = prevNode
            prevNode = nextNode
            nextNode = nextNode.next
    
    def insertCircularLL(self, value, location):
        if self.head is None:
            return 'Head reference is None'
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                temp = self.head
                index = 0
                while index < location -1:
                    temp = temp.next
                    index += 1
                nextNode = temp.next
                temp.next = newNode
                newNode.next = nextNode

    def traverseCSLL(self):
        if self.head is None:
            return 'Empty Linked List'
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
                if temp == self.tail.next:
                    break

circularSLL = CircularLinkedList()
circularSLL.createCircularLL(3)
circularSLL.insertCircularLL(0,0)
circularSLL.insertCircularLL(1,0)
circularSLL.insertCircularLL(2,0)
circularSLL.insertCircularLL('yes',1)
print([node.value for node in circularSLL])
circularSLL.reverseList()
print('after', [node.value for node in circularSLL])

