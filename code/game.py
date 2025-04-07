from level import Level

class Game:
    def __init__(self, window):
        self.window = window
        self.level = Level(window)

    def run(self):
        self.level.run()