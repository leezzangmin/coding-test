N=int(input())



count = N // 5
b = N % 5

while b % 3 != 0:
    b+=5
    count-=1

if b>N:
    print(-1)
else:
    count += b // 3
    print(count)