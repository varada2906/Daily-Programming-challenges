def reverse_words(string):
#split words in the given string and reverse the string
    reversed_words=string.split()[::-1]
#join the reversed words into a single string
    return " ".join(reversed_words)
string="the sky is blue"
print(reverse_words(string))
