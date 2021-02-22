class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i =='[' or i == '{':            
                stack = [i] + stack
            else:
                if len(stack) == 0:
                    return False
                con = stack[0] + i
                if con == '()' or con == '[]' or con == '{}':
                    stack.pop(0)
                else:
                    return False

        return len(stack) == 0