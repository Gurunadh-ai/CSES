n = int(input())
wt = list(map(int,input().split()))
su = sum(wt)
res = su
from itertools import combinations
for i in range(1,n):
    comb = list(combinations(wt,i))
    for i in comb:
        if su-2*sum(i) >= 0:
            res = min(res, su-2*sum(i))
print(res)