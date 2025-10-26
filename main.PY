import math
print("This program supports the calculation of area, perimeter , number of diagonals , length of diagonals(square and rectangle only)and also visual pictures for square,triangle and rectangle")
print("The allowed shapes are square,rectangle,triangle,pentagon,hexagon,heptagon,octagon,nonagon,decagon")
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def number_of_diagonals(self):
        no_ofdiagonals = self.sides * (self.sides - 3) // 2
        return f"Number of Diagonals = {no_ofdiagonals}"


class RegularPolygon(Polygon):
    def __init__(self, sides, side_length):
        super().__init__(sides)
        self.side_length = side_length

    def get_perimeter(self):
        return f"Perimeter = {self.sides * self.side_length}"

    def get_area(self):
        n = self.sides
        s = self.side_length
        area = (n * s**2) / (4 * math.tan(math.pi / n))
        return f"Area = {area}"
    def get_diagonal_lengths(self):
        n = self.sides
        s = self.side_length
        R = s / (2 * math.sin(math.pi / n))
        diagonals = []
        for k in range(2, n // 2 + 1):  
            d = 2 * R * math.sin(k * math.pi / n)
            diagonals.append(round(d, 4))
        return f"Diagonal lengths = {diagonals}"


    
class Triangle(RegularPolygon):
    def __init__(self, side_length):
        
        super().__init__(3, side_length)

    def get_picture(self):
        picture = ""
        for i in range(1, self.side_length + 1):
            picture += " " * (self.side_length - i) + "* " * i + "\n"
        return picture



class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return f"Area = {self.width * self.height}"

    def get_perimeter(self):
        return f"Perimeter = {2 * (self.width + self.height)}"

    def get_diagonal_length(self):
        return f"Diagonal Length = {(self.width ** 2 + self.height ** 2) ** 0.5}"

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "* " * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        numberofsquares = (self.width // shape.width) * (self.height // shape.height)
        return f"The number of squares that can fit into the rectangle = {numberofsquares} "


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

while True:
        print("\n")
        
        choice = input("Enter the name of the shape (rectangle,square OR both OR any other polygon): ").strip().lower()

        if choice=="exit":
            print("Exiting the program..")
            break
        elif choice == "rectangle":
            w = int(input("Enter the width of the rectangle: "))
            h = int(input("Enter the height of the rectangle: "))
            rect = Rectangle(w, h)
            print(rect.get_area())
            print(rect.get_diagonal_length())
            print(rect.number_of_diagonals())
            print(rect.get_perimeter())
            print(rect)
            print(rect.get_picture())


        elif choice == "square":
            side = int(input("Enter the side length of the square: "))
            sq = Square(side)
            print(sq.get_area())
            print(sq.get_diagonal_length())
            print(sq.number_of_diagonals())
            print(sq)
            print(sq.get_picture())
        
        elif choice=="both":
            w=int(input("Enter the width of the rectangle:"))
            h=int(input("Enter the height of the rectangle:"))
            print("RECTANGLE")

            rect = Rectangle(w,h)

        
            print(rect.get_area())        
            rect.set_height(h)
            print(rect.get_diagonal_length())
            print(rect.number_of_diagonals())
            print(rect.get_perimeter())
            print(rect)
            print(rect.get_picture())

            side=int(input("Enter the side length of the square:"))

            print("SQUARE")

            sq = Square(side)
            print(sq.get_area())
            sq.set_side(side)
            print(sq.get_diagonal_length())
            print(sq.number_of_diagonals())
            print(sq)                    
            print(sq.get_picture())
            

            another_choice=input("Do you want to know the number of squares that can fit into a rectangle?:").lower()
            if another_choice=="yes":
                rect = Rectangle(w,h)
                sq = Square(side)
                rect.set_width(w)
                rect.set_height(h)
                print(rect.get_amount_inside(sq))


        elif choice == "pentagon":
            sidelength=int(input("Enter the side length: "))
            pent = RegularPolygon(5,sidelength)
            print("Sides of pentagon = 5")
            print(pent.get_area())
            print(pent.number_of_diagonals())
            print(pent.get_perimeter())
            print(pent.get_diagonal_lengths())



        elif choice == "triangle":
            sidelength=int(input("Enter the side length: "))
            tri=Triangle(sidelength)
            print("Sides of triangle = 3")
            print(tri.get_area())
            print(tri.number_of_diagonals())
            print(tri.get_perimeter())
            print(tri.get_picture())


        elif choice=="hexagon":
            sidelength=int(input("Enter the side length: "))
            hex = RegularPolygon(6,sidelength)
            print("Sides of hexagon = 6")
            print(hex.get_area())
            print(hex.number_of_diagonals())
            print(hex.get_perimeter())
            print(hex.get_diagonal_lengths())


        elif choice=="heptagon":
            sidelength=int(input("Enter the side length: "))
            hep = RegularPolygon(7,sidelength)
            print("Sides of heptagon = 7")
            print(hep.get_area())
            print(hep.number_of_diagonals())
            print(hep.get_perimeter())
            print(hep.get_diagonal_lengths())


        elif choice=="octagon":
            sidelength=int(input("Enter the side length: "))
            oct = RegularPolygon(8,sidelength)
            print("Sides of octagon = 8")
            print(oct.get_area())
            print(oct.number_of_diagonals())
            print(oct.get_perimeter())
            print(oct.get_diagonal_lengths())


        elif choice == "nonagon":
            sidelength=int(input("Enter the side length: "))
            nana = RegularPolygon(9,sidelength)
            print("Sides of nonagon = 9")
            print(nana.get_area())
            print(nana.number_of_diagonals())
            print(nana.get_perimeter())
            print(nana.get_diagonal_lengths())


        elif choice =="decagon":
            sidelength=int(input("Enter the side length: "))
            dec = RegularPolygon(10,sidelength)
            print("Sides of decagon = 10")
            print(dec.get_area())
            print(dec.number_of_diagonals())
            print(dec.get_perimeter())
            print(dec.get_diagonal_lengths())

        else:
            
            print("Invalid input. Please type a valid shape or 'exit' to quit.")