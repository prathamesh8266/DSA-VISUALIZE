import heapq
from collections import deque, Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        
        n = len(hand)
        if n % groupSize != 0:
            return False

        heap = [] # O(n) space

        counter = Counter(hand) # O(n) space and time

        for k in counter.keys(): # O(n) time
            heap.append((k,counter[k]))

        heapq.heapify(heap) # O(n) time

        cards = 0
        prev = -1

        queue = deque([])  # O(n) space
        
        while heap or queue:  # O(n) space
            cards %= groupSize
            top = -1
            if cards == 0:
                while queue:
                    heapq.heappush(heap,queue.popleft()) # O(logn) time
                top = heapq.heappop(heap)
                prev = top[0]
            else:
                if not heap:
                    return False
                top = heapq.heappop(heap) # O(logn) time
                if top[0] != prev + 1:
                    return False
                prev = top[0]
            
            if top[1] > 1:
                queue.append((top[0], top[1]-1))

            cards += 1

        return True


s = Solution()
print(s.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3)) # TRUE
print(s.isNStraightHand(hand = [1,2,3,4,5], groupSize = 4)) # FALSE