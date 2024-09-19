from itertools import permutations
#itertools:Functions creating iterators for efficient looping.
 	
def string_permutations(s):
    # Generate all permutations using itertools module
    permutation = permutations(s)
    
    perm_list = [''.join(p) for p in permutation]
    
    return perm_list


s = "abc"
result = string_permutations(s)
print(result)
