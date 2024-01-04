from manim import *

# ValueTracker
# add_updater
# alpha_updaters
# https://docs.manim.community/en/stable/reference/manim.animation.updaters.html?highlight=mobject%20updaters#module-manim.animation.updaters
def ValueProvider(no_circle,radius,buff=0):
	length_dia = radius*2
	return val
class RateFunctionInManim(Scene):
	# i want a function that can give me 
	# no. of independent items
	def construct(self):
		# redundency:
		# circle1 = Circle(radius=1,color=RED)
		# circle1_d = Circle(radius=1,color=RED)

		circle1 = [Circle(radius=1,color=RED) for _ in range(0,2)]
		text1 = [Text("smooth") for _ in range(0,2)]
		circle2 = [Circle(radius=1,color=BLUE) for _ in range(0,2)]
		text2 = [Text("linear") for _ in range(0,2)]
		circle3 = [Circle(radius=1,color=GREEN) for _ in range(0,2)]
		text3 = [Text("exponential_decay") for _ in range(0,2)]
		circle4 = [Circle(radius=1,color=WHITE) for _ in range(0,2)]
		text4 = [Text("there_and_back") for _ in range(0,2)]
		vdist = 1.5
		sc = 0.42

		self.play(
			# NOT WOKRING
			# Write(circle1.animate(rate_func=smooth)), 
			# GrowFromCenter(circle1_d.animate(rate_func=linear)),
			# Write(circle1.animate.shift(LEFT*3.75+UP*1.25)),

			#working:
			Write(circle1[0].shift(LEFT*3.75+UP*vdist),rate_func=smooth),
			Write(text1[0].next_to(circle1[0],DOWN*0.01).set_color(RED).scale(sc)),
			Write(circle2[0].shift(LEFT*1.25+UP*vdist),rate_func=linear),
			Write(text2[0].next_to(circle2[0],DOWN*0.01).set_color(BLUE).scale(sc)),
			Write(circle3[0].shift(RIGHT*1.25+UP*vdist),rate_func=exponential_decay),
			Write(text3[0].next_to(circle3[0],DOWN*0.01).set_color(GREEN).scale(sc)),
			Write(circle4[0].shift(RIGHT*3.75+UP*vdist),rate_func=there_and_back),
			Write(text4[0].next_to(circle4[0],DOWN*0.01).set_color(WHITE).scale(sc)),
			# circle1[0].animate.shift(LEFT*3.75+UP*1.25),

			GrowFromCenter(circle1[1].shift(LEFT*3.75+DOWN*vdist),rate_func=smooth),
			GrowFromCenter(text1[1].next_to(circle1[1],DOWN*0.01).set_color(RED).scale(sc)),
			GrowFromCenter(circle2[1].shift(LEFT*1.25+DOWN*vdist),rate_func=linear),
			GrowFromCenter(text2[1].next_to(circle2[1],DOWN*0.01).set_color(BLUE).scale(sc)),
			GrowFromCenter(circle3[1].shift(RIGHT*1.25+DOWN*vdist),rate_func=exponential_decay),
			GrowFromCenter(text3[1].next_to(circle3[1],DOWN*0.01).set_color(GREEN).scale(sc)),
			GrowFromCenter(circle4[1].shift(RIGHT*3.75+DOWN*vdist),rate_func=there_and_back),
			GrowFromCenter(text4[1].next_to(circle4[1],DOWN*0.01).set_color(WHITE).scale(sc)),
			#experiment
			# circle1.animate.shift(LEFT*3.75+UP*1.25),
			run_time=6
			)
		# self.play(
		# 	# GrowFromCenter(circle1[1],rate_func=there_and_back),
		# 	# circle1[1].animate.shift(LEFT*3.75+DOWN*1.25),
		# 	GrowFromCenter(circle1[1].shift(LEFT*3.75+DOWN*1.25),rate_func=smooth),
		# 	GrowFromCenter(circle2[1].shift(LEFT*1.25+DOWN*1.25),rate_func=linear),
		# 	GrowFromCenter(circle3[1].shift(RIGHT*1.25+DOWN*1.25),rate_func=exponential_decay),
		# 	GrowFromCenter(circle4[1].shift(RIGHT*3.75+DOWN*1.25),rate_func=there_and_back)
		# 	# rate_func=smooth
		# 	)

		# self.play(
		# 	# Write(circle2[0].shift(LEFT*1.25+UP*1.25)),
		# 	GrowFromCenter(circle2[1].shift(LEFT*1.25+DOWN*1.25),rate_func=linear),
		# 	# rate_func=linear
		# 	)

		# self.play(
		# 	GrowFromCenter(circle3[1].shift(RIGHT*1.25+DOWN*1.25),rate_func=exponential_decay),
		# 	# rate_func=exponential_decay
		# 	)

		# self.play(
		# 	GrowFromCenter(circle4[1].shift(RIGHT*3.75+DOWN*1.25),rate_func=there_and_back),
		# 	# rate_func=there_and_back
		# 	)