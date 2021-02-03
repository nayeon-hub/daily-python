#내가 푼 방법
n = int(input())
for i in range(1,n+1):
    x = 2*i-1
    y = (2*n-1-x)//2
    print((" "*y)+("*"*x))


#해답
n=int(input())
for i in range(1,n+1):
    print((' '*(n-i))+('*'*(2*i-1)))