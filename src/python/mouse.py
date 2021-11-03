from pynput.mouse import Controller as MouseController
mouse = MouseController()

def start(currentPosition, PIXELS_TO_MOVE) :
   move_mouse(currentPosition, PIXELS_TO_MOVE)


def move_mouse_when_unable_to_move(expected_mouse_position):
    if expected_mouse_position != mouse.position:
        mouse.position = (0, 0)



def move_mouse(currentPosition, PIXELS_TO_MOVE):
    new_x = currentPosition[0] + PIXELS_TO_MOVE
    new_y = currentPosition[1] + PIXELS_TO_MOVE

    new_position = (new_x, new_y)
    mouse.position = new_position

    move_mouse_when_unable_to_move(new_position)

    current_position = mouse.position

    print('Mouse moved to: ', current_position)

    return current_position
