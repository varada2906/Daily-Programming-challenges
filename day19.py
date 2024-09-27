def evaluate_postfix(expression):
    stack = []

    # Iterate through each token in the postfix expression
    for token in expression:
        # If the token is a number, push it to the stack
        if token.isdigit():
            stack.append(int(token))
        else:
            # Pop the top two numbers from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Apply the operator and push the result back to the stack
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
            elif token == '^':
                stack.append(operand1 ** operand2)
    return stack.pop()
expression = "231*+9-"
print("The result of the postfix expression is:", evaluate_postfix(expression))
""" push operands onto the stack.pop the required number of operands off the stack"""