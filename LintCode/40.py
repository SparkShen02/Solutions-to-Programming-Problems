class Stack:
        def __init__(self):
            self.items=[]
        def push(self,item):
            self.items.append(item)
        def pop(self):
            return self.items.pop()
        def peek(self):
            return self.items[-1]
        def size(self):
            return len(self.items)
class MyQueue:
    def __init__(self):
        self.stack_push=Stack()
        self.stack_pop=Stack()

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.stack_push.push(element)
    """
    @return: An integer
    """
    def pop(self):
        if(self.stack_pop.size()==0):
            while(self.stack_push.size()!=0):
                self.stack_pop.push(self.stack_push.pop())
        return self.stack_pop.pop()

    """
    @return: An integer
    """
    def top(self):
        if(self.stack_pop.size()==0):
            while(self.stack_push.size()!=0):
                self.stack_pop.push(self.stack_push.pop())
        return self.stack_pop.peek()
