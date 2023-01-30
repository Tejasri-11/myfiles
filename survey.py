

import turtle

screen = turtle.getscreen()
pen = turtle.Turtle()       

def draw_i():
	pen.forward(50)
	pen.backward(25)
	pen.right(90)
	pen.forward(140)
	pen.left(90)
	pen.forward(25)
	pen.backward(50)

def love(fill='pink'):
	
	pen.fillcolor(fill)
	pen.begin_fill()

	pen.left(50)
	pen.forward(100)
	pen.circle(40, 180)
	pen.left(260)
	pen.circle(40, 180)
	pen.forward(100)
	pen.end_fill()

def draw_u():
	pen.up()
	pen.left(90)
	pen.forward(170)
	pen.right(130)
	pen.backward(25)
	pen.down()      
	pen.forward(100)
	pen.circle(40, 180)
	pen.forward(100)

def stickman(gender='m'):
	
	pen.right(60)
	pen.forward(50)
	pen.left(120)
	pen.forward(50)
	pen.backward(50)
	pen.right(150)
	pen.forward(60)

	pen.right(120)
	pen.forward(50)
	pen.backward(50)
	pen.right(180)

	pen.left(60)
	pen.forward(50)
	pen.backward(50)

	pen.right(210)

	if gender == 'f':
		
		pen.forward(30)
		pen.left(90)
		pen.forward(10)
		pen.circle(30, 180)
		pen.forward(10)
		pen.left(90)
		pen.forward(30)
		return

	
	pen.circle(20, 360)
	


pen.pensize(6)
pen.speed(1)

 
pen.up()  
pen.left(180)
pen.forward(130)
pen.down()       



draw_i()


pen.up()
pen.home()
pen.down()


love('red')

draw_u()


pen.up()
pen.home()


pen.fillcolor('black')
pen.right(90)
pen.forward(170)
pen.left(90)
pen.down()

pen.up()  
pen.left(180)
pen.forward(130)
pen.down()       

stickman()      


pen.up()
pen.forward(350)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.down()

stickman(gender='f')  


pen.up()
pen.home()
pen.right(90)
pen.forward(170)
pen.left(90)
pen.down()
love('white')


pen.up()
pen.left(170)
pen.forward(80)
pen.write("Can We ?", font=('Arial', 14, 'bold'))

pen.screen.exitonclick()  
