# dfs stack
def dinhthat(n, u, v, e, a):
    visited = [False] * (n + 1)
    st = [u]
    visited[u] = False
    while len(st) > 0:
        top = st.pop()
        if top == v:
            return False
        for i in a[top]:
            if visited[i] == False and i != e:
                st.append(i)
                visited[i] = True
    return True
    
for t in range(int(input())):
    n, m, u, v = map(int, input().split())
    a = {}
    for i in range(1, n + 1):
        a[i] = []
    for i in range(m):
        x, y = map(int, input().split())
        a[x].append(y)
    
    cnt = 0
    for i in range(1, n + 1):
        if i != u and i != v and dinhthat(n, u, v, i, a):
            cnt += 1
    print(cnt)