class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        # Treat (x_1, y_1) as bottom-left and (x_2, y_2) as top-right of a rectangle.
        # Return True if the unit's position lies inside or on the rectangle's edges.
        if self.pos_x >= x_1 and self.pos_x <= x_2:
            if self.pos_y >= y_1 and self.pos_y <= y_2:
                return True
            else:
                return False
        else:
            return False
        

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range # Inclusive radius of the fire square
        
    def breathe_fire(self, x, y, units):
        # Compute the inclusive square centered at (x,y)
        # Offsts are +/- fire_range along both axes
        x_min = x - self.__fire_range
        y_min = y - self.__fire_range 
        x_max = x + self.__fire_range
        y_max = y + self.__fire_range
        
        hit = [] # Collect units that fall within the target area
        for u in units:
            # Delegate the rectangle check to the unit's in_area method
            if u.in_area(x_min, y_min, x_max, y_max):
                hit.append(u) # Record this unit as hit by the blast
        return hit # Report all impacted units
        
