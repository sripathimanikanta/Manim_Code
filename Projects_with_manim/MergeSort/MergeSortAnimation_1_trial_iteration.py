from manim import *

class MergeSortAnime(Scene):
	"""docstring for MergeSortAnime"""
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
		self.add(vg.scale(0.8), indexText)

		b = Brace(vg[:3], sharpness=1)
		b1 = Brace(vg[3:])
		vg0to2 = vg[:3].copy()
		arr1 = Arrow(start=b.get_center(), end=[-3,1,0])
		self.play(
			vg0to2.animate.next_to(arr1.end,DOWN)
		)

		b01 = Brace(vg0to2[:2])
		vg0to1 = vg0to2[:2].copy()
		arr2 = Arrow(start=b01.get_center(), end=[-5,-1.5,0])
		self.play(
			vg0to1.animate.next_to(arr2.end, DOWN)
		)

		vgb = VGroup(b,b1, arr1, b01, arr2)
		self.play(Write(vgb))

		# ########## Dynamic style:
		# for x in range(0, len(vg)-1):
		# 	self.play(
		# 		vg[x][0].animate.set_fill("MAROON", opacity=0.5)
		# 		)
		# 	if x == 0:
		# 		keySquare = Square(side_length=sl).next_to(vg[x][0].get_center(), DOWN*5)
		# 		keytext = Text("min_index").next_to(keySquare, RIGHT)
		# 		key = Integer(0)
		# 		keygp = VGroup(keySquare, key)
		# 		self.play(
		# 			Create(keygp[0]),
		# 			Write(keytext)
		# 			)
		# 	# keygp = VGroup(keySquare, key)
		# 	keygp[1] = vg[x][2].copy()
		# 	self.play(
		# 		keygp[1].animate.move_to(keygp[0].get_center()),
		# 		vg[x][0].animate.set_fill("MAROON", opacity=0)
		# 		)
		# 	for y in range(x+1,len(vg)):
		# 		self.play(
		# 			vg[keygp[1].number][0].animate.set_fill("MAROON", opacity=0.5),
		# 			vg[y][0].animate.set_fill("RED", opacity=0.5)
		# 			)
		# 		self.play(
		# 			vg[keygp[1].number][0].animate.set_fill("MAROON", opacity=0),
		# 			vg[y][0].animate.set_fill("RED", opacity=0)
		# 			)
		# 		if(vg[keygp[1].number][1].number > vg[y][1].number):
		# 			self.play(
		# 				Uncreate(keygp[1]),
		# 				vg[y][0].animate.set_fill("RED", opacity=0.5)
		# 				)
		# 			keygp[1] = vg[y][2].copy()
		# 			self.play(
		# 				keygp[1].animate.move_to(keygp[0].get_center()),
		# 				# vg[keygp[1].number][0].animate.set_fill("MAROON", opacity=0),
		# 				vg[y][0].animate.set_fill("RED", opacity=0)
		# 			)

		# 	if(keygp[1].number != x and vg[keygp[1].number][1].number != vg[x][1].number):
		# 		vgtemp1 = Integer(keygp[1].number)
		# 		vgtemp2 = Integer(x)
		# 		self.play(
		# 			MoveAlongPath(vg[keygp[1].number], ArcBetweenPoints(vg[keygp[1].number].get_center(),vg[x].get_center())),
		# 			MoveAlongPath(vg[x], ArcBetweenPoints(vg[x].get_center(),vg[keygp[1].number].get_center()))
		# 			)
		# 		vg[x][2] = vgtemp1
		# 		vg[keygp[1].number][2] = vgtemp2
				
		# 		temp = vg[x]
		# 		vg[x] = vg[keygp[1].number]
		# 		vg[keygp[1].number] = temp

		# 		self.play(
		# 			Write(vg[x][2].next_to(vg[x][0].get_center(), DOWN*2.7)),
		# 			Write(vg[keygp[1].number][2].next_to(vg[keygp[1].number][0].get_center(), DOWN*2.7)),
		# 			vg[x][0].animate.set_fill("RED", opacity=0.8)
		# 			)
		# 	keytext.add_updater(lambda x: x.next_to(keySquare, RIGHT))
			
		# 	if x != len(vg)-2:
		# 		self.play(
		# 			keygp[0].animate.next_to(vg[x+1][0].get_center(), DOWN*5),
		# 			Uncreate(keygp[1])
		# 			)
		# 	else:
		# 		self.play(
		# 			Uncreate(keygp),
		# 			Uncreate(keytext)
		# 			)
			# self.wait()
