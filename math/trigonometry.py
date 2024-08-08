'''
This module is to define the Triangle class and methods for operating with it
'''


def _is_positive(x):
    positive = True

    if isinstance(x, list):
        for i in x:
            positive = i >= 0
            if not positive:
                break
    else:
        positive = x >= 0
    return positive

class Triangle:
    '''
    The class for a triangle
    '''
    def __init__(self, a=0, b=0, c=0):
        '''
        a = The first side of the triangle
        b = The second side of the triangle
        c = Hypotenuse of the triangle

        It's necessary define two parameters of the triangle at minimun input
        '''

        # The sides cannot be negatives
        if not _is_positive([a, b, c]):
            raise ValueError("The sides of a triangle might be positive")

        # To build a triangle is necessary two sides data
        if (a == 0 and b == 0) or (a == 0 and c == 0) or (b == 0 and c == 0):
            raise ValueError("It's necessary indicate two sides at minimun")

        # Value if a is 0
        if b > 0 and c > 0 and a == 0:
            self.a = (c**2 - b**2)**0.5
        else:
            self.a = a
        # Value if b is 0
        if a > 0 and c > 0 and b == 0:
            self.b = (c**2 - a**2)**0.5
        else:
            self.b = b
        # Value if a and b are defined, to make a logical hypotenuse value
        if a > 0 and b > 0:
            self.c = self.hyp()
        else:
            self.c = c

    def perimeter(self):
        '''
        Returns the perimeter of the triangle
        '''
        return self.a + self.b + self.c

    def area(self):
        '''
        Returns the area of the triangle
        '''

    def hyp(self):
        '''
        Returns the hypotenuse of the triangle
        '''
        return (self.a**2 + self.b**2)**0.5
