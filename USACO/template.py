debug = True
if debug:
    lines = []
    while True:
        string = input()
        if string == "stop":
            break
        lines.append(string)
else:
    lines = open("xxx.in","r").read().strip().split("\n")

res = 0

if debug:
    print(res)
else:
    out = open("xxx.out","w")
    out.write(str(res) + "\n")
    out.close()
