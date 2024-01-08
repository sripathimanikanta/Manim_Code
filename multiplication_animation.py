class MultiplicationAnimation(Scene):
	def construct(self):
		text = Text("How to write a")
		text2 = Text("Product")
		text3 = Text("in code")

		math1 = MathTex(r"\prod")
		math2 = MathTex(r'\prod_{n=1}^{4}2n')
		text4 = Text("captial PI")
		listing2 = Code(
						"helloprodcpp.cpp",
						tab_width=4,
						background_stroke_width=1,
						background_stroke_color=WHITE,
						insert_line_no=True,
						style=Code.styles_list[15],
						background="window",
						language="cpp",
					)
		self.add(listing2)