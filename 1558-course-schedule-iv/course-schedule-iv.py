class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachable = [[False] * numCourses for _ in range(numCourses)]
    
    # Step 2: Populate direct prerequisites
        for pre, course in prerequisites:
            reachable[pre][course] = True
        
        # Step 3: Floyd-Warshall Algorithm to find all indirect prerequisites
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True
        
        # Step 4: Answer each query in O(1)
        return [reachable[u][v] for u, v in queries]
    