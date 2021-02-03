def sugar(N):
    for y in range((N//3)+1):
        for x in range((N//5)+1):
            if ((5*x + 3*y) == N):
                return x+y
    return -1


N = int(input())
print(sugar(N))


# before
# ex) 5x + 3y=18

# m = 1
#  while 1:
#       y = s - 5 * m
#        if y > 0:
#             if y % 3 == 0:
#                 print(y//3+m)
#                 break
#         else:
#             if s % 3 == 0:
#                 print(s//3)
#                 break
#             else:
#                 print(-1)
#                 break
#         m = m + 1
