from manim import  *

class CirclesWithArrow(ThreeDScene):
	"""dirclesring for ClassWithArrow"""
	def construct(self):
		axes = ThreeDAxes()
		numberplane = NumberPlane()
		arrow1 = Arrow(start=[0,0,0],end=[0,0,1],buff=0,color=GOLD)
		arrow2 = Arrow(start=[2,0,0],end=[2,0,1],buff=0,color=RED)
		circle = Circle(radius=2,color=BLUE)
		dot = Sphere(center=(0, 0, 0), radius=.1, resolution=(15, 15)).set_color(WHITE)
		dot_1 = dot.copy().shift(RIGHT*2)


		self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
		text3d = Text("This is a 3D text")
		self.add_fixed_in_frame_mobjects(text3d)
		text3d.to_corner(UL)
		self.play(Write(axes))
		self.play(Create(numberplane))
		# self.add(arrow1)
		self.play(GrowFromCenter(circle))
		self.play(FadeIn(dot_1))
		self.add(arrow2)
		self.play(MoveAlongPath(VGroup(dot_1,arrow2.next_to(dot_1,0)),circle), run_time=2, rate_func=linear)
		self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES)
		self.wait()
		self.play(MoveAlongPath(VGroup(dot_1,arrow2.next_to(dot_1,0)),circle), run_time=2, rate_func=linear)
		self.move_camera(phi=0 * DEGREES, theta=90 * DEGREES)
		self.wait()
		self.play(MoveAlongPath(VGroup(dot_1,arrow2.next_to(dot_1,0)),circle), run_time=2, rate_func=linear)
		self.wait()


