fin = open ('walk.in', 'r')
fout = open ('walk.out', 'w')

N, K = map(int, fin.readline().split())

fout.write(str(2019201997 - 84 * (K-1) - 48 * N) + '\n')

fout.close()
