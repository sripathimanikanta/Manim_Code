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
      # circle2 = Circle(radius=0.5,color=GOLD,normal_vector=[1,0,0])
      # circle3 = Circle(radius=0.5,color=YELLOW,normal_vector=[1,0,0])
      # circle4 = Circle(radius=0.5,color=RED,normal_vector=[1,0,0])
      count = np.array(
         [
            np.array([2,0,0]),
            np.array([1.96,0.42,0]),
            np.array([1.83,0.81,0]),
            np.array([1.62,1.18,0])
         ])
      pos_x = DecimalNumber(dot.get_center()[0])
      pos_y = DecimalNumber(dot.get_center()[1])
      counter = DecimalNumber(0)
      self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES)
      self.add(axes)
      
      #write here
      self.add(dir1,dir2,dir3,dir4,counter,pos_x,pos_y)
      self.play(GrowFromCenter(VGroup(circle0,circle1)))
      # def static_vars(**kwargs):
      #    def decorate(func):
      #       for k in kwargs:
      #          setattr(func, k, kwargs[k])
      #       return func
      #    return decorate
      
      # @static_vars(counter=0)

      def circle_change(y):
         # counter += 1
         # print(counter)
         y.become(toOrient(y,[0,0,1],np.round(dot.get_center(),decimals=2),perpend=True))

      circle1.add_updater(circle_change)
      counter.add_updater(lambda d: d.next_to(dot, RIGHT))
      counter.add_updater(lambda d: d.increment_value())

      pos_x.add_updater(lambda d: d.next_to(counter, RIGHT))
      pos_x.add_updater(lambda d: d.set_value(dot.get_center()[0]))

      pos_y.add_updater(lambda d: d.next_to(pos_x, RIGHT))
      pos_y.add_updater(lambda d: d.set_value(dot.get_center()[1]))

      # circle3_1 = toOrient(circle3,[0,0,1],[1.83,0.81,0],perpend=True)
      # circle4_1 = toOrient(circle4,[0,0,1],[1.62,1.18,0],perpend=True)
#      circle1_1 = toOrient(circle1,[0,0,1],[2,0,0],perpend=True)
#      self.play(Transform(circle1,circle1_1),run_time=1)
#      circle2_1 = toOrient(circle1_1,[2,0,0],[1.96,0.42,0],perpend=True)
#      self.play(Transform(circle1_1,circle2_1),run_time=1)

      # circle1_1 = Circle(radius=0.5,color=GOLD,normal_vector = np.array([2,0,0]))
      #print("normal vector of circle1_1",circle1_1.normal_vector)
      #self.play(Transform(circle1,circle1_1),run_time=1)
      # circle2_1 = Circle(radius=0.5,color=YELLOW,normal_vector = np.array([1.96,0.42,0]))
      #print("normal vector of circle2_1",circle2_1.normal_vector)
      #self.play(Transform(circle1_1,circle2_1),run_time=1)
      # self.add(circle1_1, circle2_1)
      # self.play(Transform(circle1,circle1.shift([2,0,0])),
      #  Transform(circle2,circle2.shift([1.96,0.42,0])),
      #  Transform(circle3,circle3.shift([1.83,0.81,0])),
      #  Transform(circle4,circle4.shift([1.62,1.18,0])),   
      # run_time=1)
      self.play(MoveAlongPath(dot,circle0), run_time=2, rate_func=linear)
      self.wait()

