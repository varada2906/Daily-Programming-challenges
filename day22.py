from collections import defaultdict

def element_to_repeat_k_times(arr, k):
    # Dictionary to store the frequency of each element
    frequency = defaultdict(int)#defaultdict to store the frequency of each element
    
    # Traverse the array and count frequencies
    #first to record frequency of each element
    for num in arr:
        frequency[num] += 1
    
    # Traverse the array again and check the frequency
    #second to find the first element with frequency equal to k
    for num in arr:
        if frequency[num] == k:
            return num
    
   #if no element is found it will return -1
    return -1


arr = [3, 1, 4, 4, 5, 2, 6, 1, 4]
k = 2
print(element_to_repeat_k_times(arr, k))  # Output: 1
