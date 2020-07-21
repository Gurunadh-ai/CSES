n,m = map(int,input().split())
building = [[1 for i in range(m)]for j in range(n)] #1 is wall, 0 is floor
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == ".":
            building[i][j] = 0
def travel_room(building,i,j):               #after we visit a room once, we will be marking it as wall for future visits
    if i+1<n and building[i+1][j] != 1: #down
        building[i+1][j] = 1                 # mark it as wall and travel the remaining connected floors
        building = travel_room(building,i+1,j)
    if j+1<m and building[i][j+1] != 1: #right
        building[i][j+1] = 1                 
        building = travel_room(building,i,j+1)
    if i-1>=0 and building[i-1][j] != 1: #up
        building[i-1][j] = 1                 
        building = travel_room(building,i-1,j)
    if j-1>=0 and building[i][j-1] != 1: #left
        building[i][j-1] = 1                 
        building = travel_room(building,i,j-1)
    return building
count = 0
for i in range(n):
    for j in range(m):
        if building[i][j] == 0:
            count += 1
            building[i][j] = 1
            building = travel_room(building,i,j)
print(count)