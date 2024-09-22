from collections import defaultdict

def KDistinct(s, k):
    def KDistinct(s, k):
        count = 0
        left = 0
        var = defaultdict(int)#default dict defines the value for new keys.it is a empty dictionary
        
        for right in range(len(s)):
            var[s[right]] += 1
            
            # If the number of distinct characters exceeds k, move the left pointer
            while len(var) > k:
                var[s[left]] -= 1
                if var[s[left]] == 0:
                    del var[s[left]]
                left += 1
            
            # Add the number of substrings ending at 'right' that have at most k distinct characters
            count += (right - left + 1)
        
        return count
    
    # Result is the difference between substrings with at most k distinct characters
    # and at most (k-1) distinct characters
    return KDistinct(s, k) - KDistinct(s, k-1)

# Example usage:
s = "pqpqs"
k = 2
result = KDistinct(s, k)
print(result)

""" in this code we count the substrings using KDistinct function it increments to right and decrements to left when it 
exceeds the value of k.it calculates the difference b/w k and k-1.the difference will give the substrings of k """