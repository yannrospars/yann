import sys
sys.argv
n = int(sys.argv[1]) 
somme = 0
 
for i in range(1, n):
    if n % i == 0:
        somme += i
if somme == n :
    print(f" le nombre : {n} est parfait" ) 
else :
    print(f" le nombre : {n} n'est pas parfait" ) 
 
 

