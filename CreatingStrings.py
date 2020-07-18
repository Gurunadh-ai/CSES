from itertools import permutations as x
p = sorted(list(set(x(input()))))
print(len(p))
for i in p:
    for j in i:
        print(j,end="")
    print()