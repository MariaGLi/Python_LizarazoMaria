n=[4, 1, 2, 2, 3]
k=10
t=4
cont=0
L=len(n)

for g in range (t):
    for i in range (L):
        for j in range (L):
            if  n[i]<=n[j] and 1<=n[i] and j<=(L) and i != j:
                if  (n[i]+n[j]) % k == 0:
                    if cont < t:
                        print(n[i], n[j])
                    cont=cont+1
        
         