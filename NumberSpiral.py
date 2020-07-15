def solve(x,y):
    if x == y:
        res = (x-1)**2+x
    elif x > y:
        res = (x-1)**2
        if x%2 == 0:
            res += y
        else:
            res += 2*x-y
    else:
        res = (y-1)**2
        if y%2 != 0:
            res += x
        else:
            res += 2*y-x
    print(res)
t = int(input())
for i in range(t):
    y,x = map(int,input().split())
    solve(x,y)