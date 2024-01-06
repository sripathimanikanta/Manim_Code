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

def label(vector):
	array = vector.get_end()
	return Text(f'{round(array[0],2)},{round(array[1],2)},{array[2]}').scale(0.5).next_to(vector.get_end(),DOWN)

class Precession_Angular_momentum(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		vector1 = Arrow3D(start=[0,0,0],end=[0,0,1],color=BLUE)
		# label_1 = label(vector1)
		
		labx = axes.get_x_axis_label(Tex("$x$-label"))
		laby = axes.get_y_axis_label(Tex("$y$-label"))
		labz = axes.get_z_axis_label(Tex("$z$-label"))
		circle1 = Circle(radius=2,color=BLUE).shift([0,0,1])
		# circle1_y = circle1.copy()

		self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)

		self.add(axes,labx, laby, labz)
		self.wait()
		# circle1_y = toOrient(circle1_y,[0,1,0],perpend=True)
		self.begin_ambient_camera_rotation(rate=0.5)
		self.add(circle1,vector1)
		self.wait()
		self.play(MoveAlongPath(vector.get_end(),))

		self.stop_ambient_camera_rotation()