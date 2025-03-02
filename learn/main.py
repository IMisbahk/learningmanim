from manim import *

class SquareToCube(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)


        Axes = ThreeDAxes()
        self.add(Axes)
        square = Square(color=BLUE, fill_opacity=0.5)
        self.play(Create(square))
        self.wait(1)

        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=2)
        self.wait(1)

        cube = Cube(color=BLUE, fill_opacity=0.3)
        self.play(Transform(square, cube))

        self.play(
            cube.animate.scale(0.5),
            run_time=2
        )

        self.wait(2)
        ##ahash