from manim import *

class einde(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GREY
        tex1 = Text("Big rip").shift(UP*2+LEFT*4.5)
        tex2 = Text("Big bounce").shift(UP*2)
        tex3 = Text("Big freeze").shift(UP*2+RIGHT*4.5)

        self.play(Write(tex1))
        self.play(Write(tex2))
        self.play(Write(tex3))