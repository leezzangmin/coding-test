import sys
input=sys.stdin.readline
N,M=map(int,input().split())
s=list(map(int,input().split()))

sum,temp=[0],0
for i in range(N):
    temp+=s[i]
    sum.append(temp)

res=0
for i in range(N+1):
    for j in range(i):
        if sum[i]-sum[j]==M:
            res+=1
print(res)