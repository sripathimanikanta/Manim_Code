from manim import *

class LinearSearchAnime(Scene):
	"""docstring for Linear Search Anime"""
	def construct(self):
		# arr =  [12,20,15,29,10,14]
		arr =  [13,20,7,28,3,8]
		positionX = 3.0
		indexTextX = positionX + 2
		positionY = 3.5
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
		gp = VGroup(vg, indexText).scale(0.8)
		# print(valueLists_num)
		# self.play(Write(y),Write(y_num))
		self.play(Write(gp))

		# self.play(
		# 	vg[5][0].animate.set_fill("RED",opacity=0.5)
		# 	)
		# key = 8
		

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
			)
		Codes.code.set_opacity(0.3)
		self.play(Write(Codes.scale(0.8).move_to(LEFT*(positionX-3)+UP*(-positionY+2))))

		keySquare = Square(side_length=sl).scale(0.8).next_to(vg[1][0].get_center(), DOWN*5)
		key = Integer(3).scale(0.8).next_to(keySquare.get_center(), DOWN*0)
		keytext = Text("key").scale(0.8).next_to(keySquare, LEFT)
		keygp = VGroup(keySquare, key, keytext)

		fboolSquare = Square(side_length=sl).scale(0.8).next_to(vg[1][0].get_center(), LEFT*8+DOWN*5)
		fboool = Text("false").scale(0.4).next_to(fboolSquare.get_center(), DOWN*0)
		fbooltext = Text("fbool").scale(0.8).next_to(fboolSquare, LEFT)
		fboolgp = VGroup(fboolSquare, fboool, fbooltext)
		# self.add(keygp, keytext)

		# found = Text("Found the key").next_to(keySquare, RIGHT)
		index = Text("Found key, It's at the index:").scale(0.5).next_to(keySquare, RIGHT*2)
		notfound = Text("Not Found!!!").next_to(keySquare, RIGHT*2)
		fbool = False

		self.play(Codes.code[0].animate.set_opacity(1))
		self.play(
			Codes.code[3].animate.set_opacity(1),
			Write(keygp)
			)
		self.play(
			Codes.code[3].animate.set_opacity(0.3),
			)
		self.play(
			Codes.code[4].animate.set_opacity(1),
			Write(fboolgp)
			)
		self.play(
			Codes.code[4].animate.set_opacity(0.3),
			)
		for i in range(0, len(vg)):
			iter1 = Text(f"{i+1} Iteration", t2c={'[:1]':'#5CD0B3'}).next_to(vg, RIGHT)
			self.add(iter1)
			self.play(
				Codes.code[5].animate.set_opacity(1)
				)
			# self.play(
			# 	vg[i][0].animate.set_fill("BLUE", opacity=0.5)
			# )
			# self.play(
			# 	vg[i][0].animate.set_fill("BLUE", opacity=0)
			# )
			self.play(
					Codes.code[5].animate.set_opacity(0.3),
					Codes.code[6].animate.set_opacity(1),
					vg[i][0].animate.set_fill("BLUE", opacity=0.5),
					keygp[0].animate.set_fill("RED", opacity=0.5),
				)
			self.play(
					Codes.code[6].animate.set_opacity(0.3),
					keygp[0].animate.set_fill("RED", opacity=0),
				)
			if vg[i][1].number == keygp[1].number:
					self.play(
					vg[i][0].animate.set_fill("GREEN", opacity=0.5),
					# vg[i][2].animate.set_fill()
					# Write(found.scale(0.5)),
					Write(index),
					vg[i][2].copy().scale(1.5).animate.next_to(index, RIGHT),
					Codes.code[7].animate.set_opacity(1),
					)
					# i+=1
					fbool = True
					self.play(Uncreate(fboool))
					fboool = Text("true").scale(0.4).next_to(fboolSquare.get_center(), DOWN*0)
					self.play(
						Codes.code[7].animate.set_opacity(0.3),
						Codes.code[8].animate.set_opacity(1),
						Write(fboool)
						)
					self.play(
						Codes.code[8].animate.set_opacity(0.3),
						Codes.code[9].animate.set_opacity(1),
						)
					self.play(
						Codes.code[9].animate.set_opacity(0.3)
						)
					break
			if fbool != True and i != len(vg)-1:
				self.remove(iter1)
		self.play(
			Codes.code[12].animate.set_opacity(1)
			)
		self.play(
			Codes.code[12].animate.set_opacity(0.3)
			)
		if(fbool == False):
			self.play(
				Codes.code[13].animate.set_opacity(1),
				Write(notfound.scale(0.5))
				)
			self.play(
				Codes.code[13].animate.set_opacity(0.3)
				)
		self.wait(3)
		# return -1
		