class Check_key:
    def __init__(self, pyxel, event, player):
        self.event = event
        self.player = player
        self.pyxel = pyxel
        self.hold = 2
        self.repeat = 2

    def check_key_pressed(self):
        if self.pyxel.btnp(self.pyxel.KEY_Q):
            self.event.event_quit()

        if self.pyxel.btnp(self.pyxel.KEY_LEFT, hold=self.hold, repeat=self.repeat):
            self.event.event_player_left()

        if self.pyxel.btnp(self.pyxel.KEY_RIGHT, hold=self.hold, repeat=self.repeat):
            self.event.event_player_right()

        if self.pyxel.btnp(self.pyxel.KEY_DOWN, hold=self.hold, repeat=self.repeat):
            self.event.event_player_down()

        if self.pyxel.btnp(self.pyxel.KEY_UP, hold=self.hold, repeat=self.repeat):
            self.event.event_player_up()
