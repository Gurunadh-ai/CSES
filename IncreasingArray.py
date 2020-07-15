n = int(input())
s = input().split()

res = 0
for i in range(len(s)):
    res -= min(0, int(s[i])-int(s[max(i-1,0)]))
    if int(s[i]) < int(s[i-1]):
        s[i] = s[i-1]
print(res)