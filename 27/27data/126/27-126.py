# Решение на 2 балла
# Автор: К. Багдасарян

with open('27-126b.txt') as f:
    n = int(f.readline())
    d = [0] * n
    for i in range(n):
        a,b = f.readline().split()
        d[i] = int(b)

st = []
mx = 0
for i in range(n-1,-1,-1):
    while len(st) > 0 and st[-1][0] <= d[i]:
        st.pop()
    if len(st) > 0:
        r = st[-1][1] - i
        if r > mx:
            mx = r
    st.append((d[i],i))
print(mx)

