from manim import *
from math import sqrt,acos
def cross_prd(inits=[0.0,0.0,1.0],change=[1.0,0.0,0.0]):
		i = inits[1]*change[2]- inits[2]*change[1]
		j = -1*(inits[0]*change[2]- inits[2]*change[0])
		k = inits[0]*change[1]- inits[1]*change[0]
		# print(f"x:{i},y:{j},z:{k}")
		return np.array((i,j,k))

def dot_prod(inits=[0.0,0.0,1.0],change=[1.0,0.0,0.0]):
	val = inits[0]*change[0]+inits[1]*change[1]+inits[2]*change[2]
	val1 = sqrt(inits[0]*inits[0]+inits[1]*inits[1]+inits[2]*inits[2])
	val2 = sqrt(change[0]*change[0]+change[1]*change[1]+change[2]*change[2])
	fin = val/(val1*val2)
	f = acos(fin)
	return f

def toOrient(Mobject,init,vector,perpend=False):
   if(perpend==False):
		  Mobject.rotate(90*DEGREES,[vector[0],vector[1],vector[2]])
		  print("Perp = FALSE")
   else:
		  Mobject.rotate(dot_prod(inits=init,change=vector), cross_prd(inits=init,change=vector))
		  # print("Perp = TRUE")
   return Mobject


class Seeing_the_change(ThreeDScene):
	"""docstring for observing the change"""
	def construct(self):
		axes = ThreeDAxes()
		dot = Dot(point=[2,0,1],color=RED)
		arrow1 = Arrow3D(start=[0,0,0],end=[2,0,1],color=GOLD)
		dir1 = Arrow3D(start=[0,0,0],end=[1,1,1],color=WHITE)
		dir2 = Arrow3D(start=[0,0,0],end=[-1,-1,-1],color=YELLOW)
		circle1 = Circle(radius=2,color=BLUE)
		circle2 = Circle(radius=1,color=GOLD)
		
		self.set_camera_orientation(phi=75*DEGREES, theta=0*DEGREES)
		self.add(axes)
		
		#write here
		self.add(dir1,dir2)
		self.play(GrowFromCenter(VGroup(circle1,circle2)))
		circle1_1 = toOrient(circle1,[0,0,1],[1,1,1],perpend=True)
		circle2_1 = toOrient(circle2,[0,0,1],[-1,-1,-1],perpend=True)
		self.play(Transform(circle1,circle1_1),run_time=1)
		self.play(Transform(circle2,circle2_1),run_time=1)
		self.play(Transform(circle1,circle1.shift([1,1,1])),Transform(circle2,circle2.shift([-1,-1,-1])),run_time=1)
		self.play(MoveAlongPath(dot,circle1), run_time=2, rate_func=linear)
		self.wait()

