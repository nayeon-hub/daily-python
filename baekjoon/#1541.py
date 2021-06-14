n = input().split('-')
p = [i.split('+') for i in n]
result = 0
for i in p[0]:
    result += int(i)
for j in p[1:]:
    for k in j:
        result -= int(k)
print(result)