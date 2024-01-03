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


class CircleInDifferentOrientation3(ThreeDScene):
       def construct(self):
              # print(90*DEGREES)
              axes = ThreeDAxes()
              vector3 = Vector([1,1,0],color=GOLD)
              label_3 = vector3.coordinate_label()
              labx = axes.get_x_axis_label(Tex("$x$-label"))
              laby = axes.get_y_axis_label(Tex("$y$-label"))
              labz = axes.get_z_axis_label(Tex("$z$-label"))
              circle3 = Circle(radius=2,color=GOLD)
              circle3_x_y = Circle(radius=3,color=RED)
              self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)

              self.add(axes,labx, laby, labz)

              #Circle 5 => 6 Transformation
              # self.begin_ambient_camera_rotation(rate=0.5)
              # self.play(Transform(circle3,circle3_x_y),run_time=2)
              self.play(Write(circle3))
              circle3_x_y = toOrient(circle3_x_y,[1,1,0],perpend=True)
              self.play(Write(circle3_x_y))
              # print(circle3_x_y.get_normal_vector())
              # self.add(circle3_x_y.get_normal_vector().coordinate_label())
              self.play(GrowFromCenter(vector3))
              self.add(label_3)
              # self.wait()
              # self.stop_ambient_camera_rotation()

              # self.move_camera(phi=75*DEGREES, theta=360*DEGREES)
              # self.wait()
              # self.move_camera(phi=0*DEGREES, theta=360*DEGREES)
              self.wait()

# class A:
#        def __init__(self,normal_vector= [0,0,1],**kwags):
#               self.normal_vector = normal_vector

# class B(A):
#        def __init__(self,color="red",**kwags):
#               self.color=color
#               super().__init__(**kwags)
#        def __str__(self):
#               return f"color={self.color}, normal_vector={self.normal_vector}"

# b1 = B(color="yellow",normal_vector=[0,1,1])
# print(b1)



