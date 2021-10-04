import sys
input=sys.stdin.readline
N,S=map(int,input().split())
s=list(map(int,input().split()))


L, R, res, sum = 0, 0, sys.maxsize, 0
while True:
    if sum>=S:
        res=min(res,R-L)
        sum-=s[L]
        L+=1
    elif R==N:
        break
    else:
        sum+=s[R]
        R+=1

if res==sys.maxsize:
    print(0)
else:
    print(res)