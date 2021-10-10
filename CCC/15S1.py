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
s=Stack()
numOfIntegers=int(input())
sum=0
for i in range(numOfIntegers):
    num=int(input())
    if(num!=0):
        s.push(num) 
    if(num==0):
        s.pop()
for a in s.items:
    sum+=a
print(sum)
print()
            
            
