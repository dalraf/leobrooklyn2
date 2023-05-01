class Check_key:
    def __init__(self, pyxel, event, player):
        self.event = event
        self.player = player
        self.pyxel = pyxel
        self.hold = 1
        self.repeat = 1

    def check_key_pressed(self):
        if self.pyxel.btnp(self.pyxel.KEY_Q):
            self.event.event_quit()

        elif self.pyxel.btnp(
            self.pyxel.KEY_LEFT, hold=self.hold, repeat=self.repeat
        ) or self.pyxel.btn(self.pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.event.event_player_left()

        elif self.pyxel.btnp(
            self.pyxel.KEY_RIGHT, hold=self.hold, repeat=self.repeat
        ) or self.pyxel.btn(self.pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.event.event_player_right()

        elif self.pyxel.btnp(
            self.pyxel.KEY_DOWN, hold=self.hold, repeat=self.repeat
        ) or self.pyxel.btn(self.pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.event.event_player_down()

        elif self.pyxel.btnp(
            self.pyxel.KEY_UP, hold=self.hold, repeat=self.repeat
        ) or self.pyxel.btn(self.pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.event.event_player_up()

        elif self.pyxel.btnp(
            self.pyxel.KEY_CTRL, hold=self.hold, repeat=self.repeat
        ) or self.pyxel.btn(self.pyxel.GAMEPAD1_BUTTON_X):
            self.event.event_player_attacking()

        elif self.pyxel.btnp(
            self.pyxel.KEY_SPACE, hold=self.hold, repeat=self.repeat
        ) or self.pyxel.btn(self.pyxel.GAMEPAD1_BUTTON_Y):
            self.event.event_player_shotting()

        else:
            self.event.event_player_stopped()
