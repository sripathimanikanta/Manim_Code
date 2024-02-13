from manim import *

class BubbleSortAnime(Scene):
	"""docstring for BubbleSortAnime"""
	def construct(self):
		y= Square(side_length=1.0).move_to(LEFT*3+UP*3)
		y_num = Integer(12).move_to(y.get_center())
		valueLists = [Square(side_length=1.0) for x in range(0,5)]
		valueLists_nums = [20, 15, 29, 10, 14]
		valueLists_num = [Integer(x) for x in valueLists_nums]
		vg = VGroup()

		for x in range(0,5):
			if x == 0:
				z = valueLists[x].next_to(y, direction=RIGHT)
				z_vals = valueLists_num[x].move_to(z.get_center())
				vg = vg + VGroup(z,z_vals)
			else:
				z = valueLists[x].next_to(valueLists[x-1],direction=RIGHT)
				z_vals = valueLists_num[x].move_to(z.get_center())
				vg = vg + VGroup(z,z_vals)
		print(vg)
		boxes = VGroup(y, vg, y_num)


# 		coded = """def bubbleSortQE(arr):
# 	n=len(arr)
# 	for i in range(n-1):
# 		swapped = False
# 		for j in range(n-i-1):
# 			if arr[j] > arr[j+1]:
# 				a[j], a[j+1] = a[j+1], a[j]
# 			swapped = True

# 		if not swapped:
# 			break;
# """
# 		# circles = [Circle(radius=0.1,color=Y, fill_opacity=1).move_to(RIGHT*X) for X,Y in zip([0.4,0.8,1.2],['RED','BLUE', 'GREEN'])]
# 		# vc = VGroup()
# 		# for x in circles:
# 		# 	vc = vc + VGroup(x)
# 		# vc.next_to(boxes, DOWN+LEFT*0.1)
# 		codes = Code(code=coded, 
# 					language="Python",
# 					tab_width=4,
# 					style=Code.styles_list[13],
# 					background = "window",
# 					background_stroke_color=ManimColor('#FFFFFF')) #.move_to(RIGHT+0.1).next_to(vc, direction=DOWN)
		# ds_Q = MathTex(r"\mathbb{Q}", fill_color=logo_black).scale(7)
		# ds_Q.shift(2.25 * LEFT + 1.5 * UP)
		# ds_E = MathTex(r"\mathbb{E}", fill_color=logo_black).scale(7)
		# ds_E.shift(2.25 * LEFT + 1.5 * UP)
		self.add(boxes)
		# animation = [
		# 	y.animate.set_fill("PINK", opacity=0.5),
		# 	vg[0].animate.set_fill("PINK", opacity=0.5),
		# 	MoveAlongPath(vg[0], ArcBetweenPoints(vg[0].get_center(),y.get_center()), rate_func=linear),
		# 	MoveAlongPath(y, ArcBetweenPoints(y.get_center(),vg[0].get_center()), rate_func=linear)
		# 	# y.animate.set_fill("BLACK")
		# ]
		y_num.add_updater(lambda d: d.move_to(y.get_center()))
		valueLists_num[0].add_updater(lambda d: d.move_to(vg[0].get_center()))

		# 12, 20, 15, 29, 10, 14
		# highlight 12 and 20
		self.play(
			y.animate.set_fill("PINK", opacity=0.5),
			vg[0][0].animate.set_fill("PINK", opacity=0.5))

		# if 12 > 20 swap
		pass
		# self.play(
		# 	MoveAlongPath(vg[0], ArcBetweenPoints(vg[0].get_center(),y.get_center()), rate_func=linear),
		# 	MoveAlongPath(y, ArcBetweenPoints(y.get_center(),vg[0].get_center()), rate_func=linear)
		# 	)
		
		# remove hightlight 12 and 20
		self.play(
			y.animate.set_fill(opacity=0),
			vg[0][0].animate.set_fill(opacity=0))

		# 12, 20, 15, 29, 10, 14
		#highlight 20 and 15
		self.play(
			vg[0][0].animate.set_fill("PINK", opacity=0.5),
			vg[1][0].animate.set_fill("PINK", opacity=0.5)
			)

		# 20 > 15 swap
		self.play(
			MoveAlongPath(vg[1], ArcBetweenPoints(vg[1].get_center(),vg[0].get_center()), rate_func=linear),
			MoveAlongPath(vg[0], ArcBetweenPoints(vg[0].get_center(),vg[1].get_center()), rate_func=linear)
			)

		#remove highlight 20 and 15
		self.play(
			vg[0][0].animate.set_fill(opacity=0),
			vg[1][0].animate.set_fill(opacity=0)
			)

		# 12, 15, 20, 29, 10, 14
		# highlighting 20, 29
		self.play(
			vg[0][0].animate.set_fill("PINK", opacity=0.5),
			vg[2][0].animate.set_fill("PINK", opacity=0.5)
			)

		#remove highlight 20 and 29
		self.play(
			vg[0][0].animate.set_fill(opacity=0),
			vg[2][0].animate.set_fill(opacity=0)
			)

		# 12, 15, 20, 29, 10, 14
		# highlighting 29, 10
		self.play(
			vg[2][0].animate.set_fill("PINK", opacity=0.5),
			vg[3][0].animate.set_fill("PINK", opacity=0.5)
			)

		# 29 > 14 swap
		self.play(
			MoveAlongPath(vg[2], ArcBetweenPoints(vg[2].get_center(),vg[3].get_center()), rate_func=linear),
			MoveAlongPath(vg[3], ArcBetweenPoints(vg[3].get_center(),vg[2].get_center()), rate_func=linear)
			)

		#remove highlight 29 and 10
		self.play(
			vg[2][0].animate.set_fill(opacity=0),
			vg[3][0].animate.set_fill(opacity=0)
			)

		# 12, 15, 20, 10, 29, 14
		# highlighting 29, 14
		self.play(
			vg[2][0].animate.set_fill("PINK", opacity=0.5),
			vg[4][0].animate.set_fill("PINK", opacity=0.5)
			)

		# 29 > 14 swap
		self.play(
			MoveAlongPath(vg[2], ArcBetweenPoints(vg[2].get_center(),vg[4].get_center()), rate_func=linear),
			MoveAlongPath(vg[4], ArcBetweenPoints(vg[4].get_center(),vg[2].get_center()), rate_func=linear)
			)

		#remove highlight 29 and 10
		self.play(
			vg[2][0].animate.set_fill(opacity=0),
			vg[4][0].animate.set_fill(opacity=0)
			)
		# self.play(AnimationGroup(*animation, lag_ratio=0.5), run_time=2)
		self.wait()

