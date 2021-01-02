# assumption num1 maybe greater in digits than num2 but num2 is not greater in digits than num1
# num1 has to be greater than num2

def bigSum(num1: str, num2: str):
    carry = 0
    val = ''

    num1:list = list(num1)
    num2:list = list(num2)

    both_positive = True

    if num1[0] == '-':
        num1 = num1[1: len(num1)]
        both_positive = not both_positive

        if num2[0] != '':
            print(num1, num2)
            if len(num2) > len(num1):
                return bigSum(''.join(num2), ''.join(num1))

            for i in range(len(num1)):
                if num1[i] < num2[i]:
                    return '-' + bigSum(''.join(num2), ''.join(num1))

    if num2[0] == '-':
        num2 = num2[1: len(num2)]
        both_positive = not both_positive
    else:
        if not both_positive:
            # if len(num2) > len(num1):
            #     return bigSum(''.join(num2), ''.join(num1))

            # if len(num2) == len(num1):
            #     return 

            return bigSum(''.join(num2), ''.join(num1))

    # go reverse
    for i in range(len(num1) - 1, -1, -1):
        num1_int = int(num1[i])
        num2_int = int(num2[i])

        if both_positive: curr_val = num1_int + num2_int + carry
        else:
            if num1_int < num2_int:
                num1_int = num1_int + 10
                num1[i-1] = str(int(num1[i-1]) - 1)

            curr_val = num1_int - num2_int

        if curr_val > 9 and i > 0:
            carry = curr_val // 10
            curr_val = curr_val % 10
        

        # use lists instead of concatenation for Big O optimization
        val = str(int(str(curr_val) + val))
    
    return val

# print(bigSum('1', '9')) # 10
# print(bigSum('15', '25')) # 40
# print(bigSum('92', '-87')) # 5
# TODO: flip to 97 - 80 then negate
print(bigSum('-97','80')) # -17

# print(bigSum('80', '-97')) # -17

# print('80', '-97')