from manim import *
# from text_mobject import remove_invisible_chars

class Codes(Scene):
	"""docstring for Codes"""
	def construct(self):
		ode = '''from manim import Scene, Square

class FadeInSquare(Scene):
	def construct(self):
		s = Square()
		self.play(FadeIn(s))
		self.play(s.animate.scale(2))
		self.wait()
'''
		listing = Code(
			code=ode,
			tab_width=4,
			background_stroke_width=1,
			background_stroke_color=WHITE,
			insert_line_no=True,
			style=Code.styles_list[15],
			background="window",
			language="Python",
			)
		print(listing.line_numbers)
		print(listing.code)
		listing.code.set_opacity(0.5)
		self.add(listing)
		animation = [
			# listing.code[0].animate.set_opacity(0),
			listing.code[0].animate.set_opacity(1),
			# listing.code[2].animate.set_opacity(0),
			listing.code[2].animate.set_opacity(1)
		]
		self.play(AnimationGroup(*animation, lag_ratio=0.5), run_time=2)
		# self.play(Transform(remove_invisible_chars(listing.code.chars[0:2]),
        #             remove_invisible_chars(listing.code.chars[3][0:3])))