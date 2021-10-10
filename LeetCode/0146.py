class Node:
    def __init__(self, key=-1, val=-1, next=None, pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre

'''
Use a dictionary (hash table) to store keys and their corresponding nodes.
Use a doubly linked list to store nodes from the least recently used to the most recently used. 
Time complexity (for get and put): O(1), Space complexity: O(n). 
'''
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Use dummy nodes for head and tail
        self.beforeLeastRecent = Node()
        self.afterMostRecent = Node()
        self.connectNodes(self.beforeLeastRecent, self.afterMostRecent)

    def connectNodes(self, nodeA, nodeB):
        nodeA.next = nodeB
        nodeB.pre = nodeA
    
    def addToMostRecent(self, node):
        self.connectNodes(self.afterMostRecent.pre, node)
        self.connectNodes(node, self.afterMostRecent)

    def removeNode(self, node):
        self.connectNodes(node.pre, node.next)

    def moveToMostRecent(self, node):
        self.removeNode(node)
        self.addToMostRecent(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveToMostRecent(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Add or update the node
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToMostRecent(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.addToMostRecent(node)

        if len(self.cache) > self.capacity: # O(1)
            # Evict the least recently used node
            node = self.beforeLeastRecent.next
            self.removeNode(node)
            self.cache.pop(node.key)