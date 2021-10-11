N=int(input())
s=list(map(int,input().split()))
dp=[1]*(N+1)

for i in range(1, N):
    for j in range(i):
        if s[i]>s[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

order = max(dp)
arr = []
for i in range(N-1, -1, -1):
    if dp[i]==order:
        arr.append(s[i])
        order-=1
        
arr.reverse()
for i in arr:
    print(i, end=' ')