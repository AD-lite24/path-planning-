from inspect import stack
import sys
from turtle import right, up
import random

from MapNode import MapNode

class PlannerNode:
    stack = []
    def __init__(self):
        self.current_obj=MapNode()
        
         # Since we know that the first step the bot will take will be down, we can simply do it here
        self.current_obj.direction_callback("down")  # example 1
        notDir = 'up'
        (self.stack) = []
        self.dead =[]
        self.directions = ['up', 'down', 'left', 'right']
            
        self.found = False
        self.wall_callback(notDir)
        

    def wall_callback(self, notDir):
        # current_obj has all the attributes to help you in in your path planning !
        
        current_coords = self.current_obj.current
        end_coords = self.current_obj.map.end
        tileNum = self.current_obj.array[current_coords[0]][current_coords[1]]


        down_coords = (current_coords[0]+1), (current_coords[1])
        up_coords = (current_coords[0]-1), (current_coords[1])
        left_coords = (current_coords[0]), (current_coords[1] - 1)
        right_coords = (current_coords[0]), (current_coords[1] + 1)

        print(self.current_obj.current)

        (self.stack).append(current_coords)

        def getCost(reqCoords):
            cost = abs(reqCoords[0] - end_coords[0]) + abs(reqCoords[1] - end_coords[1])
            return cost

        if (current_coords == self.current_obj.map.end):
            self.found = True
            return

        # for left-right walls
        if (tileNum == 6):
            #down
            if (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
            #up
            elif (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
            else:
                if (self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])

                elif (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])

        #for left wall
        if (tileNum == 4):
            #down
            if (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
            #right
            elif (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
            #up
            elif (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
            else:
                #down
                if (self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])
                #right
                elif (self.directions[3] != notDir):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                #up
                elif (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])

        #for left-bottom walls
        if (tileNum == 5):
            #right
            if (up_coords in self.dead):
                self.dead.append(current_coords)
                print ('test 2 worked')
            if (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
            #up
            elif (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
            if (up_coords in self.dead):
                self.dead.append(current_coords)
                print ('test 2 worked')
            else:
                #right
                if (self.directions[3] != notDir):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                #up
                elif (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
        
        #for top-bottom walls
        if (tileNum == 9):
            #right
            if (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
            #left
            elif (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
            else:
                if (self.directions[3] != notDir and current_coords not in (self.stack + self.dead)):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
            
                elif (self.directions[2] != notDir and current_coords not in (self.stack + self.dead)):
                    self.current_obj.direction_callback(self.directions[2] )
                    self.wall_callback(self.directions[3])
                else:
                    if (self.directions[3] != notDir):
                        self.current_obj.direction_callback(self.directions[3])
                        self.wall_callback(self.directions[2])
            
                    elif (self.directions[2] != notDir):
                        self.current_obj.direction_callback(self.directions[2] )
                        self.wall_callback(self.directions[3])

        #for bottom wall
        if (tileNum == 1):
            #right
            if (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
            #up
            elif (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
            #left
            elif (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
            else:
                if (self.directions[3] != notDir):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                elif (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                elif (self.directions[2] != notDir):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])

        #for right-bottom wall
        if (tileNum == 3):
            #up
            if (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
            #left
            elif (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
            else:
                if (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                elif (self.directions[2]!= notDir):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
        
        #for right wall
        if (tileNum == 2):
            #up
            if (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
            #left
            elif (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
            #down
            elif (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
            else:
                #up
                if (self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                #left
                elif (self.directions[2] != notDir):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
                #down
                elif (self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])

        #for left wall
        if (tileNum == 4):
            
            #up
            if  (self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords) and up_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
                
            #right 
            elif (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                
            #down
            elif (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])

        #for top-right wall
        if (tileNum == 10):
            #left
            if (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
            #down 
            elif (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
            else:
                if (self.directions[2] != notDir):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
             
                elif (self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])

        #for top wall
        if (tileNum == 8):
            #right
            if (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
            #left
            elif (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
            #down
            elif (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                    
            else:
                #right
                if (self.directions[3] != notDir):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                #left
                elif (self.directions[2] != notDir):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
                #down
                elif (self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])

        #for top-left wall
        if (tileNum == 12):
            #right 
            if (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
            #down
            elif(self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in (self.stack + self.dead)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
            else:
                if (self.directions[3] != notDir):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
            
                elif(self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])
            
        #for left deadend
        if (tileNum == 11):
            self.dead.append(current_coords)
            print ('test worked')
            self.current_obj.direction_callback(self.directions[2])
            self.wall_callback(self.directions[3])

        #for no-wall 
        if (tileNum == 0):
            index = random.randint(0, 3)
            #left
            if (self.directions[2] != notDir and getCost(current_coords) > getCost(left_coords) and left_coords not in (self.dead + self.stack)):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
            #up
            elif(self.directions[0] != notDir and getCost(current_coords) > getCost(up_coords)and up_coords not in ( self.dead+ self.stack)):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
            #down
            elif (self.directions[1] != notDir and getCost(current_coords) > getCost(down_coords) and down_coords not in  ( self.dead + self.stack)):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
            #right
            elif (self.directions[3] != notDir and getCost(current_coords) > getCost(right_coords) and right_coords not in  ( self.dead + self.stack)):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
            else:
                if (index == 0 and self.directions[0] != notDir):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                if (index == 1 and self.directions[1] != notDir):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])
                if (index == 2 and self.directions[2] != notDir):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
                if (index == 3 and self.directions[3] != notDir):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
        #for top deadend
        if (tileNum == 14):
            self.dead.append(current_coords)
            print ('test worked')
            self.current_obj.direction_callback(self.directions[1])
            self.wall_callback(self.directions[0])
        
        #for bottom deadend
        if (tileNum == 7):
            self.dead.append(current_coords)
            print ('test worked')
            self.current_obj.direction_callback(self.directions[0])
            self.wall_callback(self.directions[1])
        
            

if __name__ == '__main__':
    start_obj=PlannerNode()
    start_obj.current_obj.print_root.mainloop()
 