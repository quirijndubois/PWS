from re import S
from manim import * 

class donen(Scene):
    def construct(self):
        path = "/Users/quirijndubois/Documents/pws/code/donkereEnergie/"
        self.camera.background_color = DARKER_GREY

        pic = SVGMobject(path+"energy.svg",color=YELLOW).shift(0).scale(2)
        pic2 = SVGMobject(path+"energy.svg",color=BLACK).shift(0).scale(2)
        self.play(Write(pic))
        self.wait()
        self.play(Transform(pic,pic2))
        self.wait(3)

class seesaw(Scene):
    def construct(self):
        path = "/Users/quirijndubois/Documents/pws/code/donkereEnergie/"
        self.camera.background_color = DARKER_GREY
        pic = SVGMobject(path+"energy.svg",color=BLACK).shift(LEFT*3+UP).scale(1)
        pic2 = SVGMobject(path+"weight.svg",color=BLACK).shift(RIGHT*3+UP).scale(1)
        circle = Circle(radius=0.7).shift(DOWN*0.7)
        line = Arrow(max_tip_length_to_length_ratio=0).scale(6)

        self.play(Create(circle),Create(line))
        self.wait()
        self.play(Write(pic),Write(pic2))
        group = VGroup(pic,pic2,line)
        self.play(group.animate.rotate(0.1))
        self.play(group.animate.rotate(-0.2))
        self.play(group.animate.rotate(0.2))
        self.play(group.animate.rotate(-0.2))
        self.play(group.animate.rotate(0.2))
        self.play(group.animate.rotate(-0.1))
        self.wait(3)

