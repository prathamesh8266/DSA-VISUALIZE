import heapq

class Solution:
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        if len(sticks) == 1:
            return sticks[0]
        
        heapq.heapify(sticks)

        count = 0
        while sticks:
            top_sum = 0
            for i in range(2):
                top_sum += heapq.heappop(sticks)

            count += top_sum
            
            if not sticks:
                return count
            
            heapq.heappush(sticks, top_sum)

        return count
        
s = Solution()
print(s.connectSticks([2, 4, 3]))
print(s.connectSticks([1, 8, 3, 5]))