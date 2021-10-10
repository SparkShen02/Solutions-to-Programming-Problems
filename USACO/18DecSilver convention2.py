lines = open("convention2.in", "r").read().strip().split("\n")
out = open("convention2.out", "w")

import heapq

cows = [] # 全体牛
wait = [] # 到了现场但还没轮到的牛

# 序号 i 代表资历
for (i, line) in enumerate(lines[1:]):
    a, t = map(int, line.split())
    heapq.heappush(cows, (a, i, t))

time = 0
max_wait = 0

while cows or wait:
    # 在每一个时刻，检查有没有牛已经到了，有的话就从 cows 转移到 wait
    while cows and cows[0][0] <= time:
        a, i, t = heapq.heappop(cows)
        heapq.heappush(wait, (i, a, t))

    new_cow = None
    # 如果 wait 里面没有牛，说明当前时刻还没有牛来，所以时间可以直接推移到下一头牛来的时候
    if wait:
        new_cow = heapq.heappop(wait)
    else:
        a, i, t = heapq.heappop(cows)
        new_cow = (i, a, t)

    seniority, arrival, time_spend = new_cow
    if arrival > time:
        time = arrival + time_spend
    else:
        max_wait = max(max_wait, time - arrival)
        time += time_spend
out.write(str(max_wait)+"\n")
out.close()
