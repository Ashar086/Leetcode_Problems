class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
    
        for char in s:
            if char == ')':
                # Pop from the stack until we find an opening parenthesis
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the opening parenthesis
                stack.pop()
                # Add the reversed substring back to the stack
                stack.extend(temp)
            else:
                stack.append(char)
    
        # Join the characters in the stack to form the final string
        return ''.join(stack)