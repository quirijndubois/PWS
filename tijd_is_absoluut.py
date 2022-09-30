from manim import *
import numpy as np
import random

class time(MovingCameraScene):
    def construct(self):
        time = ValueTracker()
        t = Tex("$t$").scale(3)
        # timestring = str(np.round(time.get_value(),2)) + "0"*(4-len(str(np.round(time.get_value(),2))))
        timer = always_redraw(lambda: Tex(
            "$t$ = "+str(np.round(time.get_value(),1))+"123456789"[random.randint(0,8)]
            ).scale(3))
            
        # timer = always_redraw(lambda: Tex("$t$ = "+str(np.round(time.get_value(),2))))
        self.add(t)
        self.play(Transform(t,timer))
        self.remove(t)
        self.add(timer)
        self.play(time.animate.set_value(10),rate_func=linear,run_time=10)

class absoluut(Scene):
    def construct(self):
        offset = 1.5
        scalefac = 0.8
        path = "/Users/quirijndubois/Documents/pws/code/absoluut/"
        pic1 = SVGMobject(path+"earth.svg",color=BLUE).shift((UP+RIGHT)*offset).scale(scalefac)
        pic2 = SVGMobject(path+"milky.svg").shift((DOWN+LEFT)*offset).scale(scalefac)
        pic3 = SVGMobject(path+"moon.svg",color=LIGHT_GRAY).shift((DOWN+RIGHT)*offset).scale(scalefac)
        pic4 = SVGMobject(path+"rocket.svg",color=WHITE).shift((UP+LEFT)*offset).scale(scalefac)
        self.play(Write(pic1))
        self.play(Write(pic2))
        self.play(Write(pic3))
        self.play(Write(pic4))
        