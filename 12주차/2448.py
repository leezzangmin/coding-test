import math
 
s = ["  *   ", " * *  ", "***** "]
 
def makeStar(shift):
    c = len(s)
    for i in range(c):
        s.append(s[i] + s[i]) #현 단계 삼각형을 뒤에 붙이고
        s[i] = ("   " * shift + s[i] + "   " * shift) #현 단계 삼각형을 오른쪽으로 민다
 
n = int(input())
k = int(math.log(int(n / 3), 2))
for i in range(k):
    makeStar(int(pow(2, i)))
 
for i in range(n):
    print(s[i])
