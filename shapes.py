# 
# Draw shapes and learn about classes
#
import turtle

def draw_square(someturtle):

    for i in range (1,5):
        someturtle.forward(100)
        someturtle.right(90)
                
def draw_art():
    wn = turtle.Screen()
    wn.bgcolor("red")
    
    #Create a turtle where square is drawn
    sqr = turtle.Turtle()   
    sqr.shape("turtle")
    sqr.color("yellow") 
    sqr.speed(2)   
    draw_square(sqr)
    
    #Create a turtle where circle is drawn
    crcl = turtle.Turtle()
    crcl.shape("arrow")
    crcl.color("pink")
    crcl.circle(100)
    
    wn.exitonclick()
    
draw_art()