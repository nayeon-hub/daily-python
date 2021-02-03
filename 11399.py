num = int(input())
m = input().split()

m1 = list(map(int, m))
m1.sort()
new = []
sum_s = 0
sum_m = 0

for i in range(0, len(m1)):
    sum_m = sum_m + m1[i]
    new.append(sum_m)
    i = i+1
for i in range(0, len(new)):
    sum_s = sum_s + new[i]
print(sum_s)
