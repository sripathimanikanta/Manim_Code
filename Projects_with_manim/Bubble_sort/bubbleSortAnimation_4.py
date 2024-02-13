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
				vg = vg + VGroup(y, y_num)
				vg = vg + VGroup(z,z_vals)
			else:
				z = valueLists[x].next_to(valueLists[x-1],direction=RIGHT)
				z_vals = valueLists_num[x].move_to(z.get_center())
				vg = vg + VGroup(z,z_vals)
		print(vg)
		print("vg[0]:",vg[0])
		print("vg[1]:",vg[1])
		print("vg[1]:",vg[2])
		self.add(vg)
		y_num.add_updater(lambda d: d.move_to(y.get_center()))

		########### static style: 
		iter1 = Text("1st Iteration").next_to(vg, DOWN)
		self.add(iter1)
		#### 1st iteration:
		for x in range(0, len(vg)-1):
			self.play(
				vg[x][0].animate.set_fill("PINK", opacity=0.5),
				vg[x+1][0].animate.set_fill("PINK", opacity=0.5)
				)
			if vg[x][1].number > vg[x+1][1].number:
				self.play(
				MoveAlongPath(vg[x], ArcBetweenPoints(vg[x].get_center(),vg[x+1].get_center()), rate_func=linear),
				MoveAlongPath(vg[x+1], ArcBetweenPoints(vg[x+1].get_center(),vg[x].get_center()), rate_func=linear)
				)
				temp = vg[x]
				vg[x] = vg[x+1]
				vg[x+1] = temp
			self.play(
				vg[x][0].animate.set_fill(opacity=0),
				vg[x+1][0].animate.set_fill(opacity=0)
				)

		# 12, 20, 15, 29, 10, 14
		# highlight 12 and 20 
		self.wait()

