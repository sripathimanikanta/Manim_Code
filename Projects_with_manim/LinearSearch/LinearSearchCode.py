from manim import *

class LinearSearchCode(Scene):
	def construct(self):
		coded = """void LinearSearch(int arr[])
{
	int leng = sizeof(arr)/sizeof(arr[0]);
	int key = 3;
	bool fbool = false;
	for(int i=0;i<leng;i++){
		if arr[i] == key{
			cout << "Found key,It is at the index: " << i << endl;
			fbool = true;
			break;
		}
	}
	if(fbool == false){
		cout << "Not Found!!!" << endl;
	}
}
"""
		Codes = Code(code=coded,
			language="cpp",
			tab_width=4,
			style=Code.styles_list[13],
			background="window",
			# background_with_stroke_color
			)
		self.add(Codes)