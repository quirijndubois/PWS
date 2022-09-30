from re import S
from tracemalloc import start
from manim import *
import numpy as np

class warp(Scene):
    def construct(self):
        pl = NumberPlane()
        self.play(Write(pl))
        sinesize = 10
        self.play(
		    *[ApplyPointwiseFunction(lambda point: 
            [
            point[0]+np.sin((point[1]-1.3)*sinesize)/20,
            point[1]+np.cos((point[0]+3)*sinesize)/20,
            0
            ]
            ,mob) for mob in self.mobjects]	
		)
        self.play(
		    *[ApplyPointwiseFunction(lambda point: 
            [
            point[0]+np.sin((point[0]-1.3)*sinesize)/20,
            point[1]+np.cos((point[1]+3)*sinesize)/20,
            0
            ]
            ,mob) for mob in self.mobjects]	
		)
        self.wait(3)