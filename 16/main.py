
from typing import Deque

rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

class Node:
    def __init__(self, coord: list, distance: int):
        self.coord = coord
        self.distance = distance


f = False
t = True

map = [
[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]
]

def check(map: list, row: int, col: int):
    return ((row >= 0) and (row < len(map)) and (col >= 0) and (col < len(map[row])))

def BFS(map, start: list, end: list):

    if(start[0] > len(map) or len(map[start[0]]) < start[1]):
        print("Invalid starting position: out of range")
        return None
    
    if(end[0] > len(map) or len(map[end[0]]) < end[1]):
        print("Invalid ending position: out of range")
        return None
    
    if(map[start[0]][start[1]] == t):
        print("Invalid starting position")
        return None
    
    if(map[end[0]][end[1]] == t):
        return None


    s = Node(start, 0)
    
    visited = []
    visited.append(start)

    queue = Deque()

    queue.append(s)
    
    while(queue):
        curr = queue.popleft()
        pos = curr.coord
        
        if(pos[0] == end[0] and pos[1] == end[1]):
            print(curr.distance)
            return curr.distance
        
        for i in range(4):
            
            row = pos[0] + rowNum[i]
            col = pos[1] + colNum[i]
            
            if(check(map, row, col) and map[row][col] == f and [row, col] not in visited):  
                visited.append([row, col])
                new_node = Node([row, col], curr.distance + 1)
                queue.append(new_node)
    return -1


                


        

        

BFS(map, [3, 0], [0, 0])
