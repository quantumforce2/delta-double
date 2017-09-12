import random
import time
import Snake
import turtle

# ********************** main programme ****************************
dict_snake_properties = {
    'base_unit_bg_color': 'red',
    'follower_units_bg_color': 'black',
    'header_unit_bg_color': 'black',
    'border_max_length': 300,
    'border_min_length': -300,
    'gap': 11
}

def game_over_text(points):
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.delay(0)
    t.up()
    t.setpos (-180, 270)
    t.write("**** <<Game over>> points gain >> " + str(points) + " ***", move=False, align="left", font=("Courier", 12, "normal"))
    t.hideturtle()
    t.speed(0)
    t = None

def show_points(t, points):
    t.clear()
    t.write("<<score: " + str(points) + ">>", move=False, align="left",
            font=("Courier", 12, "normal"))


# Create a border
b = Snake.Border(-311, 311, 'blue')


def create_target():
    # Create target
    x_target = random.randint(dict_snake_properties['border_min_length'], dict_snake_properties['border_max_length'])
    y_target = random.randint(dict_snake_properties['border_min_length'], dict_snake_properties['border_max_length'])
    sh_target = Snake.BaseCellUnit(x_target, y_target, False, dict_snake_properties['base_unit_bg_color'], True)


# Create target
x_target = random.randint(dict_snake_properties['border_min_length'], dict_snake_properties['border_max_length'])
y_target = random.randint(dict_snake_properties['border_min_length'], dict_snake_properties['border_max_length'])
sh_target = Snake.BaseCellUnit(x_target, y_target, False, dict_snake_properties['base_unit_bg_color'], True)


# Create the header unit
head_unit = Snake.HeaderUnit(10, 0, True, dict_snake_properties['header_unit_bg_color'])
gap = dict_snake_properties['gap']

# array of cells units
t = None
t = []
t.append(head_unit)
x = 1

# Store current addresses of follower units
t_curr = {}


# score units
t_score = turtle.Turtle()
t_score.up()
t_score.setpos(200, dict_snake_properties['border_min_length']-40)
t_score.hideturtle()

game_continue = True
while game_continue is True:
    if abs(t[0].position()[0]) >= 302 or abs(t[0].position()[1]) >= 302:
        print(t[0].position())
        game_over_text(x)
        break

    t[0].move_head_cell(gap)

    # If head unit crash with any of follower unit
    if t[0].position() in list(t_curr.values()):
        print(t[0].position(), '>>', t_curr.values())
        game_over_text(x)
        break

    if abs(sh_target.x_axis - t[0].x_current) < 8 and abs(sh_target.y_axis - t[0].y_current) < 8:
        sh_target.t.hideturtle()
        sh_target.t.goto(-999, -999)
        t.append(Snake.FollowerUnits(t[x-1].x_prev, t[x-1].y_prev, False, head_unit, dict_snake_properties['follower_units_bg_color'], True))

        # Create target
        x_target = random.randint(dict_snake_properties['border_min_length'], dict_snake_properties['border_max_length'])
        y_target = random.randint(dict_snake_properties['border_min_length'], dict_snake_properties['border_max_length'])
        sh_target = Snake.BaseCellUnit(x_target, y_target, False, dict_snake_properties['base_unit_bg_color'], True)

        x += 1

        show_points(t_score, x)

    for i in range(1, len(t)):
        t[i].set_pos(t[i - 1].x_prev, t[i - 1].y_prev)
        t_curr[i] = t[i].position()


    delay = 0.1
    time.sleep(delay)

wn = turtle.Screen()
wn.exitonclick()







