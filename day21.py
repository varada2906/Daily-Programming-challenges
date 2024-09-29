def reverse_stack(stack):
    # if stack is empty, return
    if not stack:
        return
    
    # Pop the top element and store it
    top_element = stack.pop()
    
    # reverse the remaining stack
    reverse_stack(stack)
    
    # Insert the popped element at the bottom
    insert_at_stack(stack, top_element)

def insert_at_stack(stack, element):
    # if stack is empty, push the element at the bottom
    if not stack:
        stack.append(element)
        return
    
    # Pop the top element
    top_element = stack.pop()
    
    # Recursively insert the element at the bottom
    insert_at_stack(stack, element)
    
    # Push the popped element back
    stack.append(top_element)

# Example usage:
stack = [3, 1, 4, 2]
reverse_stack(stack)
print(stack)  # Output: [2, 4, 1, 3]


"""reverse_stack(stack) function is used to pop the top 
  element and then recursively to reverse the stack .once the stack is empty it starts inserting the stack """