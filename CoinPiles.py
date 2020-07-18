t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if (x+y)%3 == 0:
        if min(x,y) <= 2*(x+y)/3 and min(x,y) >= (x+y)/3:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
