from manim import *
from manim.opengl import *

class OpenGLShow(Scene):
    def construct(self):
        circ = Circle()
        square = Square()
        self.add(circ, square)
        self.play(
            self.camera.animate.set_euler_angles(
                theta=-10*DEGREES,
                phi=50*DEGREES
                )
            )
        # self.play
        self.interactive_embed()