#2437번 저울 - 그리디 알고리즘

n = int(input())
li = sorted(list(map(int,input().split(' '))))
num = 0
while True:
    num += 1
    for i in range