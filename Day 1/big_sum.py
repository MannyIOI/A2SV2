# assumption num1 maybe greater in digits than num2 but num2 is not greater in digits than num1

def bigSum(num1: str, num2: str):
    carry = 0
    val = ''
    # go reverse
    for i in range(len(num1) - 1, -1, -1):
        num1_int = int(num1[i])
        num2_int = int(num2[i])

        curr_val = num1_int + num2_int + carry

        if curr_val > 9 and i > 0:
            curr_val = curr_val // 10
            carry = curr_val % 10
        
        # use lists instead of concatenation for Big O optimization
        val = str(curr_val) + val
    
    return val

print(bigSum('1', '9')) # 10