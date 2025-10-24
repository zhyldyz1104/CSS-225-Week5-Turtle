# Zhyldyz
# 10/21/25

# Problem 1------------------------------------------------------------
# count = 0  #we need to control the loop so it won't print more than 100 times
# while count <= 100:  #while the "controller of the loop" is less than 100, function is working
#     print("Hello World")
#     count = count + 1 #if we do not put this, the number stays same so the function will go forever because count=0

# Problem 2------------------------------------------------
# list = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for item in list:
#     print(item)
#    print(item ** 2)

# -Problem 3--------------------------,,,,,,,,
# import turtle
#
# t = turtle.Turtle()
# number_of_sides = int(input("How many sides do you want?"))
# length = int(input("How long do you want?"))
# color = input("What color do you want?")
# color_of_polygon = input("What color do you want?")
# t.color(color)
# t.fillcolor(color_of_polygon)
# t.begin_fill()
# for i in range(number_of_sides):
#     t.forward(length)
#     t.left(360 / number_of_sides)
# t.end_fill()
# turtle.done()

# Problem 4-------------------------------------------------
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, "divisible by both")
#     elif i % 3 == 0:
#         print(i, "is divisible by 3")
#     elif i % 5 == 0:
#         print(i, "is divisible by 5")
#     else:
#         print(i)
# problem 5---------------------------------------------
# import turtle
#
# t = turtle.Turtle()
# t.speed(3)
# # the stem
# t.color("green")
# t.begin_fill()
# t.forward(20)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(20)
# t.left(90)
# t.forward(200)
# t.end_fill()
#
# # end of the stem
# # t.penup()
# # t.goto(10, 300)
# # t.pendown()
# # start petals
# def draw_petal():
#     t.begin_fill()
#     t.circle(29)  # радиус лепестка
#     t.end_fill()
#
#
# # loop for 5
# t.color("hotpink")
# t.penup()
# t.goto(-30, 270)
# t.pendown()
# for _ in range(5):
#     draw_petal()
#     t.penup()
#     t.forward(60)
#     t.left(72)
#     t.pendown()
#
# # end petals
# # start center flower
# t.penup()
# t.goto(10, 220)
# t.pendown()
# t.color("yellow")
# t.begin_fill()
# t.left(90)
# t.circle(20)
# t.end_fill()
# t.color("red")
# # end center
# turtle.done()
