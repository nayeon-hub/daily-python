import math
m,n = map(int,input().split())
for i in range(m,n+1):
    check = True
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            check = False
            break
    if check == True:
        print(i)

# 제곱근 만큼!