def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    
    # Traverse from the last element of arr1 and first element of arr2
    for i in range(m-1, -1, -1):
        # If the current element of arr1 is greater than the first element of arr2, swap them
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            
            # After swapping, sort arr2 to maintain sorted order
            first = arr2[0]
            k = 1
            # Insert arr2[0] into its correct position in arr2
            while k < n and arr2[k] < first:
                arr2[k-1] = arr2[k]
                k += 1
            arr2[k-1] = first

# Example usage:
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merge(arr1, arr2)
print("arr1:", arr1)
print("arr2:", arr2)