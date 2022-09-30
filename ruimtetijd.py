from manim import *
import time
import numpy as np

class ruimtetijd(MovingCameraScene):
    def construct(self):
        self.camera.background_color = DARK_GRAY
        t0 = time.time()
        c = 5
        AS = ValueTracker(0)
        dir = ValueTracker(0)
        vec_op = ValueTracker(0)
        size = 400
        res = 1.5
        deltatime = 1/60

        plane = NumberPlane(
            x_range=[0,size],
            y_range=[0,size],
            x_length=size*(1/res),
            y_length=size*(1/res),
            # background_line_style={"stroke_opacity": 0.4},
            background_line_style=dict(stroke_color = LIGHT_GREY),
            )
        axes = always_redraw(lambda: Axes(
            x_range=[0,12*res,1],
            y_range=[0,6*res,1]
            ).move_to(self.camera.frame_center).shift(LEFT/13+DOWN/10)
            )
        y_label = always_redraw(lambda: axes.get_y_axis_label(
            Tex("positie").rotate(90 * DEGREES),
            buff=0.3,
        ).move_to(self.camera.frame_center).shift(LEFT*6.5)
        )
        x_label = always_redraw(lambda: axes.get_x_axis_label(
            Tex("tijd"),
            edge=DOWN,
            direction=DOWN,
            buff=0.3,
        ).move_to(self.camera.frame_center).shift(DOWN*3.5)
        )
        ax = VGroup(axes,y_label,x_label)

        dot = Dot(color=BLUE).scale(4)
        dot.add_updater(
            lambda mobject: 
            mobject.shift(
                RIGHT*np.cos(dir.get_value())*c*deltatime*AS.get_value()+UP*np.sin(dir.get_value())*c*deltatime*AS.get_value())
        )
        self.add(self.camera.frame)
        self.camera.frame.add_updater(
            lambda mob: 
            mob.move_to(dot.get_center())
        )

        velocity_mag = ValueTracker(0)
        velocity_vector = always_redraw(lambda: Line(
            start=dot.get_center(),
            end=(dot.get_center()+RIGHT*np.cos(dir.get_value())*velocity_mag.get_value()+UP*np.sin(dir.get_value())*velocity_mag.get_value()),
            color=RED
            ).add_tip()
            )
        velocity_vector_label = always_redraw(lambda: Tex("$c$").next_to(velocity_vector))
        velocity_x = always_redraw(lambda: Line(
            start=dot.get_center(),
            end=(dot.get_center()+UP*np.sin(dir.get_value())*velocity_mag.get_value()),
            color=BLUE,
            stroke_opacity = vec_op.get_value(),
            ).add_tip(tip_length=vec_op.get_value()/3, tip_width = vec_op.get_value()/3)
            )
        velocity_x_label = always_redraw(lambda: Tex("$v$").next_to(velocity_x))
        velocity_t = always_redraw(lambda: Line(
            start=dot.get_center(),
            end=(dot.get_center()+RIGHT*np.cos(dir.get_value())*velocity_mag.get_value()),
            color=GREEN,
            stroke_opacity = vec_op.get_value(),
            ).add_tip(tip_length=vec_op.get_value()/3, tip_width = vec_op.get_value()/3)
            )
        velocity_t_label = always_redraw(lambda: Tex("$t$").next_to(velocity_t))
        


        raket = VGroup(dot)
        self.add_foreground_mobjects(raket,velocity_vector,velocity_vector_label,velocity_t,velocity_x)
        self.play(FadeIn(plane))
        self.play(AS.animate.set_value(1),velocity_mag.animate.set_value(2.2))
        self.play(FadeIn(ax),run_time=0.1)
        self.play(dir.animate.set_value(0.0001),run_time=5)
        self.add(velocity_t_label,velocity_x_label)
        self.play(dir.animate.set_value(np.pi/3),vec_op.animate.set_value(1),run_time=5)
        self.play(dir.animate.set_value(-np.pi/4),run_time=3)
        self.remove(velocity_t_label,velocity_x_label)
        self.play(dir.animate.set_value(0),vec_op.animate.set_value(0),run_time=1)
        self.play(dir.animate.set_value(0.0001),run_time=3)