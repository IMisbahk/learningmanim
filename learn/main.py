from manim import *

class Concircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(GREEN, opacity=.3)
        circle.set_stroke(WHITE)
        self.play(Create(circle))
        