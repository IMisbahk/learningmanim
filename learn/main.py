from manim import *

class Concircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(RED, opacity=0.5)
        circle.set_stroke(color=WHITE, width=4)  

        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.rotate(PI/4)

        self.play(Create(square))
        self.play(Transform
                  (
                      square, circle
                  ))
        

    