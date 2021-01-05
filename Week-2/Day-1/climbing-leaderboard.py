def binary_search(array, number):
    left = 0
    right = len(ranked) - 1
    mid = (right + left) // 2
    while right > left:
        if mid == len(array):
            break
        if number < array[mid]:
            # right search
            left = mid + 1
            mid = (right + left) // 2
        elif number > array[mid]:
            # left search
            right = mid
            mid = (right + left) // 2
        else:
            return mid + 1
    if mid == 0: return 1
    return mid + 2

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked_2 = []
    # make ranked items appear only once
    for i in ranked:
        if len(ranked_2) > 0 and ranked_2[len(ranked_2) - 1] == i:
            continue
        ranked_2.append(i)
    
    ranked = ranked_2
    answer = []

    for i in player:
        answer.append(binary_search(ranked, i))

    return answer

        
ranked = [100, 100, 50, 40, 40, 20, 10, 5]
player = [5, 25, 50, 120]

climbingLeaderboard(ranked, player)

# #binary_search

# some fails