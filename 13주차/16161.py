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
        if sequence[i:j] == sequence[j+j-i-1:j-1:-1]:
            res=max(res,(j-i)*2)
        i+=1
        j=i+1
    else:
        if sequence[i:j] == sequence[j+j-i-2:j-2:-1]:
            res=max(res,(j-i)*2-1)
        i+=1
        j=i+1
 

print(res)


