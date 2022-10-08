import re


def figure_perimetr(test1):
    points = list(map(int, re.findall(r"[0-9]", test1)))
    int_points = {["x", "y"][i%2]+str(i//2+1): v for i, v in enumerate(points)}

    first_side = ((int_points["x2"] - int_points["x1"]) ** 2 
                + (int_points["y2"] - int_points["y1"]) ** 2) ** 0.5
    second_side = ((int_points["x4"] - int_points["x2"]) ** 2
                + (int_points["y4"] - int_points["y2"]) ** 2) ** 0.5
    third_side = ((int_points["x4"] - int_points["x3"]) ** 2
                + (int_points["y4"] - int_points["y3"]) ** 2) ** 0.5
    fourth_side = ((int_points["x3"] - int_points["x1"]) ** 2
                + (int_points["y3"] - int_points["y1"]) ** 2) ** 0.5
    
    return first_side + second_side + third_side + fourth_side
        

test1 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test1))
