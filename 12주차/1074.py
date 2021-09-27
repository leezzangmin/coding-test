import sys
import time
N,r,c=map(int,input().split())


res=0

while N>=0:
    square=int((2**(N) * 2**(N)) /4)
    if r >= (2**(N))/2:
        if c>=(2**(N))/2: #4
            res+=square*3
            r-= 2**(N-1)
            c-=2**(N-1)
        else: #3
            res+=square*2
            r-=2**(N-1)

    else:
        if c>=(2**(N))/2: #2
            res+=square
            c-=2**(N-1)
        else: #1
            pass
    
    N-=1

print(res)
