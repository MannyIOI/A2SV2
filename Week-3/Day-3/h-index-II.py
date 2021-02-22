class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        left = 0
        right = len(citations) - 1

        while left <= right:
            # if h < citations[i]:
            #     h += 1
            # elif h == citations[i]:
            #     return h
            # elif h > citations[i]:
            #     break
            mid = left + (right - left) // 2
            if len(citations) - mid > citations[mid]:
                left = mid + 1
            else:
                h = len(citations) - mid
                right = mid - 1
        return h
    