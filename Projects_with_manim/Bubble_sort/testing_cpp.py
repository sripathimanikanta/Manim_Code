from manim import *

class BubbleSortAnime(Scene):
	"""docstring for BubbleSortAnime"""
	def construct(self):
		coded = """void bubbleSort(int arr[], int n)
{
	int i, j;
	bool swapped;
	for (i = 0; i < n - 1; i++) {
		swapped = false;
		for (j = 0; j < n - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				swap(arr[j], arr[j + 1]);
				swapped = true;
			}
		}
 
		// If no two elements were swapped
		// by inner loop, then break
		if (swapped == false)
			 break;
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