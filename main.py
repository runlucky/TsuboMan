import os
import inspect
import pyxel
import guy

class App:

    def __init__(self):
        pyxel.init(160, 120, caption="TsuboMan")

        self.y = 100
        self.vy = 0.0
        self.x = 0

        print(App.gravity)
        pyxel.load(os.path.dirname(os.path.abspath(__file__)) + "/assets/hoge.pyxel")
        pyxel.run(self.update, self.draw)

    gravity = 0.3

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.vy = -5

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1

        if pyxel.btn(pyxel.KEY_LEFT):
            self.x += -1


        self.y += self.vy
        self.vy += App.gravity
        self.vy = max(self.vy, -5)

        self.y = min(self.y, 100)


    def draw(self):
        pyxel.cls(0)
        pyxel.text(0, 0, "abcedfg", 2)
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)




App()

# blt(x, y, img, u, v, w, h, [colkey])
# イメージバンクimg(0-2) の (u, v) からサイズ (w, h) の領域を
# (x, y) にコピーする。w、hそれぞれに負の値を設定すると水平、垂直方向に反転する。colkeyに色を指定すると透明色として扱われる