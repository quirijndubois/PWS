from manim import * 

class interview(Scene):
    def construct(self):
        text = Text(input("input: ")).scale(0.7).shift(DOWN*2.5+LEFT*1.4)
        self.play(Write(text))
        self.wait(3)
        self.play(Unwrite(text))