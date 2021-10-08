import sys
input=sys.stdin.readline
N=int(input())
s = list(list(map(int,input().split())) for _ in range(N))
dp=[0]*(N+1)

cmax = 0
for i in range(N):
    cmax = max(cmax,dp[i])
    if i+s[i][0] > N:
        continue
    dp[i+s[i][0]] = max(cmax+s[i][1], dp[i+s[i][0]])
print(max(dp))