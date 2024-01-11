from manim import *

class UnderstandingAngle(Scene):
	"""docstring for UnderstandingAngle"""
	def construct(self):
		line =  [
					Line(LEFT + (1/3) * UP, RIGHT + (1/3) * DOWN),
					Line(DOWN + (1/3) * RIGHT, UP + (1/3) * LEFT),
					Line(LEFT,RIGHT),
					Line(LEFT,RIGHT).rotate(110*DEGREES,about_point=LEFT)
				]
		a = [
				Angle(line[0],line[1],color=BLUE),
				Angle(line[0],line[1],radius=1,color=PURPLE),
				Angle(line[0],line[1],radius=0.4,color=WHITE, quadrant=(1,-1), dot=True, other_angle=False),
				Angle(line[0],line[1],radius=0.5, quadrant=(-1,1), stroke_width=8, dot=True, dot_color=YELLOW, dot_radius=0.04, other_angle=False),
				Angle(line[0],line[1], radius=0.7, quadrant=(-1,-1), color=RED, dot=True, dot_color=GREEN, dot_radius=0.08)
			]
		self.play(Write(VGroup(line[0],line[1],a[2],a[3],a[4])))
		# self.play(Transform(a[0],a[1]))
		self.wait()
