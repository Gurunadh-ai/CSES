from collections import defaultdict
n,m = map(int, input().split())
g = defaultdict(list)
for i in range(m):
    u,v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)
queue = [1]
visited = [False]*(n+1)
parent = [-1]*(n+1)
visited[1] = True
while queue:
    s = queue.pop(0)
    for i in g[s]:
        if not visited[i]:
            visited[i] = True
            parent[i] = s
            queue.append(i)
i = n
arr = []
while parent[i] != -1:
    arr.append(i)
    i = parent[i]
if i != 1:
    print("IMPOSSIBLE")
else:
    arr.append(1)
    print(len(arr))
    for i in reversed(arr):
        print(i,end=" ")