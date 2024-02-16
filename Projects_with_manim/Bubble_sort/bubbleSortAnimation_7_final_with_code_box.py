from manim import *

class BubbleSortAnime(Scene):
	"""docstring for BubbleSortAnime"""
	def construct(self):
		# arr =  [12,20,15,29,10,14]
		arr =  [13,20,7,28,3,8]
		positionX = 3.0
		positionY = 3.0
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

		coded = """def bubbleSortQE(arr):
	n=len(arr)
	for i in range(n-1):
		# swapped = False
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
			# swapped = True

		# if not swapped:
			# break;
"""
		codes = Code(code=coded, 
					language="Python",
					tab_width=4,
					style=Code.styles_list[13],
					background = "window",
					background_stroke_color=ManimColor('#FFFFFF'))
		codes.code.set_opacity(0.5)
		self.play(Write(codes.move_to(LEFT*(positionY-3)+UP*(-positionY+1.5))))

		########## static style:
		self.wait(2)
		for y in range(0, len(vg)-1):
			iter1 = Text(f"{y+1} Iteration", t2c={'[:1]':'#5CD0B3'}).next_to(vg, DOWN)
			self.add(iter1)
			self.play(codes.code[2].animate.set_opacity(1))
			#### 1st iteration:
			for x in range(0, len(vg)-1-y):
				self.play(
					codes.code[2].animate.set_opacity(0.5),
					codes.code[4].animate.set_opacity(1),
					vg[x][0].animate.set_fill("MAROON", opacity=0.5),
					# vg[x+1][0].animate.set_fill("PINK", opacity=0.5)
					)
				vg[x][0].set_fill("MAROON", opacity=0.5)
				# self.play(
				# 	listing.code[2].animate.set_opacity(0.5),
				# 	listing.code[3].animate.set_opacity(1),
				# 	)
				self.play(
					codes.code[4].animate.set_opacity(0.5),
					codes.code[5].animate.set_opacity(1),
					vg[x+1][0].animate.set_fill("MAROON", opacity=0.5)
					)
				# self.play(
				# 	# codes.code[2].animate.set_opacity(0.5),
				# 	codes.code[4].animate.set_opacity(0.5),
				# 	# vg[x+1][0].animate.set_fill("PINK", opacity=0.5)
				# 	)
				# self.play(
				# 	codes.code[4].animate.set_opacity(0.5),
				# 	codes.code[5].animate.set_opacity(1),
				# 	vg[x][0].animate.set_fill("PINK", opacity=0.5),
				# 	vg[x+1][0].animate.set_fill("PINK", opacity=0.5)
				# 	)
				self.play(codes.code[5].animate.set_opacity(0.5))
				if vg[x][1].number > vg[x+1][1].number:
					self.play(
						# codes.code[5].animate.set_opacity(0.5),
						codes.code[6].animate.set_opacity(1)
					)
					self.play(
						MoveAlongPath(vg[x], ArcBetweenPoints(vg[x].get_center(),vg[x+1].get_center()), rate_func=linear),
						MoveAlongPath(vg[x+1], ArcBetweenPoints(vg[x+1].get_center(),vg[x].get_center()), rate_func=linear)
					)
					temp = vg[x]
					vg[x] = vg[x+1]
					vg[x+1] = temp
					self.play(
						codes.code[6].animate.set_opacity(0.5),
						# listing.code[7].animate.set_opacity(1)
					)
				self.play(
					vg[x][0].animate.set_fill(opacity=0),
					vg[x+1][0].animate.set_fill(opacity=0)
					)
				vg[x][0].set_fill(opacity=0)
			if y != len(vg)-2:
				self.remove(iter1)
		self.wait()


		
		

