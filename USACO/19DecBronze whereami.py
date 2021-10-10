def count(string, sub):
      count = 0
      for i in range(len(string)-len(sub) + 1):
           if string[i:i+len(sub)] == sub:
                count += 1
      return count

def find_res(num, string):
    for l in range(1, num+1):
        ok = True
        i = 0
        while i+l <= len(string):
            sub = string[i:i+l]
            if count(string, sub) > 1:
                ok = False
            i += 1
        if ok: return l

fin = open('whereami.in', 'r').read().strip().split('\n')
fout = open('whereami.out', 'w')

num, string = int(fin[0]), fin[1]
res = str(find_res(num, string))
fout.write(res + '\n')
