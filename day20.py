def sort_stack(stack):
    # Base case: If the stack is empty, return
    if not stack:
        return
    
    # Remove the top element
    top = stack.pop()
    
    # Recursively sort the remaining stack
    sort_stack(stack)
    
    # Insert the top element back in sorted order
    insert_the_ele(stack, top)

def insert_the_ele(stack, element):
    # If the stack is empty or the element is greater than the top, push the element
    if not stack or stack[-1] <= element:
        stack.append(element)
        return
    
    # Remove the top element
    top = stack.pop()
    
    # Recursively call to find the right position for the element
    insert_the_ele(stack, element)
    
    # Push the removed element back
    stack.append(top)


stack = [3, 1, 4, 2]
sort_stack(stack)
print(stack)  # Output: [1, 2, 3, 4]