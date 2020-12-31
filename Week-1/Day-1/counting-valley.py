#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    level = 0
    count = 0
    for i in path:
        level = level + 1 if i == "U" else level - 1
        if level == 0 and i == "U":
            count += 1
        
    return count
