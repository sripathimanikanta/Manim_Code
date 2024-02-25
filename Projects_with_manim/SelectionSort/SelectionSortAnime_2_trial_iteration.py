from manim import *

class SelectionSortAnime(Scene):
	"""docstring for BubbleSortAnime"""
	def construct(self):
		# arr =  [12,20,15,29,10,14]
		arr =  [13,20,7,28,3,8]
		positionX = 3.0
		indexTextX = positionX + 2
		positionY = 3.0
		indexTextY = -positionY + 0.8
		sl = 1.0
		y = Square(side_length=sl).move_to(LEFT*positionX+UP*positionY)
		y_num = Integer(arr[0]).move_to(y.get_center())
		valueLists = [Square(side_length=sl) for x in range(0,len(arr)-1)]
		valueLists_nums = arr[1:]
		valueLists_num = [Integer(x) for x in valueLists_nums]
		indexText = Text("Indices:")

		vg = VGroup()
		for x in range(0,len(arr)-1):
			if x == 0:
				z = valueLists[x].next_to(y, direction=RIGHT)
				z_vals = valueLists_num[x].move_to(z.get_center())
				vg = vg + VGroup(y, y_num, Integer(0).next_to(y_num, DOWN*2))
				vg = vg + VGroup(z,z_vals, Integer(1).next_to(z_vals, DOWN*2))
			else:
				z = valueLists[x].next_to(valueLists[x-1],direction=RIGHT)
				z_vals = valueLists_num[x].move_to(z.get_center())
				indices = Integer(x+1).next_to(z_vals, DOWN*2)
				vg = vg + VGroup(z,z_vals, indices)
		print(vg)
		indexText.shift(LEFT*indexTextX, DOWN*indexTextY)
		# print(valueLists_num)
		# self.play(Write(y),Write(y_num))
		self.add(vg, indexText)

		########## Dynamic style:
		for x in range(0, len(vg)-1):
			self.play(
				vg[x][0].animate.set_fill("MAROON", opacity=0.5)
				)
			keySquare = Square(side_length=sl).next_to(vg[x][0].get_center(), DOWN*5)
			key = Integer(0)
			keygp = VGroup(keySquare, key)
			keytext = Text("min_index").next_to(keySquare, RIGHT)
			self.play(
				Create(keygp[0]),
				Write(keytext)
				)
			keygp[1] = vg[x][2].copy()
			self.play(
				keygp[1].animate.move_to(keygp[0].get_center()),
				vg[x][0].animate.set_fill("MAROON", opacity=0)
				)
			self.play(
				vg[x][0].animate.set_fill("MAROON", opacity=0.5),
				vg[x+1][0].animate.set_fill("RED", opacity=0.5)
				)
			self.play(
				Uncreate(keygp[0]),
				Uncreate(keytext),
				Uncreate(keygp[1]),
				vg[x][0].animate.set_fill("MAROON", opacity=0),
				vg[x+1][0].animate.set_fill("RED", opacity=0)
				)
