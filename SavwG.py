for _ in range(int(input())):
    ln = int(input())
    l = list(map(int, input().split()))
s = 0
st = [l[0]]
for i in range(1, ln):
    while len(st) > 0 and l[i] > st[-1]:
        st.pop()
        s += l[i]
    st.append(l[i])
print(s)
