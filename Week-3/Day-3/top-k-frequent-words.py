import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        
        heap = [(-freq, word) for word, freq in c.items()]
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]