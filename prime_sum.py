class Solution:
	# @param A : integer
	# @return a list of integers
	def primesum(self, A):
		n = A
		p=2
		isPrime = [True for i in range(n+1)]
		isPrime[0] = isPrime[1] = False
		while p*p < n:
			if isPrime[p] == True:
				for i in range(p*p,n+1,p):
					isPrime[i] = False
			p+=1
		for i in range(0,n):
			if isPrime[i] and isPrime[n-i]:
				return(i,n-i)
s = Solution()
print(s.primesum(184))


