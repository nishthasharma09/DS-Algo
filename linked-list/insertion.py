class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    #traverse
    def traverseSLL(self):
            if self.head is None:
                print('The Linked List does not exist')
            else:
                node = self.head
                while node is not None:
                    print(node.value)
                    node = node.next
    
    #insertion
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    # searching
    def insertAtEnd(self,x):
        head = self.head

        newNode = Node(x)
        newNode.next = None
        tempNode = head
        while tempNode is not None:
            if tempNode.next is None:
                tail = tempNode
                print('tail is', tail)
            tempNode = tempNode.next

    def searchSLL(self,value):
        if self.head is None:
            return "LL unavailable"
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return 'Found'
                node = node.next
            return "Value not Found"
    
    def getCount(self):
        head_node = self.head
        count = 0
        while head_node.next is not None:
            count += 1
        return count

    def deleteSLL(self, location):
        if self.head is None:
            return "LL doesn't exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = None
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    #delete entire list
    def deleteEntireSLL(self):
        if self.head is None:
            print('Singly Linked List does not exist')
        else:
            self.head = None
            self.tail = None
        
singlyLinkedList = SingleLinkedList()
singlyLinkedList.insertSLL(1, 0)
singlyLinkedList.insertSLL('string', 0)
singlyLinkedList.insertSLL({"operation": 'Linkedlist'}, 0)
singlyLinkedList.insertSLL('new at 1', 2)
# singlyLinkedList.insertAtEnd('end')
print(singlyLinkedList.getCount())
print([node.value for node in singlyLinkedList])



    
 

   
    
     