import websocket
import _thread
# import time
import ast

import pyxinput
# import json

MyVirtual = pyxinput.vController(percent=False)

button_x = False
button_y = False
button_a = False
button_b = False

button_left_shoulder = False
button_right_shoulder = False

button_dpad_up = False
button_dpad_right = False
button_dpad_down = False
button_dpad_left = False

button_left_thumb = False
button_right_thumb = False

button_start = False
button_back = False


# class VirtualGamepad:
#
#     def __init__(self):
#         """
#
#         """
#

def set_client_gamepad(gamepad_dict, gamepad_buttons):

    global button_x, button_y, button_a, button_b
    global button_left_shoulder, button_right_shoulder
    global button_dpad_up, button_dpad_right, button_dpad_down, button_dpad_left
    global button_left_thumb, button_right_thumb
    global button_start, button_back

    # TODO: Develop method to prevent unnecessarily calling set_value (if values have not changed).
    # Loop through the gamepad dictionary to set values.
    for gamepad_item in gamepad_dict:
        val = gamepad_dict[gamepad_item]

        # print('Setting value for: {0} ({1})'.format(gamepad_item, val))
        if gamepad_item == 'thumb_lx':
            MyVirtual.set_value('AxisLx', val)
        elif gamepad_item == 'thumb_ly':
            MyVirtual.set_value('AxisLy', val)
        elif gamepad_item == 'thumb_rx':
            MyVirtual.set_value('AxisRx', val)
        elif gamepad_item == 'thumb_ry':
            MyVirtual.set_value('AxisRy', val)
        elif gamepad_item == 'left_trigger':
            MyVirtual.set_value('TriggerL', val)
        elif gamepad_item == 'right_trigger':
            MyVirtual.set_value('TriggerR', val)

    # Handle any button releases before we set them again.
    # Since buttons pressed can be an empty list, a button release in the loop
    # will not be recorded as the list would be empty, so run this before checking for
    # new button presses.
    print(button_x)
    if 'X' not in gamepad_buttons and button_x is True:
        print('Release X')
        button_x = False
        # Set button x press to false.
        MyVirtual.set_value('BtnX', 0)

    if 'Y' not in gamepad_buttons and button_y is True:
        print('Release Y')
        button_y = False
        MyVirtual.set_value('BtnY', 0)

    if 'A' not in gamepad_buttons and button_a is True:
        print('Release A')
        button_a = False
        MyVirtual.set_value('BtnA', 0)

    if 'B' not in gamepad_buttons and button_b is True:
        print('Release B')
        button_b = False
        MyVirtual.set_value('BtnB', 0)

    if 'LEFT_SHOULDER' not in gamepad_buttons and button_left_shoulder is True:
        print('Release LEFT_SHOULDER')
        button_left_shoulder = False
        MyVirtual.set_value('BtnShoulderL', 0)

    if 'RIGHT_SHOULDER' not in gamepad_buttons and button_right_shoulder is True:
        print('Release RIGHT_SHOULDER')
        button_right_shoulder = False
        MyVirtual.set_value('BtnShoulderR', 0)

    # TODO: It is currently not possible to see which individual Dpad button
    #       has been released without seeing and working with the values from
    #       the controller.
    if 'DPAD_UP' not in gamepad_buttons and button_dpad_up is True:
        print('Release DPAD_UP')
        button_dpad_up = False
        # Set Dpad to off.
        MyVirtual.set_value('Dpad', 0)

    if 'DPAD_DOWN' not in gamepad_buttons and button_dpad_down is True:
        print('Release DPAD_DOWN')
        button_dpad_down = False
        # Set Dpad to off.
        MyVirtual.set_value('Dpad', 0)

    if 'DPAD_LEFT' not in gamepad_buttons and button_dpad_left is True:
        print('Release DPAD_LEFT')
        button_dpad_left = False
        # Set Dpad to off.
        MyVirtual.set_value('Dpad', 0)

    if 'DPAD_RIGHT' not in gamepad_buttons and button_dpad_right is True:
        print('Release DPAD_RIGHT')
        button_dpad_right = False
        # Set Dpad to off.
        MyVirtual.set_value('Dpad', 0)

    if 'LEFT_THUMB' not in gamepad_buttons and button_left_thumb is True:
        print('Release LEFT_THUMB')
        button_left_thumb = False
        MyVirtual.set_value('BtnThumbL', 0)

    if 'RIGHT_THUMB' not in gamepad_buttons and button_right_thumb is True:
        print('Release RIGHT_THUMB')
        button_right_thumb = False
        MyVirtual.set_value('BtnThumbR', 0)

    if 'START' not in gamepad_buttons and button_start is True:
        print('Release START')
        button_start = False
        MyVirtual.set_value('BtnStart', 0)

    if 'BACK' not in gamepad_buttons and button_back is True:
        print('Release BACK')
        button_back = False
        MyVirtual.set_value('BtnBack', 0)

    # TODO: 1. Change the structure in which button press is returned from read_state.
    # TODO: 2. Handle button press/release; what about the time in which
    #       the button is pressed for?
    # TODO: 3.. Create a way for these to be asynchronous so that a button pressed is directly
    #       set or released and not having to wait in list to be set to press/release.
    for button_no in range(len(gamepad_buttons)):
        button_name = gamepad_buttons[button_no]
        print('Handling press/release for button: ', button_name)

        # Handle buttons pressed.
        if button_name == 'X' and button_x is False:
            print('Pressed X')
            button_x = True
            # Set button X to true.
            MyVirtual.set_value('BtnX', 1)

        elif button_name == 'Y' and button_y is False:
            print('Pressed Y')
            button_y = True
            MyVirtual.set_value('BtnY', 1)

        elif button_name == 'A' and button_a is False:
            print('Pressed A')
            button_a = True
            MyVirtual.set_value('BtnA', 1)

        elif button_name == 'B' and button_b is False:
            print('Pressed B')
            button_b = True
            MyVirtual.set_value('BtnB', 1)

        elif button_name == 'LEFT_SHOULDER' and button_left_shoulder is False:
            print('Pressed left shoulder.')
            button_left_shoulder = True
            MyVirtual.set_value('BtnShoulderL', 1)

        elif button_name == 'RIGHT_SHOULDER' and button_right_shoulder is False:
            print('Pressed right shoulder.')
            button_right_shoulder = True
            MyVirtual.set_value('BtnShoulderR', 1)

        elif button_name == 'DPAD_UP' and button_dpad_up is False:
            print('Pressed Dpad Up')
            button_dpad_up = True
            MyVirtual.set_value('Dpad', 1)

        elif button_name == 'DPAD_DOWN' and button_dpad_down is False:
            print('Pressed Dpad Down')
            button_dpad_down = True
            MyVirtual.set_value('Dpad', 2)

        elif button_name == 'DPAD_LEFT' and button_dpad_left is False:
            print('Got Dpad Left')
            button_dpad_left = True
            MyVirtual.set_value('Dpad', 4)

        elif button_name == 'DPAD_RIGHT' and button_dpad_right is False:
            print('Pressed Dpad Right')
            button_dpad_right = True
            MyVirtual.set_value('Dpad', 8)

        elif button_name == 'LEFT_THUMB' and button_left_thumb is False:
            print('Pressed Left Thumbstick')
            button_left_thumb = True
            MyVirtual.set_value('BtnThumbL', 1)

        elif button_name == 'RIGHT_THUMB' and button_right_thumb is False:
            print('Pressed Right Thumbstick')
            button_right_thumb = True
            MyVirtual.set_value('BtnThumbR', 1)

        elif button_name == 'START' and button_start is False:
            print('Pressed Start')
            button_start = True
            MyVirtual.set_value('BtnStart', 1)

        elif button_name == 'BACK' and button_back is False:
            print('Pressed Back')
            button_back = True
            MyVirtual.set_value('BtnBack', 1)


def on_message(ws, message):
    message_eval = ast.literal_eval(message)

    gamepad_dict = None
    gamepad_buttons = None

    if type(message_eval) is dict:
        gamepad_dict = message_eval
        # print(gamepad_dict)
    elif type(message_eval) is list:
        gamepad_buttons = message_eval
        print(gamepad_buttons)

    # Set the values on the gamepad
    set_client_gamepad(gamepad_dict, gamepad_buttons)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        # for i in range(3):
        #     time.sleep(1)
        #     ws.send("Hello %d" % i)

        my_read = pyxinput.rController(1)

        while True:
            ws.send(str(my_read.gamepad.__dict__()))
            ws.send(str(my_read.buttons))
            # print('Read controller data')

        # time.sleep(1)
        # ws.close()
        # print("thread terminating...")

    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://youthful-driver.glitch.me/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
