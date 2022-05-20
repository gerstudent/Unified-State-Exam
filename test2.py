n = int(input())
cnt = 0
list = [x for x in input().split()]
rec = list[0]
for i in range(len(list)):
    if list[i] > rec:
        cnt += 1
        rec = list[i]
print(cnt)




