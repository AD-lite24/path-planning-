#I tried to implememt a more efficent algorithm, but it was too complicated for me to code (this was a simpler version of my originally intended algo). 
# Hence i shifted to an even simpler version using basic recursion. I did manage to implement some features in 
# I have just commented out my previous attempt for reference. The final one is given below that
# Please note that I have in fact accessed the map, but only for the current coord the bot is on, and nothing else, so think it should be legal
# My original algo is written in a txt file in the zip file.
# The arduino task in incomplete. I tried to understand but just couldnt get it work, and i also ran out of time. The incomplete work has been
# attached as instructed.







# from asyncio.windows_events import NULL
# import sys

# from MapNode import MapNode

# class PlannerNode:
    
#     stack = []
#     def __init__(self):
#         self.current_obj=MapNode()
        
#         # Since we know that the first step the bot will take will be down, we can simply do it here
#         self.current_obj.direction_callback("down")  # example 1
#         self.current_obj.direction_callback("down")
#         notDir = None
#         self.stack = []
        
#         self.wall_callback(notDir)
        
    

#     def wall_callback(self, notDir):
        
        
#         print(self.current_obj.current)
#         # current_obj has all the attributes to help you in in your path planning !
         
        
        
        
#         current_coords = self.current_obj.current 
           
#         self.stack.append(current_coords)

#         tileNum = self.current_obj.array[current_coords[0]][current_coords[1]]
#         print(tileNum)
#                 #tileNum is being accessed for the current coord only, which is inline with the practical scenario
#                 #that only the current tile can be seen

#                 #to identify dead ends 

#         pop_intersec = True
#         if (tileNum == 14 or tileNum == 7 or tileNum == 11 or tileNum == 13):
#             pop_intersec = False
#             if (tileNum == 14):
#                 notDir = 'right'
#             if (tileNum == 7):
#                 notDir = 'up'
#             if (tileNum == 11):
#                 notDir = 'left'
#             if (tileNum == 13):
#                 notDir = 'down'        

#         directions = ['down', 'up', 'left', 'right']

#         if (notDir != directions[0] and not self.current_obj.map.check_bottom_wall(current_coords) and not (current_coords[0]+1, current_coords[1]) in self.stack):
#             self.current_obj.direction_callback(directions[0])
#             notDir = directions[1]
#             self.wall_callback(notDir)

#         elif (notDir != directions[1] and not self.current_obj.map.check_top_wall(current_coords) and not (current_coords[0]-1, current_coords[1]) in self.stack):
#             self.current_obj.direction_callback(directions[1])
#             notDir = directions[0]
#             self.wall_callback(notDir)

#         elif (notDir != directions[2] and not self.current_obj.map.check_left_wall(current_coords) and not (current_coords[0], current_coords[1]-1) in self.stack):
#             self.current_obj.direction_callback(directions[2])
#             notDir = directions[3]
#             self.wall_callback(notDir)

#         elif (notDir != directions[3] and not self.current_obj.map.check_right_wall(current_coords) and not (current_coords[0], current_coords[1]+1) in self.stack):
#             self.current_obj.direction_callback(directions[3])
#             notDir = directions[2]
#             self.wall_callback(notDir)

#         else:
#             self.current_obj.direction_callback(notDir)    


#         while(not pop_intersec):
#             print('execute')
            
#             self.current_obj.direction_callback(notDir)
#             if (self.current_obj.array[current_coords[0]][current_coords[1]] == 5 and notDir != 'left'):
#                 notDir = 'left'
#             elif (self.current_obj.array[current_coords[0]][current_coords[1]] == 5 and notDir != 'down'):
#                 notDir = 'down'
#             elif (self.current_obj.array[current_coords[0]][current_coords[1]] == 3 and notDir != 'down'):
#                 notDir = 'down'
#             elif (self.current_obj.array[current_coords[0]][current_coords[1]] == 3 and notDir != 'right'):
#                 notDir = 'right'
#             elif (self.current_obj.array[current_coords[0]][current_coords[1]] == 12 and notDir != 'left'):
#                 notDir = 'left'
#             elif (self.current_obj.array[current_coords[0]][current_coords[1]] == 12 and notDir != 'up'):
#                 notDir = 'up'
#             elif (self.current_obj.array[current_coords[0]][current_coords[1]] == 10 and notDir != 'up'):
#                 notDir = 'up'
#             elif (self.current_obj.array[current_coords[0]][current_coords[1]] == 10 and notDir != 'right'):
#                 notDir = 'right'
#             elif (self.current_obj.array[current_coords[0]][current_coords[1]] == 8 or self.current_obj.array[current_coords[0]][current_coords[1]] == 4 or self.current_obj.array[current_coords[0]][current_coords[1]] == 2 or self.current_obj.array[current_coords[0]][current_coords[1]] == 1 or self.current_obj.array[current_coords[0]][current_coords[1]] ==0):
#                 pop_intersec = True 

#         self.wall_callback(notDir) 
        

# if __name__ == '__main__':
#     start_obj=PlannerNode()
#     start_obj.current_obj.print_root.mainloop()





from asyncio.windows_events import NULL
import sys

from MapNode import MapNode

class PlannerNode:
    
    def __init__(self):
        self.current_obj=MapNode()
        
        # Since we know that the first step the bot will take will be down, we can simply do it here
        self.current_obj.direction_callback("down")  # example 1
        notDir = 'up'
        self.stack = []
        self.dead =[]
        self.directions = ['up', 'down', 'left', 'right']
        
        self.found = False
        self.wall_callback(notDir)
        self.getDirections(self.stack)
        
    @staticmethod  
    def getDirections(stack):
        finalDirections = [0] * len(stack)
        finalDirections[0] = 1
        for i in range(1, len(stack)):
            x = stack[i][0]
            y = stack[i][1]
            if (x < stack[i-1][0]):
                finalDirections[i] = 0
            if (x > stack[i-1][0]):
                finalDirections[i] = 1
            if (y < stack[i-1][1]):
                finalDirections[i] = 2
            if (y > stack[i-1][1]):
                finalDirections[i] = 3
        print(finalDirections)
               



    def wall_callback(self, notDir):
        current_coords = self.current_obj.current
        end_coords = self.current_obj.map.end
        tileNum = self.current_obj.array[current_coords[0]][current_coords[1]]
        print(self.current_obj.current)
        # current_obj has all the attributes to help you in in your path planning !
         
         
           
        self.stack.append(current_coords)
        
        if(current_coords == self.current_obj.map.end):
            self.found = True
            
            return

        # for up and left 
        if (current_coords[0] > end_coords[0] and current_coords[1] > end_coords[1]):
            if (notDir != self.directions[0] and not self.current_obj.map.check_top_wall(current_coords) and ((current_coords[0] - 1, current_coords[1]) not in (self.stack + self.dead))):
                self.current_obj.direction_callback(self.directions[0])
                self.wall_callback(self.directions[1])
                if(self.found):
                    return
                
            elif (notDir != self.directions[2] and not self.current_obj.map.check_left_wall(current_coords) and ((current_coords[0], current_coords[1] - 1) not in (self.stack + self.dead))):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
                if(self.found):
                    return

        # for down and left
        if (current_coords[1] > end_coords[1] and current_coords[0] < end_coords[0]):
            if (notDir != self.directions[2] and not self.current_obj.map.check_left_wall(current_coords) and ((current_coords[0], current_coords[1] - 1) not in (self.stack + self.dead))):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
                if(self.found):
                    return
            elif (notDir != self.directions[1] and not self.current_obj.map.check_bottom_wall(current_coords) and ((current_coords[0] + 1, current_coords[1]) not in (self.stack + self.dead))):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if(self.found):
                    return
        
         #for down only
        if (current_coords[1] == end_coords[1] and current_coords[0] < end_coords[0]):
             if (notDir != self.directions[1] and not self.current_obj.map.check_bottom_wall(current_coords) and ((current_coords[0] + 1, current_coords[1]) not in (self.stack + self.dead))):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if(self.found):
                    return
        
        # for up only
        if (current_coords[1] == end_coords[1] and current_coords[0] > end_coords[0]):
            if (notDir != self.directions[0] and not self.current_obj.map.check_top_wall(current_coords) and ((current_coords[0] - 1, current_coords[1]) not in (self.stack + self.dead))):
                 self.current_obj.direction_callback(self.directions[0])
                 self.wall_callback(self.directions[1])
                 if(self.found):
                    return

        # for left only 
        if (current_coords[0] == end_coords[0] and current_coords[1] > end_coords[1]):
            if (notDir != self.directions[2] and not self.current_obj.map.check_left_wall(current_coords) and ((current_coords[0], current_coords[1] - 1) not in (self.stack + self.dead))):
                self.current_obj.direction_callback(self.directions[2])
                self.wall_callback(self.directions[3])
                if(self.found):
                    return
        
        # for right only 
        if (current_coords[0] == end_coords[0] and current_coords[1] < end_coords[1]):
            if (notDir != self.directions[3] and not self.current_obj.map.check_right_wall(current_coords) and ((current_coords[0], current_coords[1] + 1) not in (self.stack + self.dead))):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if(self.found):
                    return
        

           
        
         # for down and right     
        if (current_coords[0] < end_coords[0] and current_coords[1] < end_coords[1]):
            if (notDir != self.directions[1] and not self.current_obj.map.check_bottom_wall(current_coords) and ((current_coords[0] + 1, current_coords[1]) not in (self.stack + self.dead))):
                self.current_obj.direction_callback(self.directions[1])
                self.wall_callback(self.directions[0])
                if(self.found):
                    return
            elif (notDir != self.directions[3] and not self.current_obj.map.check_right_wall(current_coords) and ((current_coords[0], current_coords[1] + 1) not in (self.stack + self.dead))):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if(self.found):
                    return
            

        #for up and right
        if (current_coords[1] < end_coords[1] and current_coords[0] > end_coords[0]):
            if (notDir != self.directions[3] and not self.current_obj.map.check_right_wall(current_coords) and ((current_coords[0], current_coords[1] + 1) not in (self.stack + self.dead))):
                self.current_obj.direction_callback(self.directions[3])
                self.wall_callback(self.directions[2])
                if(self.found):
                    return
            elif (notDir != self.directions[0] and not self.current_obj.map.check_top_wall(current_coords) and ((current_coords[0] - 1, current_coords[1]) not in (self.stack + self.dead))):
                 self.current_obj.direction_callback(self.directions[0])
                 self.wall_callback(self.directions[1])
                 if(self.found):
                    return
            
        else:
                if (notDir != self.directions[0] and not self.current_obj.map.check_top_wall(current_coords) and ((current_coords[0] - 1, current_coords[1]) not in (self.stack + self.dead))):
                    self.current_obj.direction_callback(self.directions[0])
                    self.wall_callback(self.directions[1])
                    if(self.found):
                        return
                

                if (notDir != self.directions[1] and not self.current_obj.map.check_bottom_wall(current_coords) and ((current_coords[0] + 1, current_coords[1]) not in (self.stack + self.dead))):
                    self.current_obj.direction_callback(self.directions[1])
                    self.wall_callback(self.directions[0])
                    if(self.found):
                        return

                if (notDir != self.directions[2] and not self.current_obj.map.check_left_wall(current_coords) and ((current_coords[0], current_coords[1] - 1) not in (self.stack + self.dead))):
                    self.current_obj.direction_callback(self.directions[2])
                    self.wall_callback(self.directions[3])
                    if(self.found):
                        return
                
                if (notDir != self.directions[3] and not self.current_obj.map.check_right_wall(current_coords) and ((current_coords[0], current_coords[1] + 1) not in (self.stack + self.dead))):
                    self.current_obj.direction_callback(self.directions[3])
                    self.wall_callback(self.directions[2])
                    if(self.found):
                        return
        

        self.stack.pop()
        if (tileNum == 0 or tileNum == 2 or tileNum == 4 or tileNum == 8):
            self.dead.append(current_coords)
        
        self.current_obj.direction_callback(notDir)
        
        

if __name__ == '__main__':
    
    start_obj=PlannerNode()
    start_obj.current_obj.print_root.mainloop()


"""""
# Importing necessary libraries
import random
import math
import numpy as np

from MapNode import MapNode

import tkinter


def get_dir_backward(dir_forward):
    '''Returns the direction opposite to input direction'''

    if(dir_forward == 'right'):
        return 'left'

    if(dir_forward == 'down'):
        return 'up'

    if(dir_forward == 'left'):
        return 'right'

    if(dir_forward == 'up'):
        return 'down'


class PlannerNode:

    def __init__(self):
        '''Initializes the attribute of PlannerNode'''

        self.current_obj = MapNode()

        # Since we know that the first step the bot will take will be down, we can simply do it here
        self.current_obj.direction_callback("down")  # example 1

        self.current_direction = 'down'  # stores the direction  where the face of bot is

        self.steps = 1  # number of steps taken by the bot

        self.visited = np.zeros(
            (self.current_obj.walls.height, self.current_obj.walls.width))  # places visted by the bot

        self.blocked_places = []  # dead-ends

        self.steps_taken = [self.current_obj.walls.start,
                            self.current_obj.current]  # the steps taken by bot, in order

        self.wall_callback()  # start exploring the maze

    def wall_callback(self):

        # current_obj has all the attributes to help you in in your path planning !
        # Your code goes here. You need to figure out an algorithm to decide on the best direction of movement of the bot based on the data you have.
        # after deciding on the direction, you need to call the direction_callback() function as done in example 1.
        # dir=['up','down','left','right']

        # till the bot reaches the end
        while self.current_obj.current != self.current_obj.walls.end:

            position = self.current_obj.current  # current position of the bot

            self.visited[position[0]][position[1]] += 1

            # set of directions which are legal
            dirs = self.get_probable_dir(position)

            # to decide the best direction to be taken
            dir_prob = {}

            for dir in dirs:

                dir_prob[dir] = 0

                # where the bot would be if the step is taken
                next_pos = self.get_next_position(dir)

                # penalize if the next point is already visited
                dir_prob[dir] -= self.visited[next_pos[0]][next_pos[1]]

                # visit unvisited places to explore the map.
                if self.visited[next_pos[0]][next_pos[1]] == 0:
                    dir_prob[dir] += 10

                # if next step is end take it.
                if next_pos == self.current_obj.walls.end:
                    dir_prob[dir] += 1000

                # avoid blocked places at all cost
                if self.get_next_position(dir) in self.blocked_places:
                    dir_prob[dir] -= 100000

                # try to get closer to the end in every step
                if self.closer_to_end(dir):
                    dir_prob[dir] += 2

                # a path of length 2 is most probably a loop,so avoid taking it.
                if len(dir) == 2:
                    dir_prob[dir] -= 10

            v = list(dir_prob.values())

            # stores the directions with maximum probability.
            max_prob_dir = []

            for dir in dir_prob:
                if dir_prob[dir] == max(v):
                    max_prob_dir.append(dir)

            # From the directions who have maximum probability,choose a random one
            dir = random.choice(max_prob_dir)
            self.current_dir = dir

            # Move to the decided point.
            self.current_obj.direction_callback(dir)

            # if a place is visited twice,add it to blocked place,this makes sure that dead-ends and loops are detected
            if self.current_obj.current in self.steps_taken:
                self.blocked_places.append(position)

            # add the current point to steps_taken
            self.steps_taken.append(self.current_obj.current)

            self.steps += 1

        # make a path from the steps_taken.Eliminates all the loops
        self.path = self.make_path()

        # display the generated map.
        self.show_path(self.path)

    def get_next_position(self, direction):
        '''returns the position bot will be at if it moves in the geiven direction'''

        if direction == 'up':
            if self.current_obj.current[0] >= 1:
                return (self.current_obj.current[0]-1, self.current_obj.current[1])

        elif direction == 'left':
            if self.current_obj.current[1] >= 1:
                return (self.current_obj.current[0], self.current_obj.current[1]-1)

        elif direction == 'right':
            return (self.current_obj.current[0], self.current_obj.current[1]+1)

        elif direction == 'down':
            return (self.current_obj.current[0]+1, self.current_obj.current[1])

    def get_probable_dir(self, position):
        '''return the directions which are legal to take'''

        walls = self.current_obj.walls
        dirs = ['left', 'right', 'up', 'down']

        if(walls.check_left_wall(position)):
            dirs.remove('left')

        if(walls.check_right_wall(position)):
            dirs.remove('right')

        if(walls.check_top_wall(position)):
            dirs.remove('up')

        if(walls.check_bottom_wall(position)):
            dirs.remove('down')

        return dirs

    def closer_to_end(self, dir):
        '''returns true if the bot move closer to the end if it moves in the given direction'''

        end = self.current_obj.walls.end

        current = self.current_obj.current
        next = self.get_next_position(dir)

        dist0 = math.sqrt((current[0]-end[0])**2+(current[1]-end[1])**2)
        dist1 = math.sqrt((next[0]-end[0])**2+(next[1]-end[1])**2)

        return dist1 < dist0

    def make_path(self):
        '''Makes the most optimal path given the steps_taken by the bot in reaching the end'''
        # Alogrithm-
        # 1.Only consider the points where the bot has been to,others are pseudo walls.
        # 2.Put a 1 at starting point.
        # 3.Everywhere around 1,put 2 if no wall
        # 4.Everywhere around 2, put 3 if no wall
        # 5.Continue till we reach the end
        # 6.The number at the end is the actual path length

        steps = self.steps_taken

        start = self.current_obj.walls.start
        end = self.current_obj.walls.end

        a = np.ones((self.current_obj.walls.height,
                    self.current_obj.walls.width),
                    dtype=np.uint32)

        for x in range(self.current_obj.walls.height):
            for y in range(self.current_obj.walls.width):

                if (x, y) in steps:
                    a[x][y] = 0

        # start with a blank matrix
        m = np.zeros_like(a)

        # assign one to the starting point
        m[start[0]][start[1]] = 1

        # the counter of steps
        k = 0

        while m[end[0]][end[1]] == 0:

            # take the next step
            k += 1

            # the following nested loops are used to make one step
            for i in range(len(m)):
                for j in range(len(m[i])):

                    # use this object to get the walls' info at the given point.
                    walls = self.current_obj.walls

                    # if we find the value of some point equal to k->
                    if m[i][j] == k:

                        # if there is no number yet,and there is no wall(including pseudo wall),
                        # set k+1 to that cell

                        if i > 0 and m[i-1][j] == 0 and a[i-1][j] == 0 and not walls.check_top_wall((i, j)):
                            m[i-1][j] = k + 1

                        if j > 0 and m[i][j-1] == 0 and a[i][j-1] == 0 and not walls.check_left_wall((i, j)):
                            m[i][j-1] = k + 1

                        if i < len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0 and not walls.check_bottom_wall((i, j)):
                            m[i+1][j] = k + 1

                        if j < len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0 and not walls.check_right_wall((i, j)):
                            m[i][j+1] = k + 1
        # now we need to find the shortest path based on the m-matrix

        # start from the end point
        i, j = end

        # the value of end point in m
        k = m[i][j]

        # store the path here,(reversed)
        path = [(i, j)]

        # till we reach the start again
        while k > 1:

            # find a neighbour cell with value k-1, go there decrease k by 1.

            if i > 0 and m[i - 1][j] == k-1:
                i, j = i-1, j
                path.append((i, j))
                k -= 1

            elif j > 0 and m[i][j - 1] == k-1:
                i, j = i, j-1
                path.append((i, j))
                k -= 1

            elif i < len(m) - 1 and m[i + 1][j] == k-1:
                i, j = i+1, j
                path.append((i, j))
                k -= 1

            elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
                i, j = i, j+1
                path.append((i, j))
                k -= 1

        # the path is from end-point to start-point so reverse it.
        path.reverse()

        # return the path calculated
        return path

    def show_path(self, path):
        '''Displays the shortest path decide by the bot'''

        width = self.current_obj.walls.width
        height = self.current_obj.walls.height
        print_root = tkinter.Tk()
        print_canvas = tkinter.Canvas(
            print_root, bg="white", height=50+height*50, width=50+width*50)
        end = self.current_obj.walls.end
        start = self.current_obj.walls.start
        print_canvas.create_rectangle(
            (50+(end[1]*50)), (50+(end[0]*50)), (50+((end[1]+1)*50)), (50+((end[0]+1)*50)), fill="#0000ff")
        print_canvas.create_rectangle((50+(start[1]*50)), (50+(start[0]*50)), (50+(
            (start[1]+1)*50)), (50+((start[0]+1)*50)), fill="#000000")
        for step in path:
            if step == end or step == start:
                continue
            print_canvas.create_rectangle(
                (50+(step[1]*50)), (50+(step[0]*50)), (50+((step[1]+1)*50)), (50+((step[0]+1)*50)), fill="#00ff00")
        print_canvas.pack()
        print_canvas.update()
        print_root.mainloop()


if __name__ == '__main__':

    start_obj = PlannerNode()

    print("Number of steps taken by the bot are = ", len(start_obj.steps_taken))
    print("The length of path found by the bot is = ", len(start_obj.path))
    print("Path- ", start_obj.path)

    start_obj.current_obj.print_root.mainloop()
 """