
from manim import *
import numpy as np

class lorentz(Scene):
    def construct(self):
        gamma = MathTex(r"\gamma = \frac{1}{\sqrt{1-\frac{v^2}{c^2}}}").scale(2)
        dilation = MathTex(r"t' = \gamma (t-\frac{vx}{c^2})").scale(2)
        ax = Axes(x_range=[0,1,0.1],y_range=[0,10,1],axis_config={"include_numbers": True}).scale(0.6).shift(RIGHT*2.5)
        graph = ax.plot(lambda v: 1/np.sqrt(1-(v**2)),x_range=[0,0.995])
        label_v  = ax.get_x_axis_label(Tex("$v/c$"),edge=RIGHT,direction=RIGHT,buff=0.3)
        label_g  = ax.get_y_axis_label(Tex("$\gamma$"),edge=UP,direction=UP,buff=0.3)

        self.play(Write(gamma))
        self.wait(1)
        self.play(gamma.animate.shift(LEFT*4.4+UP*1.5).scale(0.6))
        self.play(Write(dilation))
        self.wait(1)
        self.play(dilation.animate.shift(LEFT*4.4+DOWN*1.5).scale(0.6))
        group = VGroup(gamma,dilation)
        self.play(Write(ax),Write(label_v),Write(label_g))
        self.play(Create(graph))
        graphgroup = VGroup(graph,ax,label_g,label_v)
        self.wait(5)
        self.play(FadeOut(group),graphgroup.animate.shift(LEFT*2.5).scale(1.5))
        self.wait(2)