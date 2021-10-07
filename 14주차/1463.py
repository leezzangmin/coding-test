import sys
N=int(input())

s=[0] * (N+2)
if N==1:
    print(0)
    sys.exit()
elif N==2:
    print(1)
    sys.exit()
elif N==3:
    print(1)
    sys.exit()

s[1],s[2],s[3]=0,1,1

for i in range(4,N+1):
    if (i%2==0 and i%3==0):
        s[i] = min( s[int(i/2)] + 1, s[int(i/3)] + 1 )
    elif i%2==0:
        s[i] = s[int(i/2)] + 1
    elif i%3==0:
        s[i] = s[int(i/3)] + 1
    else:
        s[i] = s[i-1] + 1
    s[i]=min(s[i],s[i-1]+1)

print(s[N])
