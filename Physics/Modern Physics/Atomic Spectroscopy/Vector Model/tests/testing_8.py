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
   dt = 0;
   values_x_array=np.array([0])
   values_y_array=np.array([0])
   values_z_array=np.array([1])
   realtracker=0
   def construct(self):
      axes = ThreeDAxes()
      dot = Dot(point=[2,0,0],color=RED)
      arrow1 = Arrow3D(start=[0,0,0],end=[2,0,1],color=GOLD)
      dir1 = Arrow3D(start=[0,0,0],end=[2,0,0],color=WHITE)
      dir2 = Arrow3D(start=[0,0,0],end=[1.96,0.42,0],color=YELLOW)
      dir3 = Arrow3D(start=[0,0,0],end=[1.83,0.81,0],color=RED)
      dir4 = Arrow3D(start=[0,0,0],end=[1.62,1.18,0],color=BLUE)
      circle0 = Circle(radius=2,color=RED,arc_center=[0,0,1], normal_vector=[1,0,0])
      circle1 = Circle(radius=0.5,color=BLUE,normal_vector=[0,0,1])
      values_x = ValueTracker(dot.get_center()[0])
      values_y = ValueTracker(dot.get_center()[1])
      values_z = ValueTracker(dot.get_center()[2])
      pos_x = DecimalNumber(dot.get_center()[0])
      pos_y = DecimalNumber(dot.get_center()[1])
      counter = DecimalNumber(0)
      self.set_camera_orientation(phi=75*DEGREES, theta=-75*DEGREES)
      self.add(axes)
      
      #write here
      self.add(dir1,dir2,dir3,dir4,counter,pos_x,pos_y,values_x,values_y,values_z)
      self.play(GrowFromCenter(VGroup(circle0,circle1)))

      
      def measures_x(d):
         d.set_value(np.round(dot.get_center()[0],decimals=2))
         print("values_x",d.get_value())
         self.values_x_array = np.append(self.values_x_array,d.get_value())
      
      def measures_y(d):
         d.set_value(np.round(dot.get_center()[1],decimals=2))
         print("values_y",d.get_value())
         self.values_y_array = np.append(self.values_y_array,d.get_value())

      def measures_z(d):
         d.set_value(np.round(dot.get_center()[2],decimals=2))
         print("values_z",d.get_value())
         self.values_z_array = np.append(self.values_z_array,d.get_value())

      counter.add_updater(lambda d: d.next_to(dot, RIGHT))
      counter.add_updater(lambda d: d.increment_value())
      values_x.add_updater(measures_x)
      values_y.add_updater(measures_y)
      values_z.add_updater(measures_z)

      self.play(MoveAlongPath(dot,circle0), run_time=2, rate_func=linear)
      self.wait()
      print("values_x_array",self.values_x_array)
      print("values_y_array",self.values_y_array)
      print("values_z_array",self.values_z_array)
      
      def circle_change(y):
         y.become(toOrient(y,[self.values_x_array[self.realtracker],self.values_y_array[self.realtracker],self.values_z_array[self.realtracker]],[self.values_x_array[self.realtracker+1],self.values_y_array[self.realtracker+1],self.values_z_array[self.realtracker+1]],perpend=True))
         self.realtracker=self.realtracker+1
      
      circle1.add_updater(circle_change)

      self.play(MoveAlongPath(dot,circle0), run_time=2, rate_func=linear)
      self.wait()
