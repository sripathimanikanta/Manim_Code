from manim import *

class VectorModel(Scene):
	"""docstring for ClassName"""
	def construct(self):
		# text1 = Text("Hello It's about Vector Model")
		axes = Axes(
			x_range=[-10,10,1],
			y_range=[-3,3,1],
			x_length=10,
			axis_config={"color": GREEN},
			x_axis_config={
				"numbers_to_include": np.arange(-10,10.01,2),
				"numbers_with_elongated_ticks": np.arange(-10,10.01,2)
			},
			tips=False,
			)
		circle = Circle(radius=2,color=BLUE)
		dot = Dot()
		dot2 = dot.copy().shift(RIGHT*2)

		self.play(Write(axes))
		self.add(dot)
		self.play(GrowFromCenter(circle))
		self.play(Transform(dot,dot2))
		self.play(MoveAlongPath(dot,circle),run_time=2, rate_func=linear)
		# self.remove(dot)
		self.wait()