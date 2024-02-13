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
		self.add(boxes)
		y_num.add_updater(lambda d: d.move_to(y.get_center()))

		########### static style: 

		#### 1st iteration:

		# 12, 20, 15, 29, 10, 14
		# highlight 12 and 20
		iter1 = Text("1st Iteration").next_to(boxes, DOWN)
		self.add(iter1)
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
		self.remove(iter1)
		# 12, 15, 20, 10, 14, 29

		#### 2nd iteration:
		iter2 = Text("2nd Iteration").next_to(boxes, DOWN)
		self.add(iter2)

		# highlight 12 and 15
		self.play(
			y.animate.set_fill("PINK", opacity=0.5),
			vg[1][0].animate.set_fill("PINK", opacity=0.5)
			)

		#remove highlight 12 and 15
		self.play(
			y.animate.set_fill(opacity=0),
			vg[1][0].animate.set_fill(opacity=0)
			)

		# 12, 15, 20, 10, 14, 29
		# highlight 15 and 20
		self.play(
			vg[0][0].animate.set_fill("PINK", opacity=0.5),
			vg[1][0].animate.set_fill("PINK", opacity=0.5)
			)

		#remove highlight 15 and 20
		self.play(
			vg[0][0].animate.set_fill(opacity=0),
			vg[1][0].animate.set_fill(opacity=0)
			)

		# 12, 15, 20, 10, 14, 29
		# highlight 20 and 10
		self.play(
			vg[0][0].animate.set_fill("PINK", opacity=0.5),
			vg[3][0].animate.set_fill("PINK", opacity=0.5)
			)

		# 20 > 10 swap
		self.play(
			MoveAlongPath(vg[0], ArcBetweenPoints(vg[0].get_center(),vg[3].get_center()), rate_func=linear),
			MoveAlongPath(vg[3], ArcBetweenPoints(vg[3].get_center(),vg[0].get_center()), rate_func=linear)
			)

		#remove highlight 20 and 10
		self.play(
			vg[0][0].animate.set_fill(opacity=0),
			vg[3][0].animate.set_fill(opacity=0)
			)
		# 12, 15, 10, 20, 14, 29
		# highlight 20 and 14
		self.play(
			vg[0][0].animate.set_fill("PINK", opacity=0.5),
			vg[4][0].animate.set_fill("PINK", opacity=0.5)
			)

		# 20 > 14 swap
		self.play(
			MoveAlongPath(vg[0], ArcBetweenPoints(vg[0].get_center(),vg[4].get_center()), rate_func=linear),
			MoveAlongPath(vg[4], ArcBetweenPoints(vg[4].get_center(),vg[0].get_center()), rate_func=linear)
			)
		
		#remove highlight 20 and 14
		self.play(
			vg[0][0].animate.set_fill(opacity=0),
			vg[4][0].animate.set_fill(opacity=0)
			)
		self.remove(iter2)
		# 12, 15, 10, 14, 20, 29

		#### 3rd iteration:
		iter3 = Text("3rd Iteration").next_to(boxes, DOWN)
		self.add(iter3)

		# highlight 12 and 15
		self.play(
			y.animate.set_fill("PINK", opacity=0.5),
			vg[1][0].animate.set_fill("PINK", opacity=0.5)
			)

		# 12 > 15 swap
				
		#remove highlight 20 and 14
		self.play(
			y.animate.set_fill(opacity=0),
			vg[1][0].animate.set_fill(opacity=0)
			)

		# 12, 15, 10, 14, 20, 29
		# highlight 15 and 10
		self.play(
			vg[3][0].animate.set_fill("PINK", opacity=0.5),
			vg[1][0].animate.set_fill("PINK", opacity=0.5)
			)

		# 15 > 10 swap
		self.play(
			MoveAlongPath(vg[1], ArcBetweenPoints(vg[1].get_center(),vg[3].get_center()), rate_func=linear),
			MoveAlongPath(vg[3], ArcBetweenPoints(vg[3].get_center(),vg[1].get_center()), rate_func=linear)
			)

		#remove highlight 15 and 10
		self.play(
			vg[3][0].animate.set_fill(opacity=0),
			vg[1][0].animate.set_fill(opacity=0)
			)

		# 12, 10, 15, 14, 20, 29
		# highlight 15 and 14
		self.play(
			vg[4][0].animate.set_fill("PINK", opacity=0.5),
			vg[1][0].animate.set_fill("PINK", opacity=0.5)
			)

		# 15 > 14 swap
		self.play(
			MoveAlongPath(vg[1], ArcBetweenPoints(vg[1].get_center(),vg[4].get_center()), rate_func=linear),
			MoveAlongPath(vg[4], ArcBetweenPoints(vg[4].get_center(),vg[1].get_center()), rate_func=linear)
			)

		#remove highlight 15 and 14
		self.play(
			vg[4][0].animate.set_fill(opacity=0),
			vg[1][0].animate.set_fill(opacity=0)
			)
		self.remove(iter3)

		#### 4rd iteration:
		iter4 = Text("4th Iteration").next_to(boxes, DOWN)
		self.add(iter4)

		# 12, 10, 14, 15, 20, 29
		# highlight 12 and 10
		self.play(
			y.animate.set_fill("PINK", opacity=0.5),
			vg[3][0].animate.set_fill("PINK", opacity=0.5),
			)

		# 12 > 10 swap
		self.play(
			MoveAlongPath(y, ArcBetweenPoints(y.get_center(),vg[3].get_center()), rate_func=linear),
			MoveAlongPath(vg[3], ArcBetweenPoints(vg[3].get_center(),y.get_center()), rate_func=linear)
			)

		#remove highlight 12 and 10
		self.play(
			vg[3][0].animate.set_fill(opacity=0),
			y.animate.set_fill(opacity=0)
			)

		# 10, 12, 14, 15, 20, 29
		# highlight 12 and 10
		self.play(
			vg[4][0].animate.set_fill("PINK", opacity=0.5),
			y.animate.set_fill("PINK", opacity=0.5)
			)

		# 12 > 10 swap

		#remove highlight 12 and 10
		self.play(
			vg[4][0].animate.set_fill(opacity=0),
			y.animate.set_fill(opacity=0)
			)
		self.remove(iter4)

		# 10, 12, 14, 15, 20, 29
		#### 5rd iteration:
		iter5 = Text("5th Iteration").next_to(boxes, DOWN)
		self.add(iter5)
		# highlight 12 and 10
		self.play(
			vg[3][0].animate.set_fill("PINK", opacity=0.5),
			y.animate.set_fill("PINK", opacity=0.5)
			)

		# 12 > 10 swap

		#remove highlight 12 and 10
		self.play(
			vg[3][0].animate.set_fill(opacity=0),
			y.animate.set_fill(opacity=0)
			)
		# 10, 12, 14, 15, 20, 29
		self.wait()

