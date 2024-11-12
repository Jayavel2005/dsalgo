def postfixEval(string):
    formatted = string.replace(" ","")
    stack = []

    for char in formatted:
        if char.isdigit():
            stack.append(int(char))

        else:
            if len(stack) < 2:
                return "Invalid Expression"
            rightOperand = stack.pop()
            leftOperand = stack.pop()
            if char == "+":
                stack.append(leftOperand + rightOperand)
            elif char == "-":
                stack.append(leftOperand - rightOperand)
            elif char == "*":
                stack.append(leftOperand * rightOperand)
            elif char == "/":
                stack.append(leftOperand / rightOperand)
            else:
                return "Invalid Operator"
    return stack[0] if len(stack) == 1 else "Invalid Expression: Too many operands"


exp = "5 3 2 * + 9 - "
print(postfixEval(exp))


# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if self.is_empty():
#             return None
#         return self.stack.pop()
    
#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.stack[-1]
    
#     def is_empty(self):
#         return len(self.stack) == 0
    
#     def evaluate(self, string):
#         formatted = string.replace(" ","")
#         for token in formatted:
#             if token.isdigit():
#                 self.push(int(token))

#             else:
#                 if len(self.stack) < 2:
#                     return "Invalid Expression"
                
#                 rightOperand = self.pop()
#                 leftOperand = self.pop()

#                 if token == "+":
#                     self.push(leftOperand + rightOperand)
#                 elif token == "-":
#                     self.push(leftOperand - rightOperand)
#                 elif token == "*":
#                     self.push(leftOperand * rightOperand)
#                 elif token == "/":
#                     self.push(leftOperand / rightOperand)
#                 else:
#                     return "Invalid Operator"
                
#         return self.peek() if len(self.stack) == 1 else "Invalid Expression"

# stack = Stack()
# string = "5 3 2 * + 9 -"
# print(stack.evaluate(string))