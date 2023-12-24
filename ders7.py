# 5 = 5.4.3.2.1 = 120
# 4 = 4.3.2.1

# range(5,1,-1)

n = 5

faktor = 1

for i in range(n,0,-1):
    print(i)
    faktor *= i

print(faktor)