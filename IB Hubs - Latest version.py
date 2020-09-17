V = input()
S = input()
dic = {}
v =[int(x) for x in V.split(".")]
s =[int(s) for s in S.split(".")]
#di = sorted(dic.items() ,key = lambda x:(x[1][2],x[1][1],x[1][0]))
#req_list = [str(x) for x in di[1][1]]
c = len(v)
d = len(s)
if c>=d:
    for i in range(d):
        if v[i]>s[i]:
            print('.'.join(map(str,v)))
            break
        elif v[i]<s[i]:
            print('.'.join(map(str,s)))
            break
elif c<d:
    for i in range(c):
        if v[i]>s[i]:
            print('.'.join(map(str,v)))
            break
        elif v[i]<s[i]:
            print('.'.join(map(str,s)))
            break
