series = [0, 6, 28]
attack = 8
n = int(input())
for i in range(4,n+1):
    p = (i**2)*((i**2)-1)/2
    attack += 4*(2*i-4)
    series.append(p - attack)
for i in range(n):
    print(int(series[i]))