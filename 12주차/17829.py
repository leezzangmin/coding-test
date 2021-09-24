import sys
input=sys.stdin.readline
N=int(input())

square=[ list(map(int,input().split())) for _ in range(N) ]


def select(x,y):
    l=[square[x][y],square[x][y+1],square[x+1][y],square[x+1][y+1]]
    l.sort()
    return(l[2])



while True:
    if len(square)==1:
        break
    pulling=[]
    for i in range(0,len(square),2):
        temp=[]
        for j in range(0,len(square),2):
            temp.append(select(i,j))
        pulling.append(temp)
    square=pulling

print(square[0][0]) 