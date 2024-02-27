from manim import *

class InsertionSortAnime(Scene):
	"""docstring for InsertionSortAnime"""
	def construct(self):
		arr =  [12,20,15,29,10,14]
		# arr =  [13,20,7,28,3,8]
		positionX = 3.0
		positionY = 2.0
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

		coded = """def InsertionSortAnimation(arr):
	n=len(arr)
	for i in range(1, n):
		key = arr[i]
		j = i - 1
		while j>=0 and arr[j] > key:
			arr[j+1] = arr[j]
			j -= 1
		if arr[j+1] != key:
			arr[j + 1] = key
"""
		codes = Code(code=coded, 
					language="Python",
					tab_width=4,
					style=Code.styles_list[13],
					background = "window",
					background_stroke_color=ManimColor('#FFFFFF'))
		codes.code.set_opacity(0.4)
		self.play(Write(codes.move_to(LEFT*(positionX-3)+UP*(-positionY+0.5))))
		self.play(codes.code[0].animate.set_opacity(1))

		########## Dynamic style:
		for x in range(1, len(vg)):
			iter1 = Text(f"{x} Iteration", t2c={'[:1]':'#5CD0B3'}).next_to(vg, DOWN)
			self.add(iter1)
			self.play(codes.code[2].animate.set_opacity(1))
			self.play(
				vg[x][0].animate.set_fill("MAROON", opacity=0.5),
				codes.code[2].animate.set_opacity(0.4)
				)
			keySquare = Square(side_length=sl).next_to(vg[x][0].get_center(), UP*3)
			key = Integer(0)
			keygp = VGroup(keySquare, key)
			keytext = Text("key").next_to(keySquare, RIGHT)
			self.play(
				Create(keygp[0]),
				Write(keytext)
				)
			keygp[1] = vg[x][1].copy()
			self.play(
				keygp[1].animate.move_to(keygp[0].get_center()),
				vg[x][0].animate.set_fill("MAROON", opacity=0),
				codes.code[3].animate.set_opacity(1)
				)
			# self.play(
			# 		vg[x-1][0].animate.set_fill("MAROON", opacity=0.5),
			# 		keygp[0].animate.set_fill("RED", opacity=0.5)
			# 		)
			y = x - 1
			self.play(
				codes.code[3].animate.set_opacity(0.4),
				codes.code[4].animate.set_opacity(1)
				)
			self.play(
					vg[y][0].animate.set_fill("MAROON", opacity=0.5),
					keygp[0].animate.set_fill("MAROON", opacity=0.5),
					codes.code[4].animate.set_opacity(0.4)
					)
			self.play(
					vg[y][0].animate.set_fill("MAROON", opacity=0),
					keygp[0].animate.set_fill("MAROON", opacity=0),
					)
			while y >= 0 and vg[y][1].number > keygp[1].number:
				self.play(
					codes.code[4].animate.set_opacity(0.4),
					codes.code[5].animate.set_opacity(1)
				)
				vg[y+1][1] = vg[y][1].copy()
				self.play(
					vg[y][0].animate.set_fill("MAROON", opacity=0.5),
					keygp[0].animate.set_fill("MAROON", opacity=0.5),
					codes.code[5].animate.set_opacity(0.4)
					)
				self.play(
					vg[y+1][1].animate.move_to(vg[y+1][0].get_center()),
					codes.code[6].animate.set_opacity(1)
				)
				self.play(
					vg[y][0].animate.set_fill("MAROON", opacity=0),
					keygp[0].animate.set_fill("MAROON", opacity=0),
					)
				y -= 1
				self.play(
					codes.code[6].animate.set_opacity(0.4),
					codes.code[7].animate.set_opacity(1),
					)
				self.play(
					codes.code[7].animate.set_opacity(0.4)
					)
			if vg[y+1][1].number != keygp[1].number:
				self.play(
					codes.code[8].animate.set_opacity(1),
					)
				vg[y+1][1]= keygp[1].copy()
				self.play(
						vg[y+1][1].animate.move_to(vg[y+1][0].get_center()),
						codes.code[8].animate.set_opacity(0.4),
						codes.code[9].animate.set_opacity(1)
					)
				self.play(
					codes.code[9].animate.set_opacity(0.4),
					)
			self.play(
				Uncreate(keygp[0]),
				Unwrite(keytext),
				Unwrite(keygp[1]),
				)
			if x != len(vg)-1:
				self.remove(iter1)
			self.wait()
		
		

