
def printLeader(arr, n):
    for i in range(n):
        k = False
        for j in range(i+1, n):
            if(arr[i] <= arr[j]):
                k = True
                break
        else: # If loop did not break
            print(arr[i], end=' ')


# Driver function
arr = [16, 17, 4, 3, 5, 2]
printLeader(arr, len(arr))




    