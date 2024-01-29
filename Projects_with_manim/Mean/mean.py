from manim import *

class MeanAnimation(Scene):
    def construct(self):
        text = Text("Mean").shift(UP * 3)
        math0 = Text("In Math:").shift(UP * 1 + LEFT * 3.5)
        math2 = MathTex(r'\chi = [1,1,2,3,4,5,6,7,7,6]').next_to(math0, DOWN*1.5)
        math1 = MathTex(r'\mu = \sum_{i=1}^{N}\frac{\chi_i}{N}').next_to(math2, DOWN*1.5)
        vg1 = VGroup(math0, math2, math1)
        
        #write here:
        text1 = Text("In Code:").shift(UP * 1 + RIGHT * 3.5)  
        coded = """x = [1,1,2,3,4,5,6,7,7,6]
total = 0
for y in x:
    total = total + y
mean = total/len(x)"""
        listingcode = Code(
            code=coded,
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[15],
            background="window",
            language="Python",
        ).next_to(text1, DOWN*1.5)
        vg2 = VGroup(text1,listingcode)
        self.add(text,vg1, vg2)

