n,l = map(int,input().split())
pipe = sorted(list(map(int,input().split())))
p = pipe[0]
cnt = 1
for i in pipe:
    leng = p+l-1
    if i <= leng:
        continue
    else:
        p = i
        cnt += 1
print(cnt)