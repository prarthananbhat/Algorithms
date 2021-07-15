import math
import time
class Solution:
	# @param A : integer
	# @return a list of integers
    def allFactors_1(self, A):
        ''' O(N) complexity'''
        factor_list = []
        n = int(A/2)
        for i in range(1,n+1):
            if A % i == 0:
                factor_list.append(i)
        factor_list.append(A)
        return factor_list

    def allFactors_2(self,A):
        '''O(sqrt(N)) complexity'''
        factor_list_1 = []
        factor_list_2 = []
        i = 1
        while i <= math.sqrt(A):
            if A % i == 0:
                factor_list_1.append(i)
                if i != A / i:
                    factor_list_2.insert(0,int(A/i))
            i = i + 1
        return factor_list_1+factor_list_2

S = Solution()
N=1235578
start_time = time.time()
res = S.allFactors_1(N)
print(res)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
res = S.allFactors_2(N)
print(res)
print("--- %s seconds ---" % (time.time() - start_time))


