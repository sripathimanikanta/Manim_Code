from manim import *

class Circles3D(ThreeDScene):
	"""docstring for Circles3D"""
	def construct(self):
		axes = ThreeDAxes()
		circle = Circle(radius=2,color=BLUE)
		circle2 = Circle(radius=3,color=RED).shift([0,0,1])
		circle3 = Circle(radius=4,color=GREEN).shift([0,0,2])
		dot = Sphere(center=(0, 0, 0), radius=.1, resolution=(15, 15)).set_color(WHITE)
		dot2 = Sphere(center=(0, 0, 0), radius=.1, resolution=(15, 15)).set_color(GOLD)
		dot3 = Sphere(center=(0, 0, 0), radius=.1, resolution=(15, 15)).set_color(PURPLE)
		dot_1 = dot.copy().shift(RIGHT*2)
		dot2_1 = dot2.copy().shift([3,0,1])
		dot3_1 = dot3.copy().shift([4,0,2])
		dot2.shift([0,0,1])
		dot3.shift([0,0,2])
		self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
		text3d = Text("This is a 3D text")
		self.add_fixed_in_frame_mobjects(text3d)
		text3d.to_corner(UL)
		self.play(Write(axes))
		# self.add(VGroup(dot_1,dot2_1,dot3_1))
		# self.add(VGroup(circle,circle2,circle3))

		#first circle:
		self.play(GrowFromCenter(circle))
		self.play(FadeIn(dot))
		self.play(Transform(dot,dot_1))
		self.play(MoveAlongPath(dot,circle), run_time=2, rate_func=linear)

		#second Circle:
		self.play(GrowFromCenter(circle2))
		self.play(FadeIn(dot2))
		self.play(Transform(dot2,dot2_1))
		self.play(MoveAlongPath(dot2,circle2), run_time=3, rate_func=linear)

		#third Circle:
		self.play(GrowFromCenter(circle3))
		self.play(FadeIn(dot3))
		self.play(Transform(dot3,dot3_1))
		self.play(MoveAlongPath(dot3,circle3), run_time=4, rate_func=linear)

		self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES)

		self.wait()
