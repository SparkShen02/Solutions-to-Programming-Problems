import sys
lines = sys.stdin.read().strip().split("\n")

i = 0
while i < len(lines):
    ans = "012" # 0=stack, 1=queue, 2=priority queue
    stack, queue, pq = [], [], []
    for x in range(int(lines[i])):
        a, b = map(int, lines[i+1].split())
        i += 1
        
        if a == 1: # throw in
            stack.append(b)
            queue.append(b)
            pq.append(b)
        elif a == 2: # take out
            if stack == [] or stack[-1] != b: # not a stack
                ans = ans.replace("0", "")
            else:
                stack.pop()
                
            if queue == [] or queue[0] != b: # not a queue
                ans = ans.replace("1", "")
            else:
                queue.pop(0)
                
            if pq == [] or max(pq) != b: # not a priority queue
                ans = ans.replace("2", "")
            else:
                pq.remove(b)
    i += 1
    
    if len(ans) > 1:
        print("not sure")
    elif len(ans) == 0:
        print("impossible")
    else:
        print(["stack", "queue", "priority queue"][int(ans)])
        
