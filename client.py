import websocket
import _thread
import ast

import pyxinput
# import json


class VirtualGamepad:

    def __init__(self):
        """

        """

        self._button_x = False
        self._button_y = False
        self._button_a = False
        self._button_b = False

        self._button_left_shoulder = False
        self._button_right_shoulder = False

        self._button_dpad_up = False
        self._button_dpad_right = False
        self._button_dpad_down = False
        self._button_dpad_left = False

        self._button_left_thumb = False
        self._button_right_thumb = False

        self._button_start = False
        self._button_back = False

        self._virtual_controller = pyxinput.vController(percent=False)

    def set_gamepad(self, gamepad, gamepad_buttons):
        """

        :param gamepad:
        :param gamepad_buttons:
        :return:
        """

        # TODO: Develop method to prevent unnecessarily calling set_value (if values have not changed).
        # Loop through the gamepad dictionary to set values.
        if gamepad is not None:
            for gamepad_item in gamepad:
                val = gamepad[gamepad_item]

                # print('Setting value for: {0} ({1})'.format(gamepad_item, val))
                if gamepad_item == 'thumb_lx':
                    self._virtual_controller.set_value('AxisLx', val)
                elif gamepad_item == 'thumb_ly':
                    self._virtual_controller.set_value('AxisLy', val)
                elif gamepad_item == 'thumb_rx':
                    self._virtual_controller.set_value('AxisRx', val)
                elif gamepad_item == 'thumb_ry':
                    self._virtual_controller.set_value('AxisRy', val)
                elif gamepad_item == 'left_trigger':
                    self._virtual_controller.set_value('TriggerL', val)
                elif gamepad_item == 'right_trigger':
                    self._virtual_controller.set_value('TriggerR', val)

        # Handle any button releases before we set them again.
        # Since buttons pressed can be an empty list, a button release in the loop
        # will not be recorded as the list would be empty, so run this before checking for
        # new button presses.
        if gamepad_buttons is not None:
            print(gamepad_buttons)
            if 'X' not in gamepad_buttons and self._button_x is True:
                print('Release X')
                self._button_x = False
                # Set button x press to false.
                self._virtual_controller.set_value('BtnX', 0)

            if 'Y' not in gamepad_buttons and self._button_y is True:
                print('Release Y')
                self._button_y = False
                self._virtual_controller.set_value('BtnY', 0)

            if 'A' not in gamepad_buttons and self._button_a is True:
                print('Release A')
                self._button_a = False
                self._virtual_controller.set_value('BtnA', 0)

            if 'B' not in gamepad_buttons and self._button_b is True:
                print('Release B')
                self._button_b = False
                self._virtual_controller.set_value('BtnB', 0)

            if 'LEFT_SHOULDER' not in gamepad_buttons and self._button_left_shoulder is True:
                print('Release LEFT_SHOULDER')
                self._button_left_shoulder = False
                self._virtual_controller.set_value('BtnShoulderL', 0)

            if 'RIGHT_SHOULDER' not in gamepad_buttons and self._button_right_shoulder is True:
                print('Release RIGHT_SHOULDER')
                self._button_right_shoulder = False
                self._virtual_controller.set_value('BtnShoulderR', 0)

            # TODO: It is currently not possible to see which individual Dpad button
            #       has been released without seeing and working with the values from
            #       the controller.
            if 'DPAD_UP' not in gamepad_buttons and self._button_dpad_up is True:
                print('Release DPAD_UP')
                self._button_dpad_up = False
                # Set Dpad to off.
                self._virtual_controller.set_value('Dpad', 0)

            if 'DPAD_DOWN' not in gamepad_buttons and self._button_dpad_down is True:
                print('Release DPAD_DOWN')
                self._button_dpad_down = False
                # Set Dpad to off.
                self._virtual_controller.set_value('Dpad', 0)

            if 'DPAD_LEFT' not in gamepad_buttons and self._button_dpad_left is True:
                print('Release DPAD_LEFT')
                self._button_dpad_left = False
                # Set Dpad to off.
                self._virtual_controller.set_value('Dpad', 0)

            if 'DPAD_RIGHT' not in gamepad_buttons and self._button_dpad_right is True:
                print('Release DPAD_RIGHT')
                self._button_dpad_right = False
                # Set Dpad to off.
                self._virtual_controller.set_value('Dpad', 0)

            if 'LEFT_THUMB' not in gamepad_buttons and self._button_left_thumb is True:
                print('Release LEFT_THUMB')
                self._button_left_thumb = False
                self._virtual_controller.set_value('BtnThumbL', 0)

            if 'RIGHT_THUMB' not in gamepad_buttons and self._button_right_thumb is True:
                print('Release RIGHT_THUMB')
                self._button_right_thumb = False
                self._virtual_controller.set_value('BtnThumbR', 0)

            if 'START' not in gamepad_buttons and self._button_start is True:
                print('Release START')
                self._button_start = False
                self._virtual_controller.set_value('BtnStart', 0)

            if 'BACK' not in gamepad_buttons and self._button_back is True:
                print('Release BACK')
                self._button_back = False
                self._virtual_controller.set_value('BtnBack', 0)

            # TODO: 1. Change the structure in which button press is returned from read_state.
            # TODO: 2. Handle button press/release; what about the time in which
            #       the button is pressed for?
            # TODO: 3.. Create a way for these to be asynchronous so that a button pressed is directly
            #       set or released and not having to wait in list to be set to press/release.
            for button_no in range(len(gamepad_buttons)):
                button_name = gamepad_buttons[button_no]
                print('Handling press/release for button: ', button_name)

                # Handle buttons pressed.
                if button_name == 'X' and self._button_x is False:
                    print('Pressed X')
                    self._button_x = True
                    # Set button X to true.
                    self._virtual_controller.set_value('BtnX', 1)

                elif button_name == 'Y' and self._button_y is False:
                    print('Pressed Y')
                    self._button_y = True
                    self._virtual_controller.set_value('BtnY', 1)

                elif button_name == 'A' and self._button_a is False:
                    print('Pressed A')
                    self._button_a = True
                    self._virtual_controller.set_value('BtnA', 1)

                elif button_name == 'B' and self._button_b is False:
                    print('Pressed B')
                    self._button_b = True
                    self._virtual_controller.set_value('BtnB', 1)

                elif button_name == 'LEFT_SHOULDER' and self._button_left_shoulder is False:
                    print('Pressed left shoulder.')
                    self._button_left_shoulder = True
                    self._virtual_controller.set_value('BtnShoulderL', 1)

                elif button_name == 'RIGHT_SHOULDER' and self._button_right_shoulder is False:
                    print('Pressed right shoulder.')
                    self._button_right_shoulder = True
                    self._virtual_controller.set_value('BtnShoulderR', 1)

                elif button_name == 'DPAD_UP' and self._button_dpad_up is False:
                    print('Pressed Dpad Up')
                    self._button_dpad_up = True
                    self._virtual_controller.set_value('Dpad', 1)

                elif button_name == 'DPAD_DOWN' and self._button_dpad_down is False:
                    print('Pressed Dpad Down')
                    self._button_dpad_down = True
                    self._virtual_controller.set_value('Dpad', 2)

                elif button_name == 'DPAD_LEFT' and self._button_dpad_left is False:
                    print('Got Dpad Left')
                    self._button_dpad_left = True
                    self._virtual_controller.set_value('Dpad', 4)

                elif button_name == 'DPAD_RIGHT' and self._button_dpad_right is False:
                    print('Pressed Dpad Right')
                    self._button_dpad_right = True
                    self._virtual_controller.set_value('Dpad', 8)

                elif button_name == 'LEFT_THUMB' and self._button_left_thumb is False:
                    print('Pressed Left Thumbstick')
                    self._button_left_thumb = True
                    self._virtual_controller.set_value('BtnThumbL', 1)

                elif button_name == 'RIGHT_THUMB' and self._button_right_thumb is False:
                    print('Pressed Right Thumbstick')
                    self._button_right_thumb = True
                    self._virtual_controller.set_value('BtnThumbR', 1)

                elif button_name == 'START' and self._button_start is False:
                    print('Pressed Start')
                    self._button_start = True
                    self._virtual_controller.set_value('BtnStart', 1)

                elif button_name == 'BACK' and self._button_back is False:
                    print('Pressed Back')
                    self._button_back = True
                    self._virtual_controller.set_value('BtnBack', 1)


def on_message(ws, message):
    message_eval = ast.literal_eval(message)
    recv_pad = None
    recv_buttons = None

    if type(message_eval) is dict:
        recv_pad = message_eval
        print("Evaluated: ", recv_pad)

    elif type(message_eval) is list:
        recv_buttons = message_eval
        print("Evaluated: ", recv_buttons)

    # Set the values on the gamepad.
    # set_client_gamepad(gamepad, gamepad_buttons)
    my_gamepad.set_gamepad(gamepad=recv_pad, gamepad_buttons=recv_buttons)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        # for i in range(3):
        #     time.sleep(1)
        #     ws.send("Hello %d" % i)
        # time.sleep(1)
        # ws.close()
        # print("thread terminating...")

        my_read = pyxinput.rController(1)

        previous_pad = None
        previous_buttons = None
        while True:
            # msg = {'id': id, 'data': None}

            # TODO: Does adding this in change the play/movement in real time games?
            pad = my_read.gamepad.__dict__()
            if pad != previous_pad:
                # msg['data'] = pad
                ws.send(str(pad))
            previous_pad = pad

            buttons = my_read.buttons
            if buttons != previous_buttons:
                # msg['data'] = buttons
                ws.send(str(buttons))
            previous_buttons = buttons
            # print('Read controller data')
    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    # websocket.enableTrace(True)
    # print(pyxinput.vController.available_ids())

    # Create an instance of the virtual gamepad.
    my_gamepad = VirtualGamepad()

    ws = websocket.WebSocketApp("ws://youthful-driver.glitch.me/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.on_open = on_open
    ws.run_forever()
