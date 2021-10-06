import sys
input=sys.stdin.readline
N,M=map(int,input().split())
s=[int(input()) for _ in range(N)]
s.sort()

left,right=0,0
ans=sys.maxsize
while left<N-1 and right<N:
 #   print(left,right,'asdf')

    if s[right]-s[left]<M:
        right+=1
    else:
        ans=min(ans,s[right]-s[left])
        if ans==M:
            break
        left+=1
 #       right=left+1
        
print(ans)