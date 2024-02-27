from manim import *

class Shuffler(Scene):
	"""docstring for Shuffler"""
	def construct(self):
		arr =  [13, 20, 7, 28, 3, 8]
		arrf =  [8,7,3,13,20,28]
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
		coded = """void bubbleSort(int arr[], int n)
{
	int i, j;
	bool swapped;
	for (i = 0; i < n - 1; i++) {
		for (j = 0; j < n - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				swap(arr[j], arr[j + 1]);
			}
		}
	}
}
"""
		codes = Code(code=coded, 
					language="cpp",
					tab_width=4,
					style=Code.styles_list[13],
					background = "window",
					background_stroke_color=ManimColor('#FFFFFF'))
		codes.code.set_opacity(0.3)
		self.add(codes.move_to(LEFT*(positionY-3)+UP*(-positionY+1.5)))
		codes.code[0].set_opacity(1)

		self.play(
					MoveAlongPath(vg[5], ArcBetweenPoints(vg[5].get_center(),vg[0].get_center()), rate_func=linear),
					MoveAlongPath(vg[0], ArcBetweenPoints(vg[0].get_center(),vg[3].get_center()), rate_func=linear),
					MoveAlongPath(vg[1], ArcBetweenPoints(vg[1].get_center(),vg[4].get_center()), rate_func=linear),
					MoveAlongPath(vg[4], ArcBetweenPoints(vg[4].get_center(),vg[2].get_center()), rate_func=linear),
					MoveAlongPath(vg[2], ArcBetweenPoints(vg[2].get_center(),vg[1].get_center()), rate_func=linear),
					MoveAlongPath(vg[3], ArcBetweenPoints(vg[3].get_center(),vg[5].get_center()), rate_func=linear),
					run_time=3)
		self.wait(2)