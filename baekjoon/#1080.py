# 1080번 행렬 - 그리디 알고리즘
# 문제 핵심 : 행렬변환연산은 3*3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것!
# 모든원소를 뒤집었을 때 바꾸지 못하면 -1 => 무조건 바뀌는게 아님

n,m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
b = [list(map(int,list(input()))) for _ in range(n)]
cnt = 0

def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True

def solve(x,y):
    for i in range(x+3):
        for j in range(y+3):
            a[i][j] = 1 - a[i][j]

for i in range(n-2): #3*3행렬의 (0,0)부분들만 체크해서 뒤집으면 (1-2,1-2)나머지는 자동 뒤집힘
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            cnt += 1
            solve(i,j)

if check():
    print(cnt)
else:
    print(-1)