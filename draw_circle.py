import turtle

def draw_cicular_square():
    
    window = turtle.Screen()
    window.bgcolor("white")
    line = turtle.Turtle()
    line.shape("turtle")
	
	#the speed is change as recommended
    line.speed(40)
    line.color("green")
    for a in range(36):
        line.right(10)
        
        for i in range(4):
            line.forward(100)
            line.right(90)

    
    window.exitonclick()

    
draw_cicular_square()

