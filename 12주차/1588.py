first=input()
left=int(input())
right=int(input())
N=int(input())



# while N!=0:
#     temp=''
#     for i in range(len(first)):
#         if left<=i**N<=right:
#             if first[i]=='1':
#                 temp+='132'
#             elif first[i]=='2':
#                 temp+='211'
#             elif first[i]=='3':
#                 temp+='232'
#     first=temp
#     print(first)
#     N-=1
# print(first)


for i in range(N):
    temp=''
    for j in range(len(first)):
        if left<=(N-i)**3<=right: