N,K=map(int,input().split())
sequence=list(map(int,input().split()))
M=max(sequence)+1
number=[0 for _ in range(M)]

i,j=0,0
length=0
while j<N:
    if number[sequence[j]]==K:
        number[sequence[i]]-=1
        i+=1
    else:
        number[sequence[j]]+=1
        j+=1
    length=max(length,j-i)

print(length)




