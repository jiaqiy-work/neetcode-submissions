class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
        
        node = ListNode(key, value)
        self.add(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            deleteNode = self.head.next
            self.remove(deleteNode)
            del self.map[deleteNode.key]
        
    def add(self, node):
        oldTail = self.tail.prev
        oldTail.next = node
        node.prev = oldTail
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next