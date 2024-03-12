from manim import *

class BinarySearchAnimeWithCode(Scene):
	"""docstring for Binary Search Anime"""
	def construct(self):
		# arr =  [12,20,15,29,10,14]
		arr =  [3,7,8,13,20,28]
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
		self.play(Write(gp.move_to(RIGHT*3)))

		coded = """void BinarySearch(int arr[])
{
	int leng = sizeof(arr)/sizeof(int)
	int start = 0;
	int end = leng-1;
	int mid=0;
	int key = 28;
	bool bbool = false
	while(start<=end){
		mid = (start+end)/2;
		if(arr[mid] == key){
			cout << "Found key" << endl;
			cout << "it's at the index:" << mid;
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
			).scale(0.7)
		Codes.code.set_opacity(0.3)
		# self.play(Write(Codes.scale(0.8).move_to(LEFT*Camera().pixel_width+UP*(-positionY+2))))
		self.play(Write(Codes.move_to(LEFT*(3))))
		self.play(Codes.code[0].animate.set_opacity(1))
		# self.play(
		# 	vg[5][0].animate.set_fill("RED",opacity=0.5)
		# 	)
		# key = 8
		
		keySquare = Square(side_length=sl).scale(0.8).next_to(vg[1][0].get_center(), UP*10)
		key = Integer(28).scale(0.8).next_to(keySquare.get_center(), DOWN*0)
		keytext = Text("key").scale(0.5).next_to(keySquare, UP*0.5)
		keygp = VGroup(keySquare, key, keytext)

		startSquare = Square(side_length=sl).scale(0.8).next_to(vg[0][0].get_center(), DOWN*5)
		start = Integer(0).scale(0.8).next_to(startSquare.get_center(), DOWN*0)
		starttext = Text("start").scale(0.5).next_to(startSquare, DOWN)
		startgp = VGroup(startSquare, start, starttext)	
		
		endSquare = Square(side_length=sl).scale(0.8).next_to(vg[len(vg)-1][0].get_center(), DOWN*5)
		end = Integer(len(vg)-1).scale(0.8).next_to(endSquare.get_center(), DOWN*0)
		endtext = Text("end").scale(0.5).next_to(endSquare, DOWN)
		endgp = VGroup(endSquare, end, endtext)	
        # int((end.number-start.number)/2)
		midSquare = Square(side_length=sl).scale(0.8).next_to(vg[0][0].get_center(), DOWN*11)
		mid = Integer(0).scale(0.8).next_to(midSquare.get_center(), DOWN*0)
		midtext = Text("mid").scale(0.5).next_to(midSquare, DOWN)
		midgp = VGroup(midSquare, mid, midtext)	
		# print(midgp[1])

		fboolSquare = Square(side_length=sl).scale(0.8).next_to(keySquare.get_center(), RIGHT*5)
		fboool = Text("false").scale(0.4).next_to(fboolSquare.get_center(), DOWN*0)
		fbooltext = Text("fbool").scale(0.5).next_to(fboolSquare, UP*0.5)
		fboolgp = VGroup(fboolSquare, fboool, fbooltext)
		# self.add(keygp, keytext)

		# found = Text("Found the key").next_to(keySquare, RIGHT)
		foundindex = Text("Found key").scale(0.5).next_to(keySquare, RIGHT*2+DOWN*2)
		index = Text("It's at the index:").scale(0.5).next_to(foundindex, DOWN*1)
		notfound = Text("Not Found!!!").next_to(keySquare, RIGHT*2)
		fbool = False

		self.play(
			Write(startgp[0]),
			Write(startgp[2])
		)
		startgp[1] = vg[start.number][2] .copy()
		self.play(
			Codes.code[3].animate.set_opacity(1),
			startgp[1].animate.next_to(startgp[0].get_center(),DOWN*0)
		)
		self.play(
			Codes.code[3].animate.set_opacity(0.3),
			Write(endgp[0]),
			Write(endgp[2])
		)
		endgp[1] = vg[end.number][2] .copy()
		self.play(
			Codes.code[4].animate.set_opacity(1),
			endgp[1].animate.next_to(endgp[0].get_center(),DOWN*0)
		)		
		self.play(
			Codes.code[4].animate.set_opacity(0.3),
			Write(midgp[0]),
			Write(midgp[2])
		)
		midgp[1] = vg[mid.number][2] .copy()
		# print("after first midgp:",midgp[1])
		self.play(
			Codes.code[5].animate.set_opacity(1),
			midgp[1].animate.next_to(midgp[0].get_center(),DOWN*0)
		)		
		self.play(
			Codes.code[5].animate.set_opacity(0.3),
			Codes.code[6].animate.set_opacity(1),
			Write(keygp)
		)
		self.play(
			Codes.code[6].animate.set_opacity(0.3),
			Codes.code[7].animate.set_opacity(1),
			Write(fboolgp)
		)
		self.play(
			Codes.code[7].animate.set_opacity(0.3),
		)
		# iter1 = Text(f"{i+1} Iteration", t2c={'[:1]':'#5CD0B3'}).next_to(vg, RIGHT)
		# self.add(iter1)
		text = MathTex("( {{start}} + {{end}} ) \over 2")
		midcal = VGroup(text)
		# print(midcal)
		# print(midcal[0])
		while (startgp[1].number <= endgp[1].number):
			self.play(
				Codes.code[8].animate.set_opacity(1),
			)
			self.play(
			    Codes.code[8].animate.set_opacity(0.3),
			    Codes.code[9].animate.set_opacity(1),
			)
			text = MathTex("( {{start}} + {{end}} ) \over 2")
			midcal = VGroup(text)
			self.play(
				Write(midcal[0].next_to(vg, UP*3))
			)
			startgpcopy = startgp[1].copy()
			self.play(
				Uncreate(midcal[0][1]),
				startgpcopy.animate.next_to(midcal[0][1], DOWN*0)
			)
			endgpcopy = endgp[1].copy()
			self.play(
				Uncreate(midcal[0][3]),
				endgpcopy.animate.next_to(midcal[0][3], DOWN*0)
			)
			tempmids = startgp[1].number+endgp[1].number
			tempmidltx = MathTex(f"{tempmids} \over 2").next_to(midcal[0][2],DOWN*0)
			self.play(
				FadeOut(startgpcopy,endgpcopy),
				ReplacementTransform(
					midcal[0],tempmidltx
				),
				run_time=1
			)
			self.wait(0.5)
			mids = tempmids/2
			midsltx = MathTex(f"={mids}").next_to(tempmidltx,RIGHT*0)
			self.play(
				ReplacementTransform(
					tempmidltx,midsltx
				),
				run_time=1
			)
			self.wait(0.5)
			midsintltx = MathTex(f"=int({mids})").next_to(tempmidltx,RIGHT*0)
			self.play(
				ReplacementTransform(
					midsltx, midsintltx
				),
				run_time=1
			)
			self.wait(0.5)
			midsint = int(mids)
			midsintltx2 = Integer(midsint).next_to(tempmidltx,RIGHT*0)
			self.play(
				ReplacementTransform(
					midsintltx, midsintltx2
				),
				run_time=1
			)
			self.wait(0.5)
			midnumber = int((endgp[1].number + startgp[1].number)/2)
			self.play(
				midgp.animate.next_to(vg[midnumber][0].get_center(),DOWN*11),
			)
			midgp[1] = midsintltx2.scale(0.8).copy()
			# print("after first copy:",midgp[1])
			self.play(
			    Codes.code[9].animate.set_opacity(0.3),
				midgp[1].animate.next_to(midgp[0].get_center(),DOWN*0),
			)
			self.wait(0.5)
			self.play(
				FadeOut(midsintltx2)
			)
			curvearrow = CurvedArrow(start_point=midgp[0].get_center(),end_point=vg[midnumber][2].get_center())
			self.play(
				Create(curvearrow)
			)
			self.play(
				FadeOut(curvearrow),
				vg[midnumber][0].animate.set_fill("Maroon",0.5),
				keygp[0].animate.set_fill("BLUE",0.5),
			    Codes.code[10].animate.set_opacity(1),
			)
			self.play(
			    Codes.code[10].animate.set_opacity(0.3),
            )
			if(key.number == vg[midnumber][1].number):
				self.play(
					vg[midnumber][0].animate.set_fill("GREEN",0.5),
					Codes.code[11].animate.set_opacity(1),
				)
				self.play(
					Write(foundindex),
					Codes.code[11].animate.set_opacity(0.3),
                )
				self.play(
					Codes.code[12].animate.set_opacity(1),
					Write(index),
                )
				self.play(
					Codes.code[12].animate.set_opacity(0.3),
					midgp[1].copy().animate.next_to(index, RIGHT*1)
                )
				fboolgp[1] = Text("true").scale(0.4)
				self.play(
					Codes.code[13].animate.set_opacity(1),
					Write(fboolgp[1].next_to(fboolgp[0].get_center(), DOWN*0))
					# fboolgp[1].animate.next_to(fboolgp[0].get_center(), DOWN*0),
                )
				self.play(
					Codes.code[13].animate.set_opacity(0.3),
					Codes.code[14].animate.set_opacity(1),
                )
				self.play(
					Codes.code[14].animate.set_opacity(0.3),
                )
				break
			else:
				self.play(
					vg[midnumber][0].animate.set_fill("Maroon",0),
					keygp[0].animate.set_fill("BLUE",0),
					Codes.code[16].animate.set_opacity(1),
				)
				self.play(
					Codes.code[16].animate.set_opacity(0.3),
					Codes.code[17].animate.set_opacity(1),
				)
				self.play(
					Codes.code[17].animate.set_opacity(0.3),
				)	
				if(key.number > vg[midnumber][1].number):
					self.play(
						Codes.code[18].animate.set_opacity(1),
						startgp.animate.next_to(vg[midnumber+1][0].get_center(),DOWN*5)
					)
					# startgp[1] = vg[mid.number+1][2].copy()
					# startgptest = midgp[1].copy()
					startgp[1]= Integer(midgp[1].number+1).scale(0.8).next_to(midgp[0].get_center(),DOWN*0)
					# self.play(
						# Transform(
						# 	startgptest,startgp[1]
						# ),
					# )
					self.play(
						startgp[1].animate.next_to(startgp[0].get_center(),DOWN*0),
						Codes.code[18].animate.set_opacity(0.3),
					)
				else:
					self.play(
					    Codes.code[20].animate.set_opacity(1),
					)
					self.play(
					    Codes.code[20].animate.set_opacity(0.3),
					)
					end = midnumber
					self.play(
					    Codes.code[21].animate.set_opacity(1),
						endgp.animate.next_to(vg[midnumber][0].get_center(),DOWN*5)
					)
					# endgp[1] = vg[mid.number][2].copy()
					# print("before:",endgp[1])
					endgp[1] = midgp[1].copy()
					# print("after:",endgp[1])
					self.play(
					    Codes.code[21].animate.set_opacity(0.3),
						endgp[1].animate.next_to(endgp[0].get_center(),DOWN*0)
					)
			self.remove(midcal)

		self.play(
			Codes.code[25].animate.set_opacity(1),
		)
		self.play(
			Codes.code[25].animate.set_opacity(0.3),
		)
		self.wait(3)