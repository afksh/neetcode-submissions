from heapq import *
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return [i[0] for i in heapq.nlargest(k, counts.items(), key=lambda x:x[1])]