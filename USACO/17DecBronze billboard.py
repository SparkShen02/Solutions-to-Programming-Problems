fin = open ('billboard.in', 'r')
fout = open ('billboard.out', 'w')

first = list(map(int, fin.readline().strip().split(' ')))
second = list(map(int, fin.readline().strip().split(' ')))
block = list(map(int, fin.readline().strip().split(' ')))

minus = 0
#https://blog.csdn.net/lanchunhui/article/details/50547837
one = first[2] <= block[0] or first[1] >= block[3]
two = block[2] <= first[0] or  block[1] >= first[3]
judge = one or two
if not judge:
    length = min(block[2], first[2]) - max(block[0], first[0])
    width = min(block[3], first[3]) - max(block[1], first[1])
    minus += length * width
area1 = (first[3]-first[1]) * (first[2]-first[0])

one = second[2] <= block[0] or second[1] >= block[3]
two = block[2] <= second[0] or  block[1] >= second[3]
judge = one or two
if not judge:
    length = min(block[2], second[2]) - max(block[0], second[0])
    width = min(block[3], second[3]) - max(block[1], second[1])
    minus += length * width
area2 = (second[3]-second[1]) * (second[2]-second[0])

num = area1 + area2 - minus
fout.write (str(num) + '\n')
