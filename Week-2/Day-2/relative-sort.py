class Solution:
    def relativeSortArray(self, arr1, arr2):
        sorted_ = []
        for i in arr2:
            for j in range(len(arr1)):
                if i == arr1[j]:
                    sorted_.append(arr1[j])
        rem = []
        for i in arr1:
            if i not in sorted_:
                rem.append(i)
        
        sorted_ += sorted(rem)
        return sorted_