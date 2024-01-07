from manim import * 

class ArrowPrecession(ThreeDScene):
	"""docstring for ArrowPrecession"""
	def construct(self):
		axes = ThreeDAxes()
		arrow1 = Arrow3D(start=[0,0,0],end=[0,0,1],buff=0,color=GOLD)
		arrow2 = Arrow3D(start=[2,0,0],end=[2,0,1],buff=0,color=RED)
		circle = Circle(radius=2,color=BLUE)
		# dot = Sphere(center=(0, 0, 0), radius=.1, resolution=(15, 15)).set_color(WHITE)
		# dot_1 = dot.copy().shift(RIGHT*2)

		self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
		self.play(Write(axes))
		# self.add(arrow1)
		self.play(GrowFromCenter(circle))
		# self.play(FadeIn(dot_1))
		self.play(Transform(arrow1,arrow2))
		self.play(MoveAlongPath(arrow1,circle), run_time=2, rate_func=linear)
		# self.play(MoveAlongPath(VGroup(dot_1,arrow2.next_to(dot_1,0)),circle), run_time=2, rate_func=linear)
		self.wait()
