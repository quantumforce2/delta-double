import turtle

class Border(object):
    def __init__(self, min_length, max_length, border_color='black', border_bg_color='white', size=5):
        self.max_length = max_length
        self.min_length = min_length
        self.border_color = border_color
        self.border_bg_color = border_bg_color
        self.size = size

        # Set canvas properties
        wn = turtle.Screen()
        wn.bgcolor(border_bg_color)

        t = turtle.Turtle()
        t.hideturtle()
        t.pensize(size)
        t.pencolor(border_color)
        t.up()
        t.goto(max_length, max_length)
        t.down()
        t.goto(max_length, min_length)
        t.goto(min_length, min_length)
        t.goto(min_length, max_length)
        t.goto(max_length, max_length)


# This is base class of the shape unit.
class BaseCellUnit(object):
    # define no of units created
    static_cell_count = 0

    def __init__(self, x_axis, y_axis, front_cell, color='black', Target=False):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.front_cell = front_cell
        self.Target = Target

        # Count no of cell created
        if Target is False:
            HeaderUnit.static_cell_count += 1

        # Set the shape properties
        self.t = turtle.Turtle()
        #self.t.write()
        self.t.up()
        self.t.setpos(self.x_axis, self.y_axis)
        self.t.shape('square')
        self.t.shapesize(0.5, 0.5)
        self.t.fillcolor(color)
        self.t.speed(0)

        # Turn off the delay speed up
        wn = turtle.Screen()
        wn.delay(0)

    def position(self):
        return self.t.pos()


# This is the header class that response to the key events
class HeaderUnit(BaseCellUnit):
    # current cell coordinate information for moving them
    x_current = 0
    y_current = 0
    x_prev = 0
    y_prev = 0
    current_direction = 'right'
    prev_direction = 0

    def __init__(self, x_axis, y_axis, front_cell, color='black', Target = False):
        BaseCellUnit.__init__(self, x_axis, y_axis, front_cell, color, Target=False)
        self.t.speed(10)
        x, y = self.t.pos()
        self.x_prev, self.prev = x, y
        self.activate_event()

    # Returns TRUE if the shape object is a leading one
    def is_front_cell(self):
        return self.front_cell

    # Activates all the arrow key events
    def activate_event(self):
        self.ts = self.t.getscreen()
        self.ts.onkeypress(self.move_left, "Left")
        self.ts.onkeypress(self.move_right, "Right")
        self.ts.onkeypress(self.move_up, "Up")
        self.ts.onkeypress(self.move_down, "Down")
        self.ts.listen()

    # Move the header cell to a certain direction
    def move_head_cell(self, gap):
        x, y = self.t.pos()
        self.x_prev, self.y_prev = x, y
        if self.prev_direction != self.current_direction:
            gap = 0

        if self.current_direction == 'right':
            self.t.setpos(x + gap, y)
        elif self.current_direction == 'left':
            self.t.setpos(x - gap, y)
        elif self.current_direction == 'up':
            self.t.setpos(x, y + gap)
        elif self.current_direction == 'down':
            self.t.setpos(x, y - gap)
        else:
            pass

        self.prev_direction = self.current_direction
        self.x_current, self.y_current = self.t.pos()

    # Move left event
    def move_left(self):
        if self.current_direction != 'right':
            self.current_direction = 'left'

    # Move Right event
    def move_right(self):
        if self.current_direction != 'left':
            self.current_direction = 'right'

    # Move Up event
    def move_up(self):
        if self.current_direction != 'down':
            self.current_direction = 'up'

    # Move Down event
    def move_down(self):
        if self.current_direction != 'up':
            self.current_direction = 'down'


# This is the Follower class that follows header shape or a prev shape
class FollowerUnits(BaseCellUnit):
    is_last_cell = True
    t_prev = None
    x_prev = 0
    y_prev = 0
    x_current = 0
    y_current = 0

    def __init__(self,x_axis,y_axis, front_cell, t_prev, color='black', Target=False):
        BaseCellUnit.__init__(self, x_axis, y_axis, front_cell, color, Target=False)
        self.is_last_cell = True
        self.t_prev = t_prev

    def set_pos(self, x, y):
        self.x_prev, self.y_prev = self.t.pos()
        self.t.goto(x, y)
        self.x_current, self.y_current = self.t.pos()



