
"""
Time Complexity: O(1) for get and put (avg. time complexities)
Space Complexity: O(capacity)

Approach: Uses a combination of a hashmap (key → node) and a doubly linked list 
to achieve O(1) access and update. The DLL maintains the usage order, with the 
most recently used node at the head and the least recently used at the tail.
"""


class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    class DLL:
        def __init__(self):
            self.head = LRUCache.Node(-1, -1)
            self.tail = LRUCache.Node(-1, -1)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0
        
        def addToHead(self, node):
           curr = self.head.next
           node.prev = self.head
           node.next = curr
           self.head.next = node
           curr.prev = node

           self.size += 1
        
        def removeTail(self):
            if self.size == 0:
                return None

            node = self.tail.prev
            self.tail.prev = node.prev
            node.prev.next = self.tail
            node.next = None
            node.prev = None

            self.size -= 1
            return node

            
    
        def removeNode(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None

            self.size -= 1



    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyMap = {} #key -> Node
        self.Dll = LRUCache.DLL()

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        
        node = self.keyMap[key]
        self.Dll.removeNode(node)
        self.Dll.addToHead(node)
        return node.val
    
        

    def put(self, key: int, value: int) -> None:
        
        if key not in self.keyMap:
            node = LRUCache.Node(key, value)
            #if cache is full, remove the LRU cache node
            if self.Dll.size == self.capacity:
                tail = self.Dll.removeTail()
                del self.keyMap[tail.key]
            
            self.Dll.addToHead(node)
            self.keyMap[key] = node

        else:
            #already there in keymap
            node = self.keyMap[key]
            node.val = value
            self.Dll.removeNode(node)
            self.Dll.addToHead(node)
            
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)