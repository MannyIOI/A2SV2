class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        arr = [0] * len(T)
        stack = [len(T) - 1]
        
        for i in range(len(T) - 2, -1, -1):
            # case 1 -> our stack is empty -> add elements to the stack
            # case 2 -> when our element is less than or equal to the top of the stack -> pop till you get the greater element
            # case 3 -> when our element is greater than the top of the stack
            if len(stack) == 0:
                stack.append(i)
            
            print(T[i] >= T[stack[-1]])
            while len(stack) > 0 and T[stack[-1]] <= T[i]:
                # pop elemnts from our stack
                stack.pop()
            
            if len(stack) == 0:
                stack.append(i)
                continue
                
            if T[stack[-1]] > T[i]:
                arr[i] = stack[-1] - i
                stack.append(i)
            
            
        return arr