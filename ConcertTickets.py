import bisect
n,m = map(int,input().split())
prices = list(map(int,input().split()))
prices.sort()
maxPrices = list(map(int,input().split()))
used = [False for i in range(n)] 
for i in range(m):
    found = False
    pt = bisect.bisect_left(prices,maxPrices[i])
    if prices[pt] == maxPrices[i]:
        print(prices[pt])
        prices.pop(pt)
    elif pt == 0:
        print(-1)
    else:
        print(prices[pt-1])
        prices.pop(pt-1)
        