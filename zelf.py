from manim import *

class zelf(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GREY
        text = Text("Alle animaties in deze video zijn").scale(1)
        text2 = Text("origineel en zelf gemaakt",t2c={"origineel": BLUE, "zelf": BLUE}).shift(DOWN)
        self.play(Write(text))
        self.play(Write(text2))
        self.play(Unwrite(text2),Unwrite(text))
        self.wait(3)