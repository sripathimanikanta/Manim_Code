from manim import *

class mult_animation_ins(Scene):
	def construct(self):
		text = Text("Summation")
		self.play(Write(text))
		self.play(
