# The following code allows the user to enter the values of the sides of a triangle and determines what type of triangle it is

def determine_triangle_type(A, B, C):
    if A == B and B == C:
        print('The triangle is equilateral.\n')
    elif (A == B  or B == C or A == C): 
        print('The triangle is isosceles.\n')
    else:
        print('The triangle is scalene.\n')

def get_valid_side(side_name):
    while True:
        try:
            side = float(input(f'Please enter the size of the side {side_name} of the triangle: '))
            if side <= 0:
                print('You must enter a positive value.')
            else:
                return side
        except:
            print('You must enter a number.')

def main():
    while True:
        print('\nEnter the values of the sides of a triangle to determine its type.')

        side_a = get_valid_side('A')
        side_b = get_valid_side('B')
        side_c = get_valid_side('C')
        
        determine_triangle_type(side_a, side_b, side_c)
        
        cont = input('Do you want to try with another triangle? [y/n] ')
        if cont == 'n':
            print('Bye.')
            break

if __name__ == "__main__":
    main()
