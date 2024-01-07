from manim import * 

class UnderstandingText(Scene):
	def construct(self):
		tex1 = MathTex('a^2 + b^2 = c^2')
		tex2 = MathTex(r'{{ a }} + {{ b }} = {{ c }}').next_to(tex1,DOWN)
		deg = str(Integer(90).get_value())
		tex = MathTex(f'{deg}^\circ').next_to(tex2,DOWN)

		# self.add(tex1,tex2,tex)
		# self.add(deg)

class QuadracticFormula(Scene):
	def construct(self):
		#testing:
		ab1 = MathTex(r"{{ ax^2 }}+{{ bx }}+{{ c }}={{ 0 }}")
		# ab2 = MathTex(r"ax^2+bx=-c")
		self.add(ab1[0],ab1[1],ab1[2],ab1[3],ab1[4],ab1[5],ab1[6])
		self.wait()
		# {{ ax^2 }} + {{ bx }} + {{ c }} = {{ 0 }}
		#     0      1    2     3    4    5    6

		self.remove(ab1[6])
		# {{ ax^2 }} + {{ bx }} + {{ c }} = 
		#     0      1    2     3    4    5

		self.play(
			#equals between c and 0 moving from 5 -> 3 th position
			ab1[5].animate.next_to(ab1[3],RIGHT*0),

			#PLUS moving from 3 -> 4 th position
			ab1[3].animate.become(MathTex(r"-").next_to(ab1[4],RIGHT*0)),

			#
			ab1[4].animate.next_to(ab1[5],RIGHT*0),
			)
		# {{ ax^2 }} + {{ bx }} = - {{ c }}
		#     0      1    2     3 4    5
		self.wait()

		# exp:1
		# ab1[0] = "x^2"
		# self.add(ab1[0])

		self.play(
			ab1[0].animate.become(MathTex(r'x^2')).next_to(ab1[0],RIGHT*0),
			ab1[2].animate.become(MathTex(r'{b \over a}x')).next_to(ab1[2],RIGHT*0),
			ab1[4].animate.become(MathTex(r'{c \over a}')).next_to(ab1[4],RIGHT*0)
			)

		# {{ ax^2 }} + {{ bx }} = - {{ c }}
		#     0      1    2     3 4    5
		#    x^2     + {b\over a}x=-{c\over a}

		# self.play(Transform(ab1,ab2))
		# (011011011)base2
		# 0123456789 -> 10
		# 01 -> 2
		# 01234567 -> 8
		# 0123456789ABCDEF -> 16
		1+1*(2^4)+0*(2^3)+1*(2^2)+1*(2^1)+0*(2^0)

class MatchingEquationParts(Scene):
	def construct(self):
		variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

		eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
		eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
		eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

		self.add(eq1)
		self.wait(0.5)
		self.play(TransformMatchingTex(Group(eq1, variables), eq2))
		self.wait(0.5)
		self.play(TransformMatchingTex(eq2, eq3))
		self.wait(0.5)