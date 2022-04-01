costs = {} 
visited = set()

def cost(self, x, y) :
    c = [] 

    visited.add((x, y))

    if (x, y) == self.current_obj.walls.end:
        return 0
        
    if (x, y) in costs:
        return cost[(x, y)]
    else:
        if available(x, y, "right"):
            c.append(cost(x+1, y))
        if available(x, y, "left"):
            c.append(cost(x-1, y))
        if available(x, y, "up"):
            c.append(cost(x, y-1))
        if available(x, y, "down"):
            c.append(cost(x, y+1))
        costs[(x, y)] = min(c)+1
    return costs[(x, y)]


def available(a, b, x, y):      #a and b are the points from which u want to check availability and x, y is the point u r checking availability at
    n = 14          #actually the tile number

    if (x, y) in visited:
        return False

    s = bin(14)[2:]
    s = "0"*(4-len(s)) + s

    if x == a and y == b+1:
        dir = "down"
    elif x == a and y == b-1:
        dir = "up"
    elif x == a+1:
        dir = "right"
    else:
        dir = "left"


    if dir == "up":
        if s[0] == "1":
            return True
    if dir == "left":
        if s[1] == "1":
            return True
    if dir == "right":
        if s[2] == "1":
            return True
    if dir == "down":
        if s[3] == "1":
            return True

    

    

        