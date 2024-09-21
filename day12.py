def isValid(s:str):
    stack=[]
    brackets={'(':')','{':'}','[':']'}#dictionary is created,keys:open bracket and values:closed bracket
    #to loop through all characters in string use for loop
    for character in s:
        #for each character we have to check if is a open bracket to check use if
        if character in brackets:
            #if is a open bracket
            stack.append(brackets[character])#returns corresponding closed brackets
        elif  not stack or stack.pop() !=character:#pop returns the topmost element in the stack
            return False
    return not stack
print(isValid("[{()}]"))
#not keyword is used to check whether the stack is empty or not ,it will return true if stack is empty
            