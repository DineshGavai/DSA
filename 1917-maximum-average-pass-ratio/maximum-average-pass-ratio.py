class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def benefit(passi, totali):
            return (passi + 1) / (totali + 1) - passi / totali
    
        # Max-Heap with benefit as the key (negated for max behavior)
        heap = [(-benefit(passi, totali), passi, totali) for passi, totali in classes]
        heapq.heapify(heap)
        
        # Assign extra students
        for _ in range(extraStudents):
            max_benefit, passi, totali = heapq.heappop(heap)
            passi += 1
            totali += 1
            heapq.heappush(heap, (-benefit(passi, totali), passi, totali))
        
        # Compute the average pass ratio
        total_ratio = sum(passi / totali for _, passi, totali in heap)
        return total_ratio / len(classes)