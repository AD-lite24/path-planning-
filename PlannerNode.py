import sys

from MapNode import MapNode

class PlannerNode:
    stack = []
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

    




    def wall_callback(self, notDir):
        # current_obj has all the attributes to help you in in your path planning !
        
        current_coords = self.current_obj.current
        end_coords = self.current_obj.map.end
        tileNum = self.current_obj.array[current_coords[0]][current_coords[1]]
        print(self.current_obj.current)

        self.stack.append(current_coords)

        def getCost(reqCoords):
            cost = abs(reqCoords[0] - end_coords[0]) + abs(reqCoords[1] - end_coords[1])
            return cost

        if (tileNum == )
        

if __name__ == '__main__':
    start_obj=PlannerNode()
    start_obj.current_obj.print_root.mainloop()
 