from manim import *

class SummationAnimation(Scene):
	def construct(self):
		text = Text("How to write a")
		text2 = Text("Summmation")
		text3 = Text("in code")

		math1 = MathTex(r"\sum")
		math2 = MathTex(r'\sum_{n=0}^{4}n')
		text4 = Text("captial sigma")
		# self.add(math2)

		listing1 = Code(
						"hellosumcpp.cpp",
						tab_width=4,
						background_stroke_width=1,
						background_stroke_color=WHITE,
						insert_line_no=True,
						style=Code.styles_list[15],
						background="window",
						language="cpp",
					)
		# self.add(listing1)

