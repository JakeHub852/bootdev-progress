class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        return (
            self.pos_x >= x1
            and self.pos_x <= x2
            and self.pos_y >= y1
            and self.pos_y <= y2
        )


# don't touch above this line


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        # Initialize shared Unit fields; name and center position
        super().__init__(name, pos_x, pos_y)

        # Store dragon-specific properties
        self.height = height
        self.width = width
        self.fire_range = fire_range

        # Build the dragon's hit box as a rectangle using its center
        # Half sizes let us convert center-based position to corner coordinates
        half_w = self.width / 2 
        half_h = self.height / 2

        # Rectangle expects two opposite corners (x1, y1) and (x2, y2)
        # Left = center_x - half_w
        # Right = center_x + half_w
        # Bottom = center_y - half_h
        # Top = center_y + half_h
        self.__hit_box = Rectangle(
            self.pos_x - half_w,
            self.pos_y - half_h,
            self.pos_x + half_w,
            self.pos_y + half_h
        )
    def in_area(self, x1, y1, x2, y2):
        # Create a rectangle for the queried area
        area = Rectangle(x1, y1, x2, y2)
        # A dragon is "in" if its hit box overlaps the area at all
        return area.overlaps(self.__hit_box)


# don't touch below this line


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2
