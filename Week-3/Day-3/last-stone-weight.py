import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: x * -1, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            max_1 = -1 * heapq.heappop(stones)
            max_2 = -1 * heapq.heappop(stones)
            
            if max_1 != max_2:
                heapq.heappush(stones, max_2 - max_1)
        
        if len(stones) == 1:
            return -1 * stones[0]
    
        return 0
        # if 0 items in stones return 0
        # return weight of remaining stone