import math
def E(y,n):
    A = (y/(y+n))  #yes的比例
    B = (n/(y+n))  #no的比例
    sum = -A*math.log(A,2) +  -B*math.log(B,2) #算I混亂值
    return sum

print(E(2,2))
print(E(2,4))
print(E(1,3))
R = 4/14*E(2,2) + 6/14*E(2,4) + 4/14*E(1,3)  #算E
print("R= %f"%R)
IG = 0.940 - R  # Gain = I - E
print("IG= %f"%IG)
print("jk99")
