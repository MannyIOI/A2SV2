def superDigit(n, k):
    if len(n) <= 1:
        return n
    else:
        # find sum of digits of n
        digit_sum = 0
        for i in n:
            digit_sum += int(i)
        
        digit_sum = digit_sum * k
        print(digit_sum)
        
        return superDigit(str(digit_sum), 1)