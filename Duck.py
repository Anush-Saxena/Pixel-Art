import turtle

def show(x,y):
	cursor.up()
	cursor.goto(x,y)
	cursor.down()

def pixel(x,y,color):
	show(x,y)
	cursor.color(color)
	cursor.begin_fill()
	for i in range(4):
		cursor.fd(20)
		cursor.rt(90)
	cursor.end_fill()

cursor = turtle.Turtle()
cursor.speed(0)
turtle.bgcolor("#bbbbbb")

for i in range(5):
	for j in range(8):
		pixel(60+20*j,20+20*i,"#fee300")


for i in range(5):
	for j in range(5):
		pixel(60+20*j,140+20*i,"#fee300")


for i in range(6):
	pixel(80+20*i,0,"#202020")
pixel(200,20,"#202020")
for i in range(4):
	pixel(220,40+20*i,"#202020")
pixel(200,120,"#202020")
for i in range(3):
	pixel(180-20*i,100,"#202020")
for i in range(3):
	pixel(80+20*i,120,"#202020")

pixel(60,100,"#202020")
for i in range(3):
	pixel(40,80-20*i,"#202020")
pixel(60,20,"#202020")
#y=140
#x=
pixel(140,140,"#202020")
for i in range(3):
	pixel(160,160+20*i,"#202020")
pixel(140,220,"#202020")
for i in range(3):
	pixel(120-20*i,240,"#202020")
pixel(60,220,"#202020")
pixel(40,200,"#202020")
pixel(20,200,"#202020")
pixel(0,180,"#202020")
pixel(20,160,"#202020")
pixel(40,160,"#202020")
pixel(40,180,"#202020")
pixel(20,180,"#f7921d")
pixel(60,140,"#202020")
pixel(80,180,"#202020")

input()
