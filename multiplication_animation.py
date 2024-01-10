from manim import *

class MultiplicationAnimation(Scene):
	def construct(self):
		text2 = Text("Multiplication").shift(UP*3)

		math0 = Text("In Math:").shift(UP*1+LEFT*2.5)
		math2 = MathTex(r'\prod_{n=1}^{5}n').next_to(math0, DOWN)
		# text4 = Text("captial sigma").next_to(math2,DOWN)
		vg1 = VGroup(math0,math2)
		# self.add(math2)

		text3 = Text("In Code:").shift(UP*1+RIGHT*2.5)
		coded = """#in python
n = 1
for x in range(1,6):
	n = n * x"""
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
		# text = Text("How to write a")
		# text2 = Text("Product")
		# text3 = Text("in code")

		# math1 = MathTex(r"\prod")
		# math2 = MathTex(r'\prod_{n=1}^{4}2n')
		# text4 = Text("captial PI")
		# listing2 = Code(
		# 				"helloprodcpp.cpp",
		# 				tab_width=4,
		# 				background_stroke_width=1,
		# 				background_stroke_color=WHITE,
		# 				insert_line_no=True,
		# 				style=Code.styles_list[15],
		# 				background="window",
		# 				language="cpp",
		# 			)
		# self.add(listing2)

		# text = Text("How to write a")
		# math1 = MathTex(r"\sum")
		
