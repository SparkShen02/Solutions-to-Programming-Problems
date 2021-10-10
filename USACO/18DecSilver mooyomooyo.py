lines = open("mooyomooyo.in", "r").read().strip().split("\n")
out = open("mooyomooyo.out", "w")

n, k = map(int, lines[0].split())
matrix = lines[1:]

# 深度优先搜索找相连的同色格子
def find_connected(i, j):
    global matrix, n
    color = matrix[i][j]
    cells = [(i, j)]
    connected = set()
    while cells:
        [row, col] = cells.pop()
        connected.add((row, col))
        for (newrow, newcol) in [(row, col+1), (row, col-1), (row-1, col), (row+1, col)]:
            if 0<=newrow<n and 0<=newcol<10 and matrix[newrow][newcol]==color and (newrow, newcol) not in connected:
                cells.append((newrow, newcol))
    return connected

def reduce(matrix):
    global n
    for col in range(10):
        # 这里我用字符串的方法偷鸡摸狗了一下，如果超时的话我是准备将它改成更直接的数组操作
        items = "".join([matrix[row][col] for row in range(n)])
        items = items.replace("0", "")
        items = items.rjust(n, "0")
        for row in range(n):
            matrix[row][col] = items[row]

while True:
    changed = False
    new_matrix = [[None]*10 for i in range(n)]
    for i in range(n):
        for j in range(10):
            # 避免重复探索
            if new_matrix[i][j] is not None:
                continue
            elif matrix[i][j]=="0":
                new_matrix[i][j]="0"
            else:
                connected = find_connected(i, j)
                color = matrix[i][j]
                at_least_k = len(connected)>=k # 同颜色 >=k 个才消除
                if at_least_k: changed = True
                # 无论消除与否，都在新的矩阵中设定值，有效避免重复探索
                for (row, col) in connected:
                   new_matrix[row][col] = "0" if at_least_k else color
    if not changed: break
    reduce(new_matrix)
    matrix = new_matrix

for line in matrix:
    out.write("{}\n".format("".join(line)))
out.close()
Hosted by Coding Pages
