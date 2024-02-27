from manim import *

class InsertionSortAnime(Scene):
	"""docstring for InsertionSortAnime"""
	def construct(self):
		# arr =  [12,20,15,29,10,14]
		arr =  [13,20,7,28,3,8]
		positionX = 3.0
		positionY = 0.0
		sl = 1.0
		y = Square(side_length=sl).move_to(LEFT*positionX+UP*positionY)
		y_num = Integer(arr[0]).move_to(y.get_center())
		valueLists = [Square(side_length=sl) for x in range(0,len(arr)-1)]
		valueLists_nums = arr[1:]
		valueLists_num = [Integer(x) for x in valueLists_nums]

		vg = VGroup()
		for x in range(0,len(arr)-1):
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
		# print(valueLists_num)
		# self.play(Write(y),Write(y_num))
		self.add(vg)
		########## static style:
		########## Dynamic style:
		self.play(
			vg[1][0].animate.set_fill("MAROON", opacity=0.5)
			)
		keySquare = Square(side_length=sl).next_to(vg[1][0].get_center(), UP*3)
		key = Integer(0)
		keygp = VGroup(keySquare, key)
		keytext = Text("key").next_to(keySquare, UP)
		self.play(
			Create(keygp[0]),
			Write(keytext)
			)
		keygp[1] = vg[1][1].copy()
		self.play(
			keygp[1].animate.move_to(keygp[0].get_center()),
			vg[1][0].animate.set_fill("MAROON", opacity=0)
			)
		self.play(
			vg[0][0].animate.set_fill("MAROON", opacity=0.5),
			keygp[0].animate.set_fill("RED", opacity=0.5)
			)


		# self.play(
		# 	Create(keygp[0][0], keytext)
		# 	)




		

