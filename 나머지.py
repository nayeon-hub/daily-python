list = []
for i in range(0, 10):
    a = int(input())
    x = a % 42
    if (x in list) == False:
        list.append(x)
print(len(list))

# -Feedback-
# list가 아닌 set을 쓴 이유 : set 집합은 중복이 자동으로 제거됨
# 그렇다면 굳이 if문이 없어도 됬음
