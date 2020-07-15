n = int(input())
while True:
  if n == 1:
    print(int(n),end=" ")
    break
  elif n%2 == 0:
    print(int(n),end=" ")
    n /= 2
  else:
    print(int(n),end=" ")
    n *= 3
    n += 1
  
