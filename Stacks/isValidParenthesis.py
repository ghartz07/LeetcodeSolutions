class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if(item == '(' or item == '[' or item == '{'):
                stack.append(item)
            elif(stack):
                twin = stack.pop()
                if (twin == '(' and item != ')'
                 or twin == '[' and item != ']'
                  or twin == '{' and item != '}'):
                    return False
            else: return False

        if (stack):
            return False
        else: return True