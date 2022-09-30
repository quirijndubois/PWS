from ctypes.wintypes import DWORD
from re import S
from manim import *

class intro(Scene):
    def construct(self):
        path = "/Users/quirijndubois/Documents/pws/code/intro/"
        imgscale = 2
        pic1 = SVGMobject(path+"sundial.svg",color=YELLOW).shift(UP*1+LEFT*3.7).scale(imgscale)
        pic2 = SVGMobject(path+"eclipse.svg").shift(UP*1+RIGHT*3.7).scale(imgscale)

        self.play(Write(pic1))
        self.wait()
        self.play(Write(pic2))
        self.wait(3)
        self.play(Unwrite(pic1))
        self.wait()
        self.play(Unwrite(pic2))

class wat(Scene):
    def construct(self):
        self.play(Write(Text("Wat is tijd?").scale(3)))
        self.wait(1)
        