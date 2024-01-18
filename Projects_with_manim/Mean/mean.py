from manim import *

class MeanAnimation(Scene):
    def construct(self):
        text = Text("Mean").shift(UP * 3)
        math0 = Text("In Math").shift(UP * 1 + LEFT *2.5)
        math1 = MathTex("::
