import math 

def longDivision(number, divisor): 
    ans = "" 
    
    idx = 0 
    temp = ord(number[idx]) - ord('0') 
    while (temp < divisor):
        temp = (temp * 10 + ord(number[idx + 1]) - ord('0')) 
        idx += 1 
    
    idx += 1 

    while ((len(number)) > idx):
        ans += chr(math.floor(temp // divisor) + ord('0')) 
        
        # Take next digit of number 
        temp = ((temp % divisor) * 10 + ord(number[idx]) - ord('0'))
        idx += 1

    ans += chr(math.floor(temp // divisor) + ord('0')) 
    
    # If divisor is greater than number 
    if (len(ans) == 0): 
        return "0"
    
    # else return ans 
    return ans

# Driver Code 
number = "525"
divisor = 5
print(longDivision(number, divisor))