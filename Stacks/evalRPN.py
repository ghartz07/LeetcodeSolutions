class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item.lstrip('-').isdigit():
                stack.append(int(item))
            else:
                var2 = stack.pop()
                var1 = stack.pop()
                if(item == "+"):
                    stack.append(var1 + var2)
                elif(item == "-"):
                    stack.append(var1 - var2)
                elif(item == "*"):
                    stack.append(var1 * var2)
                else:
                    stack.append(int(var1 / var2))

        return stack.pop()