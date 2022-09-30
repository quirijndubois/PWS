from manim import *

class relenkwa(Scene):
    def construct(self):
        text1 = Text("Relativiteit",color=BLUE).shift(UP)
        text2 = Text("en")
        text3 = Text("Kwantummechanica",color=RED).shift(DOWN)
        circle = Circle(radius=10)
        omkeerbaar = Text("omkeerbaar").shift(UP*10)
        self.add(circle)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        group = VGroup(text1,text2,text3)
        self.play(group.animate.scale(0.5),circle.animate.scale(0.2),omkeerbaar.animate.shift(DOWN*7))
        self.wait(3)