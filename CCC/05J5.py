while True:
    str=input()
    if str=="X":
        break
    str1=str.split("N")
    string=[]
    for ch in str1:
        if len(ch)>1:
            for c in ch:
                string.append(c)
        else:
            string.append(ch)
            
    def BSBalanced(string):
        str=[]
        for ch in string:
            if ch=="B":
                str.append("B")
            if ch=="S":
                if len(str)==0:
                    return False
                else:
                    str.pop()
        return len(str)==0
    def allA(str):
        for ch in str:
            if ch!="A" and ch!="B" and ch!="S":
                return False
        return True
    str1=""
    for ch in string:
        str1+=ch
    if BSBalanced(str1) and allA(str1) and ("AB" not in str) and ("SA" not in str) and ("AA" not in str) and ("BS" not in str):
        print("YES")
    else:
        print("NO")
        
