from tracemalloc import start
from manim import *
import numpy as np
import random

class kanonskogel(MovingCameraScene):
    def construct(self):
        self.camera.background_color = BLUE
        g = -9.81
        vy = 15
        vx = 15
        x0 = 0.0

        a = 0.5 * g * (vx**(-2))
        b = vy / vx
        c = x0
        maxx = -b/a

        kanon = ImageMobject("konon.png").scale(0.15 ).shift(LEFT*5.7+DOWN*3.3  )
        k = ValueTracker(0)
        velocityMag = ValueTracker(1)


        ax = Axes(
            x_range=[0, vy*2, 1],
            y_range=[0, vy*2, 1],
        ).shift(UP*0.15+RIGHT)

        graph = ax.plot(lambda x: 0.5*g*((x/vx)**2)+vy*(x/vx)+x0 ,x_range=[0, maxx])
        dashed_graph = DashedVMobject(graph,num_dashes=100)

        dot = always_redraw(lambda: Dot(color=GREY,radius=0.2).move_to(
            ax.c2p(k.get_value(),graph.underlying_function(k.get_value())
            )))
        timer = always_redraw(lambda: MathTex("t = "+str(np.round(k.get_value()/maxx,2))).move_to(dot).shift(RIGHT/2+UP/3).scale(0.5))


        


        self.add(kanon)
        self.wait(1)
        self.play(Create(timer))
        self.add(dot)
        self.play(Create(dashed_graph),k.animate.set_value(maxx), run_time=2, rate_func=linear)
        self.add(dot)
        self.play(self.camera.frame.animate.shift(RIGHT*4).scale(1.5))
        self.wait(0.5)
        self.play(k.animate.set_value(maxx/2))
        self.play(self.camera.frame.animate.move_to(dot).scale(0.4))

        # ref_ax = Axes(x_range=[0, 10, 1],y_range=[0, 10, 1],color=RED).move_to(dot).scale(0.5)
        
        normalize = 10
        velocity_vector = always_redraw(lambda: Line(
            start=dot.get_center(),
            end=(dot.get_center()+RIGHT*(vx / normalize)*velocityMag.get_value()+UP*((g*(k.get_value() / vx) + vy) / (normalize * 2))*velocityMag.get_value()),
            color=RED
            ).add_tip()
            )
        gravity_vector = always_redraw(lambda: Line(
            start=dot.get_center(),
            end=(dot.get_center()+DOWN),
            color=BLUE_D
            ).add_tip()
            )


        self.play(Create(velocity_vector),Create(gravity_vector))
        self.play(k.animate.set_value(maxx/2+4))
        self.play(k.animate.set_value(maxx/2-4))
        self.play(k.animate.set_value(maxx/2))

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={
                'color' : WHITE,
                'stroke_width' : 2,
                'include_numbers' : False,
            }
        )
        x_formula = MathTex(r"x = v \cdot t").move_to(dot).scale(0.5).shift(DOWN*1.1+RIGHT*2)
        y_formula = MathTex(r"y = \frac{1}{2} g t^{2} + v_0 t + x_0").move_to(dot).scale(0.5).shift(UP*1+LEFT*1.5)
        x_formula_minus = MathTex(r"x = v \cdot (-t)").move_to(dot).scale(0.5).shift(DOWN*1.1+LEFT*1.6)
        y_formula_minus = MathTex(r"y = \frac{1}{2} g (-t)^{2} + v_0 (-t) + x_0").move_to(dot).scale(0.5).shift(UP*1+RIGHT*1)
        axes.move_to(dot).scale(0.5)

        self.play(Create(axes),Create(x_formula),Create(y_formula))
        self.wait(0.5)
        self.play(Rotate(axes, 180*DEGREES, axis=UP),velocityMag.animate.set_value(-1),Transform(x_formula,x_formula_minus),Transform(y_formula,y_formula_minus))

        self.wait(1)
        self.play(k.animate.set_value(maxx/2+6))
        self.play(k.animate.set_value(maxx/2+-6))
        self.play(k.animate.set_value(maxx/2))

        self.wait(2)

        self.play(Rotate(axes, 180*DEGREES, axis=UP),velocityMag.animate.set_value(1),
        Transform(x_formula,MathTex(r"x = v \cdot t").move_to(dot).scale(0.5).shift(DOWN*1.1+RIGHT*2)),
        Transform(y_formula,MathTex(r"y = \frac{1}{2} g t^{2} + v_0 t + x_0").move_to(dot).scale(0.5).shift(UP*1+LEFT*1.5))
        )

        self.wait(3)

class lucht(MovingCameraScene):
    def construct(self):
        nothing = ValueTracker(0)
        deltatime = 1/60
        space = 30
        self.camera.background_color = BLUE
        kogel = Dot(color=GREY).scale(10)
        c = 10
        radius = 0.8
        startspeed = 0.05

        luchtdeeltjes = VGroup()
        for i in range(5000):
            luchtdeeltjes += Dot(color=WHITE).shift(UP*(random.random()-0.5)*space+RIGHT*(random.random()-0.5)*2*space)
            luchtdeeltjes[i].dir = random.random()*2*np.pi
            luchtdeeltjes[i].speedmag = startspeed+(random.random()-0.5)*startspeed
            luchtdeeltjes[i].speedx = ValueTracker(np.sin(luchtdeeltjes[i].dir)*luchtdeeltjes[i].speedmag-0.1)
            luchtdeeltjes[i].speedy = ValueTracker(np.cos(luchtdeeltjes[i].dir)*luchtdeeltjes[i].speedmag)

            luchtdeeltjes[i].add_updater(
                lambda mobject: 
                mobject.shift(
                UP*mobject.speedy.get_value()+RIGHT*mobject.speedx.get_value()
                )
            )
            luchtdeeltjes[i].add_updater( 
                lambda mobject: 
                mobject.speedx.set_value(mobject.speedx.get_value()+mobject.get_center()[0]/np.linalg.norm(mobject.get_center())/100*c) if np.linalg.norm(mobject.get_center()) < radius else 0
                )
            luchtdeeltjes[i].add_updater( 
                lambda mobject: 
                mobject.speedy.set_value(mobject.speedy.get_value()+mobject.get_center()[1]/np.linalg.norm(mobject.get_center())/100*c) if np.linalg.norm(mobject.get_center()) < radius else 0
                )
            luchtdeeltjes[i].add_updater( 
                lambda mobject: 
                mobject.speedy.set_value(mobject.speedy.get_value()/np.linalg.norm([mobject.speedy.get_value(),mobject.speedx.get_value()])*startspeed)
                )
            luchtdeeltjes[i].add_updater( 
                lambda mobject: 
                mobject.speedx.set_value(mobject.speedx.get_value()/np.linalg.norm([mobject.speedy.get_value(),mobject.speedx.get_value()])*startspeed)
                )

        self.play(Write(kogel))
        self.play(Write(luchtdeeltjes))
        self.play(nothing.animate.set_value(1),run_time=5)

        