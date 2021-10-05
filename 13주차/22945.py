N=int(input())
s=list(map(int,input().split()))

L,R=0,N-1
ans=0

while True:
   # print(L,R,'adf')
    if R>=N or L>=N:
        break
    temp=(R-L-1) * min(s[L],s[R])
    
    if s[L]>s[R]:
        R-=1
    else:
        L+=1


    ans=max(temp,ans)
    
print(ans)

# 10
# 1 2 3 4 5 6 7 8 9 10