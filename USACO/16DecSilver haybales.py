"""
ID: kraps
LANG: PYTHON3
TASK: haybales
"""
def search(arr, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return (True, mid)
        if arr[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return (False, low)

fin = open ('haybales.in', 'r').read().strip().split('\n')
fout = open ('haybales.out', 'w')

N, Q = map(int, fin[0].split(' '))
arr = list(map(int, fin[1].split(' ')))
arr.sort()

for i in range(Q):
    left, right = map(int, fin[2+i].split(' '))
    state1, num1 = search(arr, left)
    state2, num2 = search(arr, right)
    if state2:
        fout.write (str(num2 - num1 + 1) + '\n')
    else:
        fout.write (str(num2 - num1) + '\n')

fout.close()
