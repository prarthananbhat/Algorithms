n= 16
p=2
isPrime = [True for i in range(n+1)]
print(isPrime)

while p*p < n:
    if isPrime[p] == True:
        for i in range(p*p,n+1,p):
            isPrime[i] = False
        p+=1
prime_list = []
for p in range(2,n+1):
    if isPrime[p]:
        prime_list.append(p)
print(prime_list)

#SieveOfEratosthenes