from turtle import *

#i shall cast a spell to paint yee house

#step one: paint yee walls

speed(30)

width(3)

color("yellow")
begin_fill()
forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)

end_fill()

#end of step one

#step two: PAINT THE DOOR

left(90)
forward(70)

color("green")
begin_fill()

left(90)
forward(120)

right(90)
forward(60)

right(90)
forward(120)

end_fill()

#end of step two

#step three: paint the roof

penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

#end of step three

penup()
goto(95,180)
pendown()

#step four: window

right(60)
forward(30)

left(90)
forward(40)

left(90)
forward(60)

left(90)
forward(40)

left(90)
forward(30)


left(90)
forward(40)

left(180)
forward(20)

left(90)
forward(30)

left(180)
forward(60)

penup()
goto(240,180)

#end of step four

#congratulations, you have made a house

exitonclick()