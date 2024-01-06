from manim import *

class NextToUpdater(Scene):
	def construct(self):
		def dot_position(mobject):
			mobject.set_value(dot.get_center()[0])
			mobject.next_to(dot)

		dot = Dot(RIGHT*3)
		circle = Circle(radius=3)
		label = DecimalNumber()
		label.add_updater(dot_position)
		self.add(dot, label)

		# self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))
		# self.play(dot.animate.rotate(180*DEGREES,[0,0,1]),run_time=TAU,rate_func=linear)
		self.play(MoveAlongPath(dot,circle),run_time=TAU,rate_func=linear)

class DtUpdater(Scene):
	def construct(self):
		sq = Square()

		#Let the line rotate 90° per second
		sq.add_updater(lambda mobject, dt: mobject.rotate(dt*90*DEGREES))
		self.add(sq)
		self.wait(2)

