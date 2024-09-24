#res=cursive function is used to return gcd of a and b
def gcd(N,M):
    if N == 0:
        return M
    return gcd(M%N,N)
#function to retrun lcm of two numbers
def lcm(M,N):
    return(N//gcd(N,M))*M
N=4
M=6
print('Lcm of',N,'and',M,'is',lcm(N,M))
