class Event:
    def __init__(self, pyxel, player):
        self.player = player
        self.pyxel = pyxel

    def event_quit(self):
        self.pyxel.quit()

    def event_player_up(self):
        self.player.walk_up()

    def event_player_down(self):
        self.player.walk_down()

    def event_player_right(self):
        self.player.walk_right()

    def event_player_left(self):
        self.player.walk_left()
