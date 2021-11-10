import math

def paint_calc(cover, width, height):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You will need to purchase {num_of_cans} cans of paint.")

height = int(input("Enter the heitgh: "))
width = int(input("Enter the width: "))
cover = 5

paint_calc(cover = cover, width = width, height = height)