n,m,k = map(int,input().split())
apart = list(map(int,input().split()))
sizes = list(map(int,input().split()))
sizes.sort()
apart.sort()
sizesi = 0
aparti = 0
count = 0
while sizesi<len(sizes) and aparti<len(apart):
    if abs(apart[aparti]-sizes[sizesi])<= k:
        aparti += 1
        sizesi += 1
        count += 1
    elif apart[aparti]<sizes[sizesi]-k:
        aparti += 1
    elif apart[aparti]>sizes[sizesi]+k:
        sizesi += 1
print(count)