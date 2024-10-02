from collections import deque
def sliding_window(arr,k):
#deque is used to store the indices of the array elements
    result=[]
    dq=deque()
    for i in range(len(arr)):
        if dq and dq[0]<i-k+1:
#it will remove the indices which has value greater than k
            dq.popleft()
#in while statement it will remove the elements if they are smaller or = to current element
        while dq and arr[dq[-1]]<=arr[i]:
            dq.pop()
            #add the current element index at the back of deque
        dq.append(i)
#append the front element of the deque to the result when we have a complete window
        if i>=k-1:
            result.append(arr[dq[0]])
    return result
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window(arr, k))   