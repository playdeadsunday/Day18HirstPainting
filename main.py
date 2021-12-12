import turtle as t
from random import choice
# import colorgram

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")

color_list = [(246, 245, 243), (232, 238, 246), (247, 238, 242), (239, 246, 243), (131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]
tim.penup()
tim.setx(-225)
tim.sety(-225)

for _ in range(10):
    for _ in range(10):
        tim.color(choice(color_list))
        tim.pendown()
        tim.dot(20)
        tim.penup()
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.setx(-225)
    tim.right(90)

# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)

screen = t.Screen()
screen.exitonclick()