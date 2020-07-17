n = int(input())
if (n*(n+1)/2)%2 == 0:
    print("YES")
    if n%4 == 3:
        r = [3]
        print(2+2*(n//4))
        print("1 2",end=" ")
        for i in range(4,n+1,4):
            print(i,end=" ")
            print(i+3,end=" ")
            r.append(i+1)
            r.append(i+2)
        print()
        print(len(r))
        for i in r:
            print(i,end=" ")
    else:
        print(2*(n//4))
        r = []
        for i in range(1,n+1,4):
            print(i,end=" ")
            print(i+3,end=" ")
            r.append(i+1)
            r.append(i+2)
        print()
        print(2*(n//4))
        for i in r:
            print(i,end=" ")
else:
    print("NO")