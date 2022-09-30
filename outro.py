from cgitb import text
from manim import *

class outro(MovingCameraScene):
    def construct(self):
        spacing = 2
        texts=[
            ["Door:","Quirijn du Bois, Levon Doeven, Philippe Rosingh"],
            ["Edit door:","Qurijn du Bois"],
            ["Animaties door:","Quirijn du Bois"],
            ["Met speciale dank aan:","George van Hal  en  Marcel Vonk"],
            ["Begeleider: ","Jan van der Maas"],
        ]
        self.camera.frame.shift(UP*3)
        for i in range(len(texts)):
            text1 = Text(texts[i][0]).shift(DOWN*i*spacing).scale(0.4)
            text2 = Text(texts[i][1]).shift(DOWN*i*spacing+DOWN/2).scale(0.6)
            self.play(Write(text1),Write(text2),self.camera.frame.animate.shift(DOWN*spacing),rate_func=linear,run_time=2)
        self.play(self.camera.frame.animate.shift(DOWN*spacing*4),rate_func=linear,run_time=8)

                