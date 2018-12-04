import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="TsuboMan")
        pyxel.load("assets/hoge.pyxel")

        self.y = 100

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_SPACE):
            print("test")

    def draw(self):
        print(self.y)
        pyxel.text(0, 0, "abcedfg", 2)
        pyxel.blt(0, self.y, 0, 0, 0, 16, 16, 0)




App()

# blt(x, y, img, u, v, w, h, [colkey])
# イメージバンクimg(0-2) の (u, v) からサイズ (w, h) の領域を
# (x, y) にコピーする。w、hそれぞれに負の値を設定すると水平、垂直方向に反転する。colkeyに色を指定すると透明色として扱われる