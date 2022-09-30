from manim import * 

class entropie(Scene):
    def construct(self):
        text = Text("entropie").scale(2)
        text2 = Text("neemt toe").shift(DOWN).scale(2)
        text3 = Text("neemt altijd toe").shift(DOWN).scale(2)
        self.play(Write(text))
        self.wait()
        self.play(Write(text2),text.animate.shift(UP))
        self.play(TransformMatchingShapes(text2,text3))
        