from re import S
from manim import *

def hoofdstuknaam(naam):
    return Text(naam,t2c={"tijd": BLUE, "!": RED,"?": ORANGE}).scale(40/len(naam))

def quotefunc(naam):
    return Text(naam,color=GREY,t2c={"''": ORANGE, "!": RED,"?": ORANGE}).scale(40/len(naam)).shift(DOWN)

class hoofdstukken(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GREY
        text = hoofdstuknaam(input("text: "))
        quote = quotefunc(input("quote; "))
        self.play(Write(text),run_time=2)
        self.play(text.animate.shift(UP),FadeIn(quote))
        self.wait(3)

class quoteonly(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GREY
        text = hoofdstuknaam(input("text: "))
        auteur = hoofdstuknaam(input("auteur: ")).shift(DOWN)
        self.play(Write(text),run_time=2)
        self.play(Write(auteur))
        self.wait(3)
