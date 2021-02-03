a = input().split()
print(a)
b = list(map(int, a))
if (b == [1, 2, 3, 4, 5, 6, 7, 8]):
    print("ascending")
elif (b == [8, 7, 6, 5, 4, 3, 2, 1]):
    print("descending")
else:
    print("mixed")

# a=list(map(int,input().split()))

# if a==sorted(a):
#     print("ascending")
# elif a==sorted(a, reverse=True):
#     print("descending")
# else: print("mixed")

# -feedback-
# input().split 과 a=input() a.split의 차이
# input().split()라는 의미: 사용자 입력값을 split()공백으로 구분하여 저장
# a=input() a.split()은 a.split()실행은 되지만 그 값은 변수에 저장이 안되었으니 무용지물
# 추가 : print(list(a))는 문자열 하나하나를 다 자름
# ex) 1 23 print(list(a))는 ['1',' ','2','3']
