from collections import deque

#example map 2D list (could be customized) (0 means empty and 1 means wall)
map = [[0, 0, 0, 1],
       [1, 1, 0, 1],
       [0, 0, 0, 0],
       [0, 1, 1, 0]]

moves = [[-1, 0], [1, 0], [0, -1], [0,1]] 
directions = {(-1, 0): "N", (1,0): "S", (0, -1): "W", (0, 1): "E"} #uses dictonary to store the direction in letter according to the moves

def bfs(grid):
    R = len(grid) #gets the number of rows (how many list)
    C = len(grid[0]) #gets the number of column (how many values in each list)
    vis = [[False] * R for i in range(C)] #sets visted as all false in the begaining 
    parent = [[None] * C for i in range(C)]
    q = deque()

    #starting the queue 
    q.append((0,0))
    vis[0][0] = True

    while len(q):
        x, y = q.popleft() #gets the first values of the q, current pos
        for dx, dy in moves: #gets each of the move (direction x and direction y)
            #new pos
            new_x = x + dx 
            new_y = y + dy
            #checks if the new pos is in bound, has not been visited, and its a 0 there
            if new_x >= 0 and new_x < R and new_y >=0 and new_y < C and not vis[new_x][new_y] and grid[new_x][new_y] == 0:
                q.append((new_x, new_y)) 
                vis[new_x][new_y] = True
                parent[new_x][new_y] = (x, y, directions[(dx, dy)]) #stores the old pos and the direction it took to get to new

    #exit never reached, not possible 
    if not vis[R-1][C-1]:
        return(-1)
    

    #reconstructs the path starting from the end to start
    path = []
    x, y = R-1, C-1
    while (x, y) != (0, 0):
        px, py, dir = parent[x][y]
        path.append(dir)
        x, y = px, py
    return (path[::-1]) #reverse it because backtracking

print(bfs(map))
