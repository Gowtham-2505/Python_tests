#Sample Input:
#4
#CSk;Mi;win
#TEAM;B;win
#rr;RCB;draw
#KKR;kXIp;win

# code 1:

def countX(lst, x):     # to count how much is frequency of 'x' in list 'lst'

  count = 0

  for ele in lst: 

    if (ele == x): 

          count = count + 1

  return count 

def sort_d(d):          # table sorting

  sd = dict(sorted(d.items(),key = lambda x:(x[1][4],x[1][1],x[1][2]),reverse = True))

  return sd

def table(key,val):           # printing output as table

  name = key 

  l = len(name)

  MP = str(val[0])

  W = str(val[1])

  D = str(val[2])

  L = str(val[3])

  P = str(val[4])

   

  print("{:23s}".format(name)+' |'+MP.rjust(3)+' |'+W.rjust(3)+' |'+D.rjust(3)+' |'+L.rjust(3)+' |'+P.rjust(3)+' |')



n = int(input()) # no of games

mat = []

for i in range(n):

  mat.append([x.strip() for x in input().split(";")]) # converting into matrix

if n!= 0:

  win = []

  lose = []

  draw = []
  # append teams which won to 'win', which loss to 'lose' , which got tied to 'draw'
  for x in mat:

    if x[2] == 'win':

      win.append(x[0])

      lose.append(x[1])

    if x[2] == 'loss':

      lose.append(x[0])

      win.append(x[1])

    if x[2] == 'draw':

      draw.append(x[0])

      draw.append(x[1])
  # for getting list of teams
  se = []

  for i in mat:

    for elem in i:

      se.append(elem)

  lis_team = list(set(se))

  l1 = list(lis_team)

  if 'win' in l1:

    l1.remove('win')

  if 'draw' in l1:

    l1.remove('draw')

  if 'loss' in l1:

    l1.remove('loss')

  lis_team = l1
  lis_team.sort()  # final list of team

  dic = {}
  # counting of points
  for ele in lis_team:

    dic[ele] = [countX(se,ele),countX(win,ele),countX(draw,ele),countX(lose,ele),3*countX(win,ele) + 0*countX(lose,ele) + 1*countX(draw,ele)]

  dic = sort_d(dic)

  print('{:<23} |{:>3} |{:>3} |{:>3} |{:>3} |{:>3} |'.format('Team','MP','W','D','L','P'))

  for k,v in dic.items():

    table(k,v)

elif n==0:

  print('{:<23} |{:>3} |{:>3} |{:>3} |{:>3} |{:>3} |'.format('Team','MP','W','D','L','P'))

# Code 2:

##a=[]
##b=int(input())
##for i in range(b):
##    a.append(input().split(';'))
##    c=[]
##for i in range(b):
##    for j in range(2):
##        c.append(a[i][j])
##d=set(c)
##c={i:0 for i in d}
##e={i:0 for i in d}
##f={i:0 for i in d}
##g={i:0 for i in d}
##
##for i in range(b):
##    if a[i][2]=='win':
##        c[a[i][0]]+=3
##        
##    elif a[i][2]=='loss':
##    
##        c[a[i][1]]+=3
##    elif a[i][2]=='draw':
##        c[a[i][0]]+=1
##        c[a[i][1]]+=1
##
##for i in a:
##    if i[2]=='win':
##        
##        e[i[0]]+=1
##        g[i[1]]+=1
##    elif i[2]=='loss':
##        g[i[0]]+=1
##        e[i[1]]+=1
##    elif i[2]=='draw':
##        f[i[0]]+=1
##        f[i[1]]+=1
##
###print(e)
###print(f)
###print(g)
##c=[[i,j] for i,j in c.items()]
##c.sort(key=lambda x:x[0],reverse=False)
##c.sort(key=lambda x:x[1],reverse=True)
##
##if b!=0:
##  print('{:<23} |{:>3} |{:>3} |{:>3} |{:>3} |{:>3} |'.format('Team','MP','W','D','L','P'))
##  for i in range(len(c)):
##    print('{:<23} |{:>3} |{:>3} |{:>3} |{:>3} |{:>3} |'.format(c[i][0],e[c[i][0]]+f[c[i][0]]+g[c[i][0]],e[c[i][0]],f[c[i][0]],g[c[i][0]],c[i][1]))
##if b == 0:
##  print('{:<23} |{:>3} |{:>3} |{:>3} |{:>3} |{:>3} |'.format('Team','MP','W','D','L','P'))
