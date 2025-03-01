from manim import *

class Concircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(RED, opacity=0.5)
        circle.set_stroke(color=WHITE, width=4)  

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, direction=LEFT, buff=1)

        self.play(Create(circle))
        self.wait(0.2)
        self.play(Create(square))

        self.play(square.animate.shift(2*UP))
        self.play(circle.animate.shift(2*LEFT))