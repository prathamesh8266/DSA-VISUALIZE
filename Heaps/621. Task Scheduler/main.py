from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)

        waiting_queue = deque([])

        time = 0

        while heap or waiting_queue:
            time += 1

            if not heap and waiting_queue:
               time = waiting_queue[0][1]

            while waiting_queue and waiting_queue[0][1] <= time:
                heapq.heappush(heap,waiting_queue.popleft()[0])

            if heap:
                top = heapq.heappop(heap)
                if top < -1:
                    waiting_queue.append((top+1,time + n + 1))
            
        return time
        
        
s = Solution()
print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)) # 8
print(s.leastInterval(tasks = ["A","C","A","B","D","B"], n = 1)) # 6
print(s.leastInterval(tasks = ["A","A","A", "B","B","B"], n = 3)) # 10
