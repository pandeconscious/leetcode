class DLLNode(object):
    def __init__(self, key, value):
        self.k = key
        self.v = value
        self.left = None
        self.right = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap, self.count, self.key2dll_node,  self.dll_head, self.dll_tail  = capacity, 0, {}, None, None
      
    def __dll_delete_node(self, dll_node):
        if dll_node == self.dll_head and dll_node == self.dll_tail:
            self.dll_head, self.dll_tail = None, None
        elif dll_node == self.dll_head:
            self.dll_head = self.dll_head.right
            self.dll_head.left = None
        elif dll_node == self.dll_tail:
            self.dll_tail = self.dll_tail.left
            self.dll_tail.right = None
        else:
            temp = dll_node
            dll_node.left.right = temp.right
            dll_node.right.left = temp.left
            temp.left, temp.right = None, None
        self.count -= 1
        self.key2dll_node.pop(dll_node.k)
        
    
    def __dll_inset_end(self, dll_node):
        if self.dll_head == None:
            self.dll_head = dll_node
            self.dll_tail = dll_node
        else:
            self.dll_tail.right = dll_node
            dll_node.left = self.dll_tail
            self.dll_tail = self.dll_tail.right
        self.count += 1
        self.key2dll_node[dll_node.k] = dll_node
        
        #handle capacity check
        if self.count > self.cap:
            self.__dll_delete_node(self.dll_head)
    

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        dll_node = self.key2dll_node.get(key, None)
        if dll_node == None:
            return -1
        else:
            self.__dll_delete_node(dll_node)#delete from old position in the queue
            self.__dll_inset_end(dll_node)#insert into the end to show most recently used position
            return dll_node.v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        dll_node = self.key2dll_node.get(key, None)
        if dll_node is None:
            dll_node = DLLNode(key, value)
        else:
            dll_node.v = value #updating the new value
            self.__dll_delete_node(dll_node) #delete from old position in the queue
        self.__dll_inset_end(dll_node)#insert into the end to show most recently used position
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
