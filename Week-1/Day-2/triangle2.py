val = input("Input number: ")

for i in range(0, val * 2, 2):
    output = ' ' * (val) + '*' * (i + 1)
    val = val - 1
    print(output)