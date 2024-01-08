from manim import * 

class ArrowPrecession(ThreeDScene):
	"""docstring for ArrowPrecession"""
	def construct(self):
		# dot = Sphere(center=(0, 0, 0), radius=.1, resolution=(15, 15)).set_color(WHITE)
		dot = Dot(point=[2,0,1],color=RED)
		axes = ThreeDAxes()
		arrow1 = Arrow3D(start=[0,0,0],end=[2,0,1],color=GOLD)
		# arrow2 = Arrow3D(start=[2,0,0],end=[2,0,1],buff=0,color=RED)
		circle = Circle(radius=2,color=BLUE).shift([0,0,1])
		# dot_1 = dot.copy().shift(RIGHT*2)

		self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
		self.play(Write(axes))
		self.play(GrowFromCenter(circle))
		self.add(arrow1)
		# self.add(arrow1)
		arrow1.add_updater(
				lambda x: x.become(Arrow3D(start=[0,0,0],end=dot.get_center(),color=YELLOW))
			)
		self.play(MoveAlongPath(dot,circle), run_time=2, rate_func=linear)
		self.wait()
		# self.play(FadeIn(dot_1))
		# self.play(Transform(arrow1,arrow2))
		# self.play(MoveAlongPath(VGroup(dot_1,arrow2.next_to(dot_1,0)),circle), run_time=2, rate_func=linear)
