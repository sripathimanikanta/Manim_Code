from manim import *
from math import sqrt,acos
def cross_prd(inits=[0,0,1],change=[1,0,0]):
		i = inits[1]*change[2]- inits[2]*change[1]
		j = -1*(inits[0]*change[2]- inits[2]*change[0])
		k = inits[0]*change[1]- inits[1]*change[0]
		# print(f"x:{i},y:{j},z:{k}")
		return np.array((i,j,k))

def dot_prod(inits=[0,0,1],change=[1,0,0]):
	val = inits[0]*change[0]+inits[1]*change[1]+inits[2]*change[2]
	val1 = sqrt(inits[0]*inits[0]+inits[1]*inits[1]+inits[2]*inits[2])
	val2 = sqrt(change[0]*change[0]+change[1]*change[1]+change[2]*change[2])
	fin = val/(val1*val2)
	f = acos(fin)
	return f

def toOrient(Mobject,vector,perpend=False):
   if(perpend==False):
		  Mobject.rotate(90*DEGREES,[vector[0],vector[1],vector[2]])
		  print("Perp = FALSE")
   else:
		  Mobject.rotate(dot_prod(change=vector), cross_prd(change=vector))
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
		
		self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)
		self.add(axes)
		circle1 = toOrient(circle1,[1,1,1],perpend=True)
		self.begin_ambient_camera_rotation(rate=0.5)
		
		#write here
		self.add(dir1)
		self.play(GrowFromCenter(circle1))
		self.play(Transform(circle1,circle1.shift([1,1,1])),run_time=1)
		self.add(arrow1)
		arrow1.add_updater(
				lambda x: x.become(Arrow3D(start=[0,0,0],end=dot.get_center(),color=YELLOW))
			)
		self.play(MoveAlongPath(dot,circle1), run_time=2, rate_func=linear)
		self.wait()
		self.stop_ambient_camera_rotation()

