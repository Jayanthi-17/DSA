from copy import deepcopy
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        visited=deepcopy(image)
        r=len(visited)
        c=len(visited[0])
        initial_color=visited[sr][sc]
        if initial_color==color:
            return image
        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>= c:
                return
            if initial_color!=visited[i][j]:
                return
            visited[i][j]=color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        dfs(sr,sc)
        return visited


# BFS:
from copy import deepcopy
from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        visited=deepcopy(image)
        r=len(visited)
        c=len(visited[0])
        initial_color=visited[sr][sc]
        queue=deque()
        queue.append((sr,sc))
        if initial_color==color:
            return image
        while len(queue)!=0:
            i,j=queue.popleft()
            visited[i][j]=color
            for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                new_i=dx+i
                new_j=dy+j
                if i<0 or j<0 or i>=r or j>= c:
                    continue
                if visited[i][j]!=initial_color:
                    continue
                queue.append((sr,sc))
                return visited
                
