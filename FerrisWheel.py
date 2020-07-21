n,x = map(int,input().split())
wt = list(map(int,input().split()))
wt.sort(reverse=True)
count = 0
i = 0
j = n-1
while i<=j:
    if j-i+1 == 1 or wt[i]+wt[j] > x:
        count += 1
        i += 1
    elif(wt[i]+wt[j] <= x):
        count += 1
        i += 1
        j -= 1
print(count)
            