from collections import namedtuple

Rectangle = namedtuple('Rectangle',['x','y','width','height'])

rect1 = Rectangle(1,1,2,3)
rect2 = Rectangle(1,1,5,5)

#assume inputs to be tuples of type rectangles
def is_intersect(rect1,rect2):
    #condition of intersection
    if ((rect1.x+rect1.width >= rect2.x) | (rect2.x+rect2.width >= rect1.x)) & ((rect1.y + rect1.height >= rect2.y) | (rect2.y + rect2.height >= rect1.y)):
        return Rectangle(
            max(rect1.x,rect2.x),
            max(rect1.y,rect2.y),
            min(rect1.x+rect1.width,rect2.x+rect2.width)-max(rect1.x,rect2.x),
            min(rect1.y+rect1.height,rect2.y+rect2.height)-max(rect1.y,rect2.y)
        )

print(is_intersect(rect1,rect2))
