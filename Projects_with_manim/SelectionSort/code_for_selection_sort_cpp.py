from manim import *

class CodeForSelectionSort(Scene):
	"""docstring for CodeForSelectionSort"""
	def construct(self):
		coded = """void SelectionSort(int arr[], int n)
{
	int i, j, temp;
	for (i = 0; i < n - 1; i++) {
		min_index = i;
		for (j=i+1; j < n; j++) {
			if(arr[min_index]>arr[j]){
				min_index = j;
			}
		}
 
		if (arr[i] != arr[min_index] && min_index != i){
			temp = arr[min_index];
			arr[min_index] = arr[i];
			arr[i] = temp;
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
		codes.code.set_opacity(0.5)
		self.add(codes)
		# self.play(Write(codes.move_to(LEFT*(positionY-3)+UP*(-positionY+1.5))))