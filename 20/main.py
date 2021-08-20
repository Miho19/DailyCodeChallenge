
count = 0

def mapCreate(x: int, y: int):
    l = []
    for i in range(x):
        l.append([0] * y)
    return l

def mapPrint(map: list):
    for row in map:
        print(row)

def pathSearch(map: list, x: int, y: int):
    global count
    
    if x == len(map) -1 and y == len(map[0]) - 1:
        count += 1
        return
    
    if x + 1 < len(map):
        pathSearch(map, x + 1, y)
    
    if y + 1 < len(map[0]):
        pathSearch(map, x, y + 1)

 
new_map = mapCreate(5, 5)

pathSearch(new_map, 0, 0)
print("count: " + str(count))

    