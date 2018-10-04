from turtle import *
def tree ( levels, length ):
    if levels > 0:
        forward ( length )
        left ( 45 )
        tree ( levels-1, length*0.6)
        right ( 90 )
        tree ( levels-1, length*0.6)
        left ( 45 )
        backward ( length )
setheading ( 90 )
tree ( 5, 100 )