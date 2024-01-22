from manim import *
from math import sqrt,acos
def cross_prd(inits=[0.0,0.0,1.0],change=[1.0,0.0,0.0]):
	i = inits[1]*change[2]- inits[2]*change[1]
	j = -1*(inits[0]*change[2]- inits[2]*change[0])
	k = inits[0]*change[1]- inits[1]*change[0]
	# print(f"x:{i},y:{j},z:{k}")
	return np.round(np.array((i,j,k)),decimals = 2)

def dot_prod(inits=[0.0,0.0,1.0],change=[1.0,0.0,0.0]):
	val = inits[0]*change[0]+inits[1]*change[1]+inits[2]*change[2]
	val1 = sqrt(inits[0]*inits[0]+inits[1]*inits[1]+inits[2]*inits[2])
	val2 = sqrt(change[0]*change[0]+change[1]*change[1]+change[2]*change[2])
	fin = np.round((val/(val1*val2)), decimals = 2)
	f = np.round(acos(fin), decimals =2)
	return np.round(f, decimals = 2)

def toOrient(Mobject,init,vector,perpend=False):
   if(perpend==False):
		  Mobject.rotate(90*DEGREES,[vector[0],vector[1],vector[2]])
		  print("Perp = FALSE")
   else:
		  Mobject.rotate(dot_prod(inits=init,change=vector), cross_prd(inits=init,change=vector))
		  # print("Perp = TRUE")
   return Mobject


class testing_with_angled_orbits(ThreeDScene):
	"""docstring for testing_with_angled_orbits"""
	def construct(self):
		axes = ThreeDAxes()
		dot = Dot(point=[2,0,1],color=RED)
		# dot1 = Dot3D(point=axes.coords_to_point(2,0,1),color=GOLD)
		vector1 = Arrow(start=[0,0,0],end=[1,1,1],buff=0,color=BLUE)
		arrow1 = Arrow3D(start=[0,0,0],end=[2,0,1],color=GOLD)
		dir1 = Arrow3D(start=[0,0,0],end=[1,1,1],color=WHITE)
		circle1 = Circle(radius=2,color=BLUE)
		circle2 = Circle(radius=1,color=GOLD)
		
		self.set_camera_orientation(phi=0*DEGREES, theta=0*DEGREES)
		self.add(axes)
		# circle1 = toOrient(circle1,[1,1,1],perpend=True)
		# self.begin_ambient_camera_rotation(rate=0.5)
		
		#write here
		# self.add(dir1)
		self.play(GrowFromCenter(circle1))
		# self.play(Transform(circle1,circle1.shift([1,1,1])),run_time=1)
		self.add(arrow1,circle2)

		def arrow_updates(x):
			#print("arrow_end_point",x.get_end()),
			#x.become(Arrow3D(start=[0,0,0],end=np.round(dot.get_center(),decimals = 2),color=YELLOW))
			print("inside arrow update dot_end_point",np.round(dot.get_center(),decimals = 2))

		def circle2_updates(y):
			y1 = toOrient(circle2,[0,0,1],np.round(dot.get_center(),decimals = 2),perpend=True)
			y.become(y1)
			# print("circle_end_point",y.normal_vector),
			# print("circle_end_point",y1.normal_vector),
			#print("inside circle update dot_end_point",dot.get_center())
			#print("arrow_end_point",arrow1.get_end()),

		# arrow1.add_updater(arrow_updates)
		circle2.add_updater(circle2_updates)
	#	self.play(Transform(circle1,circle1_1),run_time=1)
	#	self.play(Transform(circle2,circle2_1),run_time=1)
		#self.play(Transform(circle1,circle1.shift([2,0,0])),Transform(circle2,circle2.shift([1.96,0.42,0])),run_time=1)
		self.play(MoveAlongPath(dot,circle1), run_time=2, rate_func=linear)
		self.wait()
		# self.stop_ambient_camera_rotation()

