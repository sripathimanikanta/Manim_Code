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
				vg = vg + VGroup(z) + VGroup(z_vals)
			else:
				z = valueLists[x].next_to(valueLists[x-1],direction=RIGHT)
				z_vals = valueLists_num[x].move_to(z.get_center())
				vg = vg + VGroup(z) + VGroup(z_vals)

		boxes = VGroup(y, y_num, vg)
		coded = """def bubbleSortQE(arr):
	n=len(arr)
	for i in range(n-1):
		swapped = False
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
			swapped = True

		if not swapped:
			break;
"""
		# circles = [Circle(radius=0.1,color=Y, fill_opacity=1).move_to(RIGHT*X) for X,Y in zip([0.4,0.8,1.2],['RED','BLUE', 'GREEN'])]
		# vc = VGroup()
		# for x in circles:
		# 	vc = vc + VGroup(x)
		# vc.next_to(boxes, DOWN+LEFT*0.1)
		codes = Code(code=coded, 
					language="Python",
					tab_width=4,
					style=Code.styles_list[13],
					background = "window",
					background_stroke_color=ManimColor('#FFFFFF')) #.move_to(RIGHT+0.1).next_to(vc, direction=DOWN)
		self.add(boxes, codes)

