class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans = []
        distance = {}
        for i in points:
            dis = i[0] ** 2 + i[1] ** 2
            if dis not in distance:
                distance[dis] = [i]
            else:
                distance[dis].append(i)
        
        sorted_ = sorted(distance.keys())
        print(sorted_)
        for i in range(len(sorted_)):
            ans += distance[sorted_[i]]
        
        return ans[:K]