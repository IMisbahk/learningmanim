from manim import *

class MorphingShapes(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=0.6)
        circle = Circle(color=GREEN, fill_opacity=0.6)
        star = Star(n=5, color=RED, fill_opacity=0.6)

        text = Text("Morphing Shapes").scale(0.7).shift(UP*2)

        
        self.play(Write(text))
        self.play(Create(square))
        self.wait(1)
        self.play(Transform(square, circle))
        self.wait(1)
        self.play(Transform(square, star))
        self.wait(1)

        self.play(FadeOut(square), FadeOut(text))
        self.wait()
