s = input()
count = [0 for i in range(26)]
res = ""
flag = -1
no = False
for i in s:
    count[ord(i)-65] += 1
for i in range(26):
    res += (count[i]//2)*(chr(i+65))
    if count[i]%2 != 0:
        if flag == -1:
            flag = i
            count[i] -= 1
        else:
            print("NO SOLUTION")
            no = True
    count[i] -= count[i]//2
res += chr(flag+65) if flag != -1 else ""
for i in range(25,-1,-1):
    res += (count[i])*(chr(i+65))
if not no: 
    print(res)
    
    
