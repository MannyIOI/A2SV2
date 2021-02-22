class RecentCounter:

    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        count = 0
        for i in range(len(self.times) - 1, -1, -1):
            if self.times[i] >= t - 3000:
                count += 1
            else:
                break
        
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)