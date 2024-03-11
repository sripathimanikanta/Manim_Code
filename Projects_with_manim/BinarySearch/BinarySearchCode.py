from manim import *

class BinarySearchCode(Scene):
	def construct(self):
		coded = """void BinarySearch(int arr[])
{
	int leng = sizeof(arr)/sizeof(int)
	int key = 8;
	int start = 0;
	int end = leng-1;
	int mid=0;
	bool bbool = false
	while(start>=end){
		mid = (start+end)/2;
		if(arr[mid] == key){
			cout << "Found key,it's at the index:" << mid;
			bbool = true
			break;
		} 
		else{
			if(num[mid] < key){
				start = mid+1;
			}
			else{
				end = mid;
			}
		}
	}
	if(bbool == false){
		cout << "Not Found" << endl;
	}
}
"""
		Codes = Code(code=coded,
			language="cpp",
			tab_width=4,
			style=Code.styles_list[13],
			background="window",
			).scale(0.8)
		self.add(Codes.scale(0.8).move_to(LEFT*(3)))