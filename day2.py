def missing_number(n,arr):
    array_sum=sum(arr)
    total_sum=(n*(n+1)) // 2
    return total_sum-array_sum
arr=[1,2,4,5]
n=5
print(missing_number(n,arr))
