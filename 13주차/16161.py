import sys
input=sys.stdin.readline
N=int(input())
sequence=list(map(int,input().split()))

i,j,res=0,1,1
while j<N:
    if N-i < res:
        break

    if sequence[j-1] < sequence[j]:
        j+=1

    elif sequence[j-1] == sequence[j]:
        f=True
        for index in range(i,j):
            if (j-1)*2 - index+1>=N:
                f=False
                break
            if sequence[index]!=sequence[ (j-1)*2 - index+1 ]:
                f=False
                break
        if f:
            res=max(res,(j-i)*2)
        i+=1
        j=i+1
    else:
        f=True
        for index in range(i,j):
            if (j-1)*2 - index >= N:
                f=False
                break
            if sequence[index]!=sequence[ (j-1)*2 - index ]:
                f=False
                break
        if f:
            res=max(res,(j-i)*2-1)        
        i+=1
        j=i+1
 

print(res)