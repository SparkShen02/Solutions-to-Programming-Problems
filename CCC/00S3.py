class Graph():
    def __init__(self,nodes,sides):
        self.sequence = {}
        self.side=[]
        for node in nodes:
            for side in sides:
                u,v=side
                if node ==u:
                    self.side.append(v)
            self.sequence[node] = self.side
            self.side=[]
    def DFS(self,node0):
        queue,order=[],[]
        queue.append(node0)
        while queue:
            v = queue.pop()
            order.append(v)
            for w in self.sequence[v]:                
                if w not in order and w not in queue: 
                    queue.append(w)
        return order
num=int(input())
url=[]
sides=[]
for i in range(num):
    URL=input()
    if URL not in url:
        url.append(URL)
    while True:
        str=input()
        if "</HTML>"==str:
            break
        if '<A HREF="' in str:
            str=str.split('<A HREF="')
            for x in range(1,len(str)):
                for y in range(0,len(str[x])):
                    if str[x][y]=='"':   
                        URL1=str[x][0:y]
                        if URL1 not in url:
                            url.append(URL1)
                        sides.append((URL,URL1))
                        print("Link from "+URL+" to "+URL1)
graph=Graph(url,sides)
print()
while True:
    str=input()
    if str=="The End":
        break
    str1=input()
    if str1 in graph.DFS(str): 
        print("Can surf from "+str+" to "+str1)
    else:
        print("Can't surf from "+str+" to "+str1)


                   

            

    
