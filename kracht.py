from manim import *

class kracht(Scene):
    def construct(self):
        dot1 = Dot().shift(LEFT*3).scale(10)
        dot2 = Dot().shift(RIGHT*3).scale(10)
        arrow1 = Arrow(start = dot1.get_center(),
         end = dot1.get_center()+(dot2.get_center()-dot1.get_center())/2,
         color=BLUE
         )
        arrow2 = Arrow(start = dot2.get_center(),
         end = dot2.get_center()+(dot1.get_center()-dot2.get_center())/2,
         color=RED
         )

        self.play(Write(dot1),Write(dot2))
        self.play(Write(arrow1),Write(arrow2))