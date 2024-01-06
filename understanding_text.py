from manim import * 

class UnderstandingText(Scene):
	def construct(self):
		tex1 = MathTex('a^2 + b^2 = c^2')
		tex2 = MathTex('{{ a }} + {{ b }} = {{ c }}').next_to(tex1,DOWN)
		deg = str(Integer(90).get_value())
		tex = MathTex(f'{deg}^\circ').next_to(tex2,DOWN)

		self.add(tex1,tex2,tex)
		# self.add(deg)