from manim import *

class UnderstandingAnimate(Scene):
	def construct(self):
		# tex = Text("Understanding animate method")
		sq1 = Square()

		#it doesnt work properly:
		# self.play(sq.animate.shift(RIGHT), sq.animate.rotate(PI))
		# self.wait()

		#it worked: it is called chaining
		self.add(sq1)
		self.play(GrowFromCenter(sq1))
		# self.play(Create(sq1))
		self.play(sq1.animate.shift(LEFT).rotate(PI/2))
		# self.play(Uncreate(sq1))
		self.play(FadeOut(sq1))
		self.play(Write(Text("HELLO")))

class AnimateExample(Scene):
	def construct(self):
		s = Square()
		self.play(Create(s))
		self.play(s.animate.shift(RIGHT))
		self.play(s.animate.scale(2))
		self.play(s.animate.rotate(PI / 2))
		self.play(Uncreate(s))

class AnimateChainExample(Scene):
	def construct(self):
		s = Square()
		self.play(Create(s))
		self.play(s.animate.shift(RIGHT).scale(2).rotate(PI / 2))
		self.play(Uncreate(s))

class AnimateWithArgsExample(Scene):
	def construct(self):
		s = Square()
		c = Circle()

		VGroup(s, c).arrange(RIGHT, buff=2)
		self.add(s, c)

		self.play(
			s.animate(run_time=2).rotate(PI / 2),
			c.animate(rate_func=there_and_back).shift(RIGHT),
		)

"""``.animate``will interpolate the :class:`~.OpenGLMobject` between 
its points prior to ``.animate`` and its points after applying ``.animate`` to it. This may
 result in unexpected behavior when attempting to interpolate along paths,
 or rotations.
 If you want animations to consider the points between, consider using
 :class:`~.ValueTracker` with updaters instead."""
