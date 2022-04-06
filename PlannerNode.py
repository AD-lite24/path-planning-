#Sorry for the bad code. I can see the redundacy and bad practices used, but this setup was actually meant to be experimental. 
#I was basically testing out behaviours for every tile type and i got pretty far, so i just decided to continue with this. 

#I also understand that this is not the one that was meant to be implemented, but the one i could do using my current programming skills.
#I fully understand the cost mapping algorithm and all its demonstrations of effectiveness though

#Also small bug sometimes it doesnt stop at end point, I will figure it out soon :(


from inspect import stack
import sys
from turtle import right, up
import random
import numpy as np
from MapNode import MapNode

class PlannerNode:
    stack = []
    def __init__(self):
        self.current_obj=MapNode()
        self.visit_num=np.zeros((10,10))
         # Since we know that the first step the bot will take will be down, we can simply do it here
        self.current_obj.direction_callback("down")  # example 1
        notDir = 'up'
        (self.stack) = []
        self.dead =[]
        self.directions = ['up', 'down', 'left', 'right']            
        (self.found) = False
        self.wall_callback(notDir)
        

    def wall_callback(self, notDir):
        # current_obj has all the attributes to help you in in your path planning !
        self.visit_num[self.current_obj.current[0]][self.current_obj.current[1]] +=1
        current_coords = self.current_obj.current
        end_coords = self.current_obj.map.end
        tileNum = self.current_obj.array[current_coords[0]][current_coords[1]]
        costs = {} 
        visited = set()


        down_coords = (current_coords[0]+1), (current_coords[1])
        up_coords = (current_coords[0]-1), (current_coords[1])
        left_coords = (current_coords[0]), (current_coords[1] - 1)
        right_coords = (current_coords[0]), (current_coords[1] + 1)

        print(self.current_obj.current)

        (self.stack).append(current_coords)

        def getCost(reqCoords):
            cost = abs(reqCoords[0] - end_coords[0]) + abs(reqCoords[1] - end_coords[1])
            return cost

        #bad attempt at making the proper cost function below



        # def getCost(self, reqCoords) :
        #     c = [] 

        #     visited.add((reqCoords))

        #     if (reqCoords) == self.current_obj.walls.end:
        #         return 0
        
        #     if (reqCoords) in costs:
        #         return getCost[(reqCoords)]
        #     else:
        #         if available(x, y, "right"):
        #             c.append(getCost(x+1, y))
        #         if available(x, y, "left"):
        #             c.append(getCost(x-1, y))
        #         if available(x, y, "up"):
        #             c.append(getCost(x, y-1))
        #         if available(x, y, "down"):
        #             c.append(getCost(x, y+1))
        #         costs[(x, y)] = min(c)+1
        #     return costs[(x, y)]


        # def available(reqCoords, x, y):      #a and b are the points from which u want to check availability and x, y is the point u r checking availability at
        #     n = 14          #actually the tile number

        #     if (x, y) in visited:
        #         return False

        #     s = bin(14)[2:]
        #     s = "0"*(4-len(s)) + s

        #     if x == reqCoords[0] and y == reqCoords[1]+1:
        #         dir = "down"
        #     elif x == reqCoords[0] and y == reqCoords[1]-1:
        #         dir = "up"
        #     elif x == reqCoords[0]+1:
        #         dir = "right"
        #     else:
        #         dir = "left"


        #     if dir == "up":
        #         if s[0] == "1":
        #             return True
        #     if dir == "left":
        #         if s[1] == "1":
        #             return True
        #     if dir == "right":
        #         if s[2] == "1":
        #             return True
        #     if dir == "down":
        #         if s[3] == "1":
        #             return True
            

        if (current_coords == self.current_obj.map.end):
            self.found = True
            print ('reached')
            return
        
        def take_random_step(index):
            print("taking random step")
            if (index == 0 ):
                print("a")
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
                if (self.found):
                    return
            if (index == 1 ):
                print("b")
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if (self.found):
                    return
            if (index == 2 ):
                print("c")
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
                if (self.found):
                    return
            if (index == 3 ):
                print("d")
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if (self.found):
                    return
        
        
        # for left-right walls
        if (tileNum == 6):
            
            #down
            if (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if (self.found):
                    return
            #up
            elif (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
                if (self.found):
                    return
            else:
                if (self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])
                    if (self.found):
                        return

                elif (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                    if (self.found):
                        return

        #for left wall
        if (tileNum == 4):
            if self.visit_num[current_coords[0]][current_coords[1]]>=4:
                take_random_step(np.random.randint(0,3))
            #down
            if (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if (self.found):
                    return
            #right
            elif (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if (self.found):
                    return
            #up
            elif (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
                if (self.found):
                    return
            else:
                #down
                if (self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])
                    if (self.found):
                        return
                #right
                elif (self.directions[3] != notDir):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                    if (self.found):
                        return
                #up
                elif (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                    if (self.found):
                        return

        #for left-bottom walls
        if (tileNum == 5):
            #right
            if (up_coords in self.dead):
                self.dead.append(current_coords)
                print ('test 2 worked')
            if (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if (self.found):
                    return
            #up
            elif (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
                if (self.found):
                    return
            
            else:
                #right
                if (self.directions[3] != notDir):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                    if (self.found):
                        return
                #up
                elif (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                    if (self.found):
                        return
        
        #for top-bottom walls
        if (tileNum == 9):
            #right
            if (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if (self.found):
                    return
            #left
            elif (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
                if (self.found):
                    return
            else:
                if (self.directions[3] != notDir and current_coords not in (self.stack + self.dead)):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                    if (self.found):
                        return
            
                elif (self.directions[2] != notDir and current_coords not in (self.stack + self.dead)):
                    self.current_obj.direction_callback(self.directions[2] )
                    self.wall_callback(self.directions[3])
                    if (self.found):
                        return
                else:
                    if (self.directions[3] != notDir):
                        self.current_obj.direction_callback(self.directions[3])
                        self.wall_callback(self.directions[2])
                        if (self.found):
                            return
            
                    elif (self.directions[2] != notDir):
                        self.current_obj.direction_callback(self.directions[2] )
                        self.wall_callback(self.directions[3])
                        if (self.found):
                            return

        #for bottom wall
        if (tileNum == 1):
            if self.visit_num[current_coords[0]][current_coords[1]]>=4:
                take_random_step(np.random.randint(0,3))
            #right
            if (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if (self.found):
                    return
            #up
            elif (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
                if (self.found):
                    return
            #left
            elif (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
                if (self.found):
                    return
            else:
                if (self.directions[3] != notDir):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                    if (self.found):
                        return
                elif (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                    if (self.found):
                        return
                elif (self.directions[2] != notDir):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
                    if (self.found):
                        return

        #for right-bottom wall
        if (tileNum == 3):
            
            #up
            if (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
                if (self.found):
                    return
            #left
            elif (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
                if (self.found):
                    return
            else:
                if (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                    if (self.found):
                        return
                elif (self.directions[2]!= notDir):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
                    if (self.found):
                        return
        
        #for right wall
        if (tileNum == 2):
            if self.visit_num[current_coords[0]][current_coords[1]]>=4:
                take_random_step(np.random.randint(0,3))
            #up
            if (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
                if (self.found):
                    return
            #left
            elif (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
                if (self.found):
                    return
            #down
            elif (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if (self.found):
                    return
            else:
                #up
                if (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                    if (self.found):
                        return
                #left
                elif (self.directions[2] != notDir):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
                    if (self.found):
                        return
                #down
                elif (self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])
                    if (self.found):
                        return

        #for left wall
        if (tileNum == 4):
            if self.visit_num[current_coords[0]][current_coords[1]]>=4:
                take_random_step(np.random.randint(0,3))
            #up
            if  (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
                if (self.found):
                    return
                
            #right 
            elif (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if (self.found):
                    return
                
            #down
            elif (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if (self.found):
                    return

        #for top-right wall
        if (tileNum == 10):
            #left
            if (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
                if (self.found):
                    return
            #down 
            elif (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if (self.found):
                    return
            else:
                if (self.directions[2] != notDir):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
                    if (self.found):
                        return
             
                elif (self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])
                    if (self.found):
                        return

        #for top wall
        if (tileNum == 8):
            if self.visit_num[current_coords[0]][current_coords[1]]>=2:
                take_random_step(np.random.randint(0,3))
            #down
            if (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if (self.found):
                    return
            #right
            elif (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if (self.found):
                    return
            #left
            elif (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
                if (self.found):
                    return
                    
            else:
                #right
                if (self.directions[3] != notDir):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                    if (self.found):
                        return
                #down
                elif (self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                    if (self.found):
                        return
                #left
                elif (self.directions[2] != notDir):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
                    if (self.found):
                        return
                

        #for top-left wall
        if (tileNum == 12):
            #right 
            if (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if (self.found):
                    return
            #down
            elif(self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if (self.found):
                    return
            else:
                if (self.directions[3] != notDir):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                    if (self.found):
                        return
            
                elif(self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])
                    if (self.found):
                        return
            
        #for left deadend
        if (tileNum == 11):
            self.dead.append(current_coords)
            print ('test worked')
            self.current_obj.direction_callback(self.directions[2])
            self.wall_callback(self.directions[3])
            if (self.found):
                return

        #for no-wall 
        if (tileNum == 0):
            index = random.randint(0, 3)
            #left
            if (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.dead + self.stack)):
                    print("1")
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
                    if (self.found):
                        return
            #up
            elif(self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords)and up_coords not in ( self.dead+ self.stack)):
                print("2")
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
                if (self.found):
                    return
            #down
            elif (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in  ( self.dead + self.stack)):
                print("3")
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if (self.found):
                    return
            #right
            elif (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in  ( self.dead + self.stack)):
                print("4")
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if (self.found):
                    return
            else:
            #left
                if (self.directions[2] != notDir and left_coords not in (self.dead + self.stack)):
                    print("1")
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
                    if (self.found):
                        return
            #up
                elif(self.directions[0] != notDir and up_coords not in ( self.dead+ self.stack)):
                    print("2")
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                    if (self.found):
                        return
            #down
                elif (self.directions[1] != notDir and down_coords not in  ( self.dead + self.stack)):
                    print("3")
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])
                    if (self.found):
                        return
            #right
                elif (self.directions[3] != notDir and right_coords not in  ( self.dead + self.stack)):
                    print("4")
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                    if (self.found):
                        return
                else:
                    #left
                    if (self.directions[2] != notDir and left_coords not in (self.dead)):
                        print("1")
                        self.current_obj.direction_callback(self.directions[2])
                        self.wall_callback(self.directions[3])
                        if (self.found):
                            return
                    #up
                    elif(self.directions[0] != notDir and up_coords not in ( self.dead)):
                        print("2")
                        self.current_obj.direction_callback(self.directions[0])
                        self.wall_callback(self.directions[1])
                        if (self.found):
                            return
            #down
                    elif (self.directions[1] != notDir and down_coords not in  ( self.dead)):
                        print("3")
                        self.current_obj.direction_callback(self.directions[1])
                        self.wall_callback(self.directions[0])
                        if (self.found):
                            return
            #right
                    elif (self.directions[3] != notDir and right_coords not in  ( self.dead)):
                        print("4")
                        self.current_obj.direction_callback(self.directions[3])
                        self.wall_callback(self.directions[2])
                        if (self.found):
                            return

        #for right deadend
        if (tileNum == 13):
            self.dead.append(current_coords)
            print ('test worked')
            self.current_obj.direction_callback(self.directions[3])
            self.wall_callback(self.directions[2])
            if (self.found):
                return
                
        #for top deadend
        if (tileNum == 14):
            self.dead.append(current_coords)
            print ('test worked')
            self.current_obj.direction_callback(self.directions[1])
            self.wall_callback(self.directions[0])
            if (self.found):
                return
        
        #for bottom deadend
        if (tileNum == 7):
            self.dead.append(current_coords)
            print ('test worked')
            self.current_obj.direction_callback(self.directions[0])
            self.wall_callback(self.directions[1])
            if (self.found):
                return
        
            

if __name__ == '__main__':
    start_obj=PlannerNode()
    start_obj.current_obj.print_root.mainloop()
 