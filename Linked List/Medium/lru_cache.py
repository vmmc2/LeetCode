class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(-1, -1) # Sentinel
        self.right = Node(-1, -1) # Sentinel

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node: Node) -> None:
        prevNode = self.right.prev
        prevNode.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prevNode

        return

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

        return

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)

        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)