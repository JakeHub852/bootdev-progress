class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        # Store the two corner points as private attributes
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        # Left edge is the smaller of the two x-values
        return min(self.__x1, self.__x2)

    def get_right_x(self):
        # Right edge is the larger of the two x-values
        return max(self.__x1, self.__x2)

    def get_top_y(self):
        # Top edge is the larger of the two y-values (higher on Cartesian plane)
        return max(self.__y1, self.__y2)

    def get_bottom_y(self):
        # Bottom edge is the smaller of the two y-values (lower on Cartesian plane)
        return min(self.__y1, self.__y2)

    # don't touch below this line

    def __repr__(self):
        # Helpful string representation for debugging/printing
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
