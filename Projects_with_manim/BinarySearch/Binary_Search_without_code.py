from manim import *

class BinarySearchAnime(Scene):
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
		self.play(Write(gp))

		# self.play(
		# 	vg[5][0].animate.set_fill("RED",opacity=0.5)
		# 	)
		# key = 8
		
		keySquare = Square(side_length=sl).scale(0.8).next_to(vg[1][0].get_center(), DOWN*17)
		key = Integer(3).scale(0.8).next_to(keySquare.get_center(), DOWN*0)
		keytext = Text("key").scale(0.5).next_to(keySquare, DOWN)
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

		fboolSquare = Square(side_length=sl).scale(0.8).next_to(vg[1][0].get_center(), LEFT*8+DOWN*5)
		fboool = Text("false").scale(0.4).next_to(fboolSquare.get_center(), DOWN*0)
		fbooltext = Text("fbool").scale(0.8).next_to(fboolSquare, LEFT)
		fboolgp = VGroup(fboolSquare, fboool, fbooltext)
		# self.add(keygp, keytext)

		# found = Text("Found the key").next_to(keySquare, RIGHT)
		index = Text("Found key, It's at the index:").scale(0.5).next_to(keySquare, RIGHT*2)
		notfound = Text("Not Found!!!").next_to(keySquare, RIGHT*2)
		fbool = False

		self.play(
			Write(startgp[0]),
			Write(startgp[2])
		)
		startgp[1] = vg[start.number][2] .copy()
		self.play(
				startgp[1].animate.next_to(startgp[0].get_center(),DOWN*0)
		)
		self.play(
			Write(endgp[0]),
			Write(endgp[2])
		)
		endgp[1] = vg[end.number][2] .copy()
		self.play(
				endgp[1].animate.next_to(endgp[0].get_center(),DOWN*0)
		)		
		self.play(
			Write(midgp[0]),
			Write(midgp[2])
		)
		midgp[1] = vg[mid.number][2] .copy()
		self.play(
				midgp[1].animate.next_to(midgp[0].get_center(),DOWN*0)
		)		
		self.play(
			Write(keygp)
		)
		# iter1 = Text(f"{i+1} Iteration", t2c={'[:1]':'#5CD0B3'}).next_to(vg, RIGHT)
		# self.add(iter1)
		text = MathTex("( {{start}} + {{end}} ) \over 2")
		midcal = VGroup(text)
		# print(midcal)
		# print(midcal[0])
		for x in range(0,3):
			text = MathTex("( {{start}} + {{end}} ) \over 2")
			midcal = VGroup(text)
			self.play(
				Write(midcal[0].next_to(vg, RIGHT*3+DOWN*1))
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
			midsintltx2 = MathTex(f"={midsint}").next_to(tempmidltx,RIGHT*0)
			self.play(
				ReplacementTransform(
					midsintltx, midsintltx2
				),
				run_time=1
			)
			self.wait(0.5)
			mid.number = int((endgp[1].number + startgp[1].number)/2)
			self.play(
				midgp.animate.next_to(vg[mid.number][0].get_center(),DOWN*11),
			)
			midgp[1] = midsintltx2[0][1].scale(0.8).copy()
			self.play(
				midgp[1].animate.next_to(midgp[0].get_center(),DOWN*0),
			)
			self.wait(0.5)
			self.play(
				FadeOut(midsintltx2)
			)
			curvearrow = CurvedArrow(start_point=midgp[0].get_center(),end_point=vg[mid.number][2].get_center())
			self.play(
				Create(curvearrow)
			)
			self.play(
				FadeOut(curvearrow),
				vg[mid.number][0].animate.set_fill("Maroon",0.5),
				keygp[0].animate.set_fill("BLUE",0.5)
			)
			if(key.number == vg[mid.number][1].number):
				self.play(
					vg[mid.number][0].animate.set_fill("GREEN",0.5),
				)
				self.play(
					Write(index),
                )
				self.play(
					midgp[1].copy().animate.next_to(index, RIGHT*1)
                )
				break
			else:
				if(key.number > vg[mid.number][1].number):
					start.number = mid.number+1
					self.play(
						startgp.animate.next_to(vg[mid.number+1][0].get_center(),DOWN*5)
					)
					startgp[1] = vg[mid.number+1][2].copy()
					self.play(
						startgp[1].animate.next_to(startgp[0].get_center(),DOWN*0)
					)
				else:
					end = mid.number
					self.play(
						endgp.animate.next_to(vg[mid.number][0].get_center(),DOWN*5)
					)
					endgp[1] = vg[mid.number][2].copy()
					self.play(
						endgp[1].animate.next_to(endgp[0].get_center(),DOWN*0)
					)
			self.play(
				vg[mid.number][0].animate.set_fill("Maroon",0),
				keygp[0].animate.set_fill("BLUE",0),
			)
			self.remove(midcal)

		self.wait(3)