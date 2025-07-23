from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])
        to_change=image[sr][sc]
        image_copy=deepcopy(image)
        if to_change==color:
            return image
        q=deque()
        q.append([sr,sc])
        image_copy[sr][sc]=color
        while q:
            i,j=q.popleft()
            for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_i,new_j=i+dx,j+dy
                if new_i < 0 or new_i==rows or new_j < 0 or new_j==cols:
                    continue
                if image_copy[new_i][new_j]==to_change:
                    image_copy[new_i][new_j]=color
                    q.append([new_i,new_j])
        return image_copy