for N in range(int(input())):
    A, B, C = map(int, input().split())
    no_ans = True

    range_x = int(C**0.5) # 由x^2+y^2+z^2=C得出x的范围
    for x in range(-range_x, range_x):
        if not no_ans: break

        range_y = int((C-x*x)**0.5) # 由x^2+y^2+z^2=C得出y的范围
        for y in range(-range_y, range_y):
            if not no_ans: break
            z = A - x - y

            if x*y*z == B and x**2+y**2+z**2 == C and x!=y and x!=z and y!=z:
                print(str(x)+' '+str(y)+' '+str(z))
                no_ans = False
    if no_ans:
        print("No solution.")
