from manim import *

class UnderstandingMathTex(Scene):
    def construct(self):
        midcal = MathTex(r" \frac { ( start +end) }{2} ")
        midcals  = midcal.tex_strings
        print(len(midcal))
        print(len(midcals))
        # self.play(Write(midcal[1]))
        self.play(Write(midcal[midcal.index_of_part_by_tex("end")]))
        self.wait(3)
