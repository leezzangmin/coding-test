import sys
input=sys.stdin.readline
N=int(input())
square=[list(map(int,input().split())) for _ in range(N)]

white=0
blue=0

def divide(NN,x,y):
    global white,blue
    temp=square[x][y]
    for i in range(x,x+NN):
        for j in range(y,y+NN):
            if square[i][j]!=temp:
                divide(NN//2,x,y)
                divide(NN//2,x+NN//2,y)
                divide(NN//2,x,y+NN//2)
                divide(NN//2,x+NN//2,y+NN//2)
                return

    if temp==0:
        white+=1
        return
    else:
        blue+=1
        return

divide(N,0,0)
print(white)
print(blue)

