from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        globalTime = 0
        cooldownHeap = []
        heapq.heapify(cooldownHeap)
        taskProcessorHeap = []
        heapq.heapify(taskProcessorHeap)

        taskCounterMap = defaultdict(int)

        for task in tasks:
            taskCounterMap[task] += 1
        
        for task, freq in taskCounterMap.items():
            heapq.heappush(taskProcessorHeap, (-freq, task))
        
        while cooldownHeap or taskProcessorHeap:
            globalTime += 1
            if len(cooldownHeap) > 0:
                cooldownTime, task, freq = cooldownHeap[0]
                if cooldownTime + n < globalTime:
                    cooldownTime, task, freq = heapq.heappop(cooldownHeap)
                    heapq.heappush(taskProcessorHeap, (freq, task))
            
            if len(taskProcessorHeap) > 0:
                negativeFreq, task = heapq.heappop(taskProcessorHeap)
                freq = -negativeFreq
                if freq - 1 == 0:
                    continue
                
                if n == 0:
                    heapq.heappush(taskProcessorHeap, (-1 * (freq - 1), task))
                else:
                    heapq.heappush(cooldownHeap, (globalTime, task, -1 * (freq - 1)))
        
        return globalTime
