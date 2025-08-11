import math 

x_1=float(input('enter the coordinate for x_1: '))
type(x_1)
y_1=float(input('enter the coordinate for y_1: '))
x_2=float(input('enter the coordinate for x_2: '))
y_2=float(input('enter the coordinate for xy_2: '))

# bulidng the function

# def compute_distance(x_1, y_1, x_2, y_2):
#     ((x_2-x_1)**2 + (y_2-y_1)**2)*1/2

# use import math     
def compute_distance(x_1, y_1, x_2, y_2):
    return math.sqrt(((x_2-x_1)**2 + (y_2-y_1)**2)*1/2 )
print(f'The distance is {compute_distance(x_1, y_1, x_2, y_2)} units')