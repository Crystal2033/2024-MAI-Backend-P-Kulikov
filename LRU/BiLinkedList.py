class BiLinkedList:
    head = None
    tail = None

    class Node:
        def __init__(self, key, value):
            self.keyValue = (key, value)

        next = None
        prev = None

        def getValue(self):
            return self.keyValue[1]

    def add(self, key, value):
        node = self.Node(key, value)
        if not self.tail:
            self.tail = node
            self.head = self.tail
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        return node

    def remove_elder_element(self):
        return self.remove(self.tail)

    def remove(self, node: Node):
        if node.keyValue == self.head.keyValue and node.keyValue == self.tail.keyValue:
            self.head = self.tail = None
        elif node.keyValue == self.tail.keyValue:
            self.tail.next.prev = None
            self.tail = self.tail.next
            node.next = None
        elif node.keyValue == self.head.keyValue:
            self.head.prev.next = None
            self.head = self.head.prev
            node.prev = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        return node.keyValue
