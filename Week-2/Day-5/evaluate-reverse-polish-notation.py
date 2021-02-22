class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        ans = 0
        if len(tokens) == 1:
            return tokens[0]
        
        for i in tokens:
            if i not in '+-*/':
                stack.append(i)
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                
                ans = self.eval(val2, val1, i)
                stack.append(str(ans))
        
        return ans
    
    def eval(self, second, first, i):
        if i == '/':
            r = (int(second) / int(first))
            if r < 0:
                return str(math.ceil(r))
            else:
                return str(math.floor(r))
        elif i == '*':
            return str(int(second) * int(first))
        elif i == '+':
            return str(int(second) + int(first))
        elif i == '-':
            return str(int(second) - int(first))