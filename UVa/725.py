def qualify(nume, deno): # numerator, denominator
    a = set(nume)
    b = set(deno)
    # 如果分子分母都是4位数，或分子、分母自身有重复的数字，return False
    if len(a) < 5 or len(b) < 5: 
        return False
    # 两个set的交集，相当于看两个set有没有重复的数字
    if len(a.intersection(b)) == 0: 
        return True
    return False

k = int(input())
first = True
while k != 0:
    have_sol = False
    if first:
        first = False
    else:
        print()
        
    for deno in range(1234, 100000//k+1):
        nume = deno * k
        nume = str(nume)
        deno = str(deno)
        if len(deno) == 4:
            deno = "0" + deno
        if qualify(nume, deno):
            have_sol = True
            print("{} / {} = {}".format(nume, deno, k))
            
    if not have_sol:
        print("There are no solutions for {}.".format(k))
    k = int(input())
    
