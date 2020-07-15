n = int(input())
s = input().split()
exist = [False for i in range(n)]
data = []
for i in s:
    data.append(int(i))
for i in data:
    exist[i-1] = True
# print(data)
# print(exist)
for i in range(len(exist)):
    if exist[i] == False:
        print(i+1)