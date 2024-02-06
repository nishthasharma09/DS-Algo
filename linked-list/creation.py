class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
    
node1 = Node(1)
node2 = Node(2)

singleLL = SingleLinkedList()
singleLL.head = node1
singleLL.head.next = node2
singleLL.tail = node2