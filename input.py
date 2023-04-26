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

        elif self.pyxel.btnp(self.pyxel.KEY_LEFT, hold=self.hold, repeat=self.repeat):
            self.event.event_player_left()

        elif self.pyxel.btnp(self.pyxel.KEY_RIGHT, hold=self.hold, repeat=self.repeat):
            self.event.event_player_right()

        elif self.pyxel.btnp(self.pyxel.KEY_DOWN, hold=self.hold, repeat=self.repeat):
            self.event.event_player_down()

        elif self.pyxel.btnp(self.pyxel.KEY_UP, hold=self.hold, repeat=self.repeat):
            self.event.event_player_up()
        
        elif self.pyxel.btnp(self.pyxel.KEY_CTRL, hold=self.hold, repeat=self.repeat):
            self.event.event_player_attacking()

        elif self.pyxel.btnp(self.pyxel.KEY_SPACE, hold=self.hold, repeat=self.repeat):
            self.event.event_player_shotting()
        
        else:
            self.event.event_player_stopped()
