n = int(input())
s = ""
if n < 4 and n > 1:
    print("NO SOLUTION")
else:
    for i in range(n):
        if i%2 != 0:
            print(i+1,end=" ")
        else:
            s += str(i+1) + " "
    print(s)