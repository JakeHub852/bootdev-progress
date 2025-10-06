class Rectangle:
    def overlaps(self, rect):       
        # Two rectangles overlap (including touching edges) if:
        # - this left edge is left of or equal to rect's right edge
        # - this right edge is right of or equal to rect's left edge
        # - this top edge is above or equal to rect's bottom edge
        # - this bottom edge is below or equal to rect's top edge
        # Using the helper getters keeps it robust even if x1>x2 or y1>y2
        return (
                self.get_left_x() <= rect.get_right_x()
                and self.get_right_x() >= rect.get_left_x()
                and self.get_top_y() >= rect.get_bottom_y()
                and self.get_bottom_y() <= rect.get_top_y()
        )

    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        # Store two opposite corners. Order doesn't matter;
        # accessors normalize which side is left/right/top/bottom.
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        # The smaller x is the left edge
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        # The larger x is the right edge
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        # The larger y is the top edge (y increases upward)
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        # The smaller y is the bottom edge
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        # Helpful string for debugging/printing rectangles
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
