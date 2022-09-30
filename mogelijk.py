from manim import *

class mogelijk(Scene):
    def construct(self):
        path = "/Users/quirijndubois/Documents/pws/code/ruimtetijd/svg/"
        self.camera.background_color = DARKER_GREY
        scale = 0.9
        imgscale = 1.4
        lineheight = 3.5
        slant = -0.5
        width = 5
        text1 = Text("Speciale\n relativiteit").shift(UP*2+LEFT*width).scale(scale)
        pic1 = SVGMobject(path+"speed.svg",color=RED).shift(DOWN+LEFT*width).scale(imgscale)
        line1 = Line(start=LEFT*(width/2+slant)+UP*lineheight,end=LEFT*(width/2-slant)+DOWN*lineheight)
        text2 = Text("Ruimtetijd").shift(UP*2).scale(scale)
        pic2 = SVGMobject(path+"axis.svg",color=GREEN).shift(DOWN).scale(imgscale)
        line2 = Line(start=RIGHT*(width/2-slant)+UP*lineheight,end=RIGHT*(width/2+slant)+DOWN*lineheight)
        text3 = Text("Zwaartekracht").shift(UP*2+RIGHT*width).scale(scale)
        pic3 = SVGMobject(path+"gravity.svg",color=BLUE).shift(DOWN+RIGHT*width).scale(imgscale)



        self.play(Write(text1))
        self.play(Write(pic1))
        self.play(Write(line1))
        self.play(Write(text2))
        self.play(Write(pic2))
        self.play(Write(line2))
        self.play(Write(text3))
        self.play(Write(pic3))
        self.wait(2)