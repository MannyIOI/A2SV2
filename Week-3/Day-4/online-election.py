class TopVotedCandidate:
    def __init__(self, persons: [int], times: [int]):
        self.A = []
        count = collections.Counter()
        leader, m = None, 0
        
        for i in range(len(persons)):
            person = persons[i]
            time = times[i]
            count[person] += 1
            c = count[person]
            if c >= m:
                leader = person
                self.A.append((time, leader))
                m = c

    def q(self, t: int) -> int:
        lo = 0
        hi = len(self.A) - 1
        while lo <= hi:
            md = (lo + hi) // 2
            if self.A[md][0] == t:
                return self.A[md][1]

            if self.A[md][0] > t:
                hi = md - 1
            else:
                lo = md + 1
        return self.A[hi][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)