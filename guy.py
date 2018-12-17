import inspect, os
class Guy:
    def __init__(self):
        self.y = 100
        self.vy = 0.0

    gravity = 0.3

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.vy = -5

        self.y += self.vy
        self.vy += App.gravity
        self.vy = max(self.vy, -5)

        self.y = min(self.y, 100)


    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, "abcedfg", 2)
        pyxel.blt(0, self.y, 0, 0, 0, 16, 16, 0)

