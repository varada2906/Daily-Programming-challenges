def findRepeating(arr,N):
    for i in range(N):
        for j in range(i+1,N):
            if(arr[i]==arr[j]):
                return arr[i]
if __name__=="__main__":
    arr=[3,1,4,3,2]
    N=len(arr)

print(findRepeating(arr,N))