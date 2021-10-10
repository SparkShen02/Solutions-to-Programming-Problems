import sys
first = True
lines = sys.stdin.read().strip().split('\n')
lines.reverse()
for i in range(int(lines.pop())):
     if first:
          first = False
     else:
          print()
     
     cars = []
     for car in range(int(lines.pop())):
          line = lines.pop().split()
          cars.append((line[0], int(line[1]), int(line[2])))

     res = ''
     for j in range(int(lines.pop())):
          undetermined = False
          price = int(lines.pop())
          count = 0
          for brand, min_price, max_price in cars:
               if min_price <= price <= max_price:
                    count += 1
                    if count > 1:
                         undetermined = True
                         break
                    res = brand

          if undetermined or count == 0:
               print("UNDETERMINED")
          else:
               print(res)
     
