import math

a = 1
num_virus = int(input("enter number of viruses: "))
ans = math.log2(num_virus)
if ans // 1 == ans:
    print(ans)
else:
    print((ans // 1) + 1)