from manim import *

class SummationAnimation(Scene):
	def construct(self):
		# text = Text("How to write a")
		# math1 = MathTex(r"\sum")
		text2 = Text("Summation").shift(UP*3)

		math0 = Text("In Math:").shift(UP*1+LEFT*3)
		math2 = MathTex(r'\sum_{n=0}^{4}n').next_to(math0, DOWN)
		# text4 = Text("captial sigma").next_to(math2,DOWN)
		vg1 = VGroup(math0,math2)
		# self.add(math2)

		text3 = Text("In Code:").shift(UP*1+RIGHT*3)
		coded = """#in python
sums = 0;
for x in range(0,5):
	sums = sums + x"""
		listing1 = Code(
						code=coded,
						tab_width=4,
						background_stroke_width=1,
						background_stroke_color=WHITE,
						insert_line_no=True,
						style=Code.styles_list[15],
						background="window",
						language="Python",
					).next_to(text3, DOWN)
		vg2 = VGroup(text3,listing1)
		self.add(text2,vg1,vg2)
