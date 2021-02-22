class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for i in logs:
            if i == './':
                continue
            if i != '../':
                stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
        
        return len(stack)