from collections import deque, defaultdict

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        
        def bfs_max_groups(start):
            # Try to group nodes starting from each node
            seen = {start: 1}  # node -> group number
            queue = deque([(start, 1)])  # (node, group)
            max_group = 1
            
            while queue:
                node, group = queue.popleft()
                
                for nei in graph[node]:
                    if nei in seen:
                        # Check if neighbor's group differs by exactly 1
                        if abs(seen[nei] - group) != 1:
                            return -1
                    else:
                        # Assign neighbor to next group
                        seen[nei] = group + 1
                        max_group = max(max_group, group + 1)
                        queue.append((nei, group + 1))
            
            return max_group
        
        # Find connected components using DFS
        def find_component(node, component, visited):
            visited[node] = True
            component.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    find_component(nei, component, visited)
        
        # Process each connected component separately
        visited = [False] * n
        total_groups = 0
        
        for node in range(n):
            if not visited[node]:
                # Find all nodes in current component
                component = []
                find_component(node, component, visited)
                
                # Try starting BFS from each node in component
                max_groups = -1
                for start in component:
                    groups = bfs_max_groups(start)
                    if groups != -1:
                        max_groups = max(max_groups, groups)
                
                # If no valid grouping found for component
                if max_groups == -1:
                    return -1
                    
                total_groups += max_groups
        
        return total_groups