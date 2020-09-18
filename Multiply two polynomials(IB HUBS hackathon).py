# Sample Input:
##4
##0 5
##1 0
##2 10
##3 6
##3
##0 1
##1 2
##2 4

n = int(input().strip())
l1 = []
for _ in range(n):
    inp = input().split(' ')
    l1.insert(int(inp[0]),int(inp[1]))
m = int(input().strip())
l2 = []
for _ in range(m):
    inp = input().split(' ')
    l2.insert(int(inp[0]),int(inp[1]))
req = []
for i in range(len(l1)):
    req.append([l1[i]*l2[j] for j in range(len(l2))])
hi_p = [req[n-1][m-1],n+m-2]
low_p = [req[0][0],0]

r1 = []
r1.append(low_p)
for k in range(1,m+n-2):
    a = 0
    for i in range(n):
        for j in range(m):
            if i+j == k:
                a = a +req[i][j]
    r1.append([a,k])
r1.append(hi_p)
a = str(r1[::-1][0][0])+'x^'+str(r1[::-1][0][1])+' '
for i in range(1,len(r1)):
    if r1[::-1][i][1] == 0 and r1[::-1][i][0] > 0:
        a = a + '+'+' ' + str(r1[::-1][i][0])
    elif r1[::-1][i][1] == 0 and r1[::-1][i][0] < 0:
        a = a + '-'+' ' + str(abs(r1[::-1][i][0]))
    elif r1[::-1][i][0] != 0 and r1[::-1][i][0] > 0:
        a = a + '+' +' '+ str(r1[::-1][i][0])+'x^'+str(r1[::-1][i][1])+' '
    elif r1[::-1][i][0] != 0 and r1[::-1][i][0] < 0:
        a = a + '-' +' '+str(abs(r1[::-1][i][0]))+'x^'+str(r1[::-1][i][1])+' '
print(a)
