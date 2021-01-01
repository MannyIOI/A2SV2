from big_sum import bigSum

from big_sum import bigSum
# assumption num1 maybe greater in digits than num2 but num2 is not greater in digits than num1

def big_multiply(num1: str, num2: str):
    carry = 0
    val = ''
    addables = []
    positive = True

    if num1[0] == '-':
        num1 = num1[1: len(num1)]
        positive = not positive

    if num2[0] == '-':
        num2 = num2[1: len(num2)]
        positive = not positive


    # multiplication phase
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num1) - 1, -1, -1):
            num1_int = int(num1[i])
            num2_int = int(num2[j])

            curr_val = (num1_int * num2_int) + carry

            if curr_val > 9 and j > 0:
                carry = curr_val // 10
                curr_val = curr_val % 10
            
            val = str(curr_val) + val

            if j == 0:
                addables.append(val)
                carry = 0
                val = ''
    
    val = bigSum(addables[1] + '0', '0'+addables[0])
    if not positive: val = '-' + val
    
    return val

def karatsuba(num1: str, num2: str):
    positive = True

    if num1[0] == '-':
        num1 = num1[1: len(num1)]
        positive = not positive

    if num2[0] == '-':
        num2 = num2[1: len(num2)]
        positive = not positive
    
    if len(num1) < 2 or len(num2) < 2:
        return str(int(num1) * int(num2))

    mid = min(len(num1) // 2, len(num2) // 2)

    high1, low1 = num1[:mid], num1[mid:]
    high2, low2 = num2[:mid], num2[mid:]

    z0 = int(karatsuba(low1, low2))
    z1 = int(karatsuba(str(int(low1) + int(high1)), str(int(low2) + int(high2))))
    z2 = int(karatsuba(high1, high2))

    return z2 * (10 ** (2 * mid)) + ((z1 - z2 - z0) * (10 ** mid)) + z0
# print(big_multiply('87', '92'))
print(karatsuba('87', '92'))