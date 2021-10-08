import sys
input=sys.stdin.readline
N,M=map(int,input().split())
grid=list(list(map(int,input().split())) for _ in range(N))
dx=[0,0,1]
dy=[-1,1,0]
dp=[[0]*M for _ in range(N)]
dp[0][0]=grid[0][0]
visit=[[0]*M for _ in range(N)]


def sol(x,y,val):
    #val=max(val,val+grid[x][y])
    val=grid[x][y]
    dp[x][y]=max(dp[x][y],val)
    if x==N-1 and y==M-1:
        return

    for i in range(3):
        mx=dx[i]+x
        my=dy[i]+y
        if 0<=mx<N and 0<=my<M:
            if visit[mx][my]==0:
                visit[mx][my]=1
                sol(mx,my,val)
                visit[mx][my]=0



sol(0,0,0)
print(dp)
