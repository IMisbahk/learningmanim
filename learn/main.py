from manim import *
import numpy as np

class lorentz(ThreeDScene):
    def lorentz_deriv(self, pos, sigma=10, rho=28, beta=8/3):
        """lorentz functions"""
        x, y, z = pos
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        return np.array([dx, dy, dz])

    def generate_lorentz_trajectory(self, dt=0.01, steps=5000):
        """euler method"""
        trajectory = []
        pos = np.array([1.0, 1.0, 1.0])  
        
        for _ in range(steps):
            trajectory.append(pos.copy())
            pos += self.lorentz_deriv(pos) * dt 
        
        return np.array(trajectory)

    def construct(self):
        self.add(ThreeDAxes())
        
        points = self.generate_lorentz_trajectory()
        
        
        scaled_points = [np.array([x, y, z-2]) * 0.1 for x, y, z in points]

        self.move_camera(phi=75 * DEGREES, theta=40 * DEGREES)
        curve = VMobject()
        curve.set_points_as_corners(scaled_points)
        curve.set_stroke(color=BLUE, width=2)
        
        self.play(Create(curve, run_time=8, rate_func=linear))
        
        self.wait(2)
