'''Task1.Create a polygon class and
    a rectangle class that inherits
    from the polygon class and
        finds the square of rectangle.'''
class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.side_lengths = []

    def input_sides(self):
        for i in range(self.num_sides):
            length = float(input(f"Enter length of side {i + 1}: "))
            self.side_lengths.append(length)

    def display_sides(self):
        print("Side Lengths:", self.side_lengths)


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)  # A rectangle has 2 sides (length and width)

    def find_area(self):
        if len(self.side_lengths) == 2:
            length, width = self.side_lengths
            area = length * width
            print(f"Area of the rectangle: {area}")
        else:
            print("A rectangle should have exactly 2 sides (length and width).")


# Create a rectangle object
my_rectangle = Rectangle()

# Input the sides of the rectangle
my_rectangle.input_sides()

# Display the sides of the rectangle
my_rectangle.display_sides()

# Calculate and display the area of the rectangle
my_rectangle.find_area()