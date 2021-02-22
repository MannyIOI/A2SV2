class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        def pancake_flip(arr, index):
            arr = arr[index - len(arr)::-1] + arr[index + 1:]
            return arr

        for i in range(len(arr), 1, -1):
            idx = arr.index(i)
            # Crazy author, inconsistent indexing
            result.append(idx + 1)
            # Flip to head
            arr = pancake_flip(arr, idx)
            result.append(i)
            # Flip to correct position
            arr = pancake_flip(arr, i - 1)
        return result