from manim import *
import math
config.frame_width = 16
config.frame_height =9 
config.pixel_width = 1920 
config.pixel_height = 1080

class Ball(Dot):
    def __init__(self,point=ORIGIN,color=WHITE,radius=1,**kwargs):
        Dot.__init__(self, point=point,color=color,radius=radius,**kwargs)
        # self.ivel = 0
        # self.fvel = 0
        self.direction = 1
        
class BallTestLine(MovingCameraScene):
    def construct(self):
        def BallUpdater(m,dt):
        #    m.fvel = m.direction*5*dt
           m.shift(m.direction*DOWN*5*(dt**dt))
           y = (math.sqrt((rad**2)-((ball.get_center()[0]+(2.5*ball.radius))**2)))
        #    print(y)
           y_dw = -y
           y_up = y
           if m.get_center()[1] <  y_dw or m.get_center()[1] > y_up:
               m.direction = -m.direction

        # def TangentUpdater(m):
        #    MoveAlongPath(m,)
        rad=25
        Circ1 = Circle(radius=rad,color="RED",stroke_width=30)
        L = Line(start=[-5,0,0],end=[5,0,0],color=WHITE,stroke_width=10)
        self.camera.frame.set(height=Circ1.height+10)
        # Dot0 = Dot(radius=0.1,color="WHITE").shift(UP*0)
        ball = Ball(point=[20,0,0])
        self.add(Circ1,ball)
        ball.add_updater(BallUpdater)
        # # self.add(L)
        # # L.add_updater(TangentUpdater)
        # Dot1 = Dot(radius=0.1,color="BLUE").shift(RIGHT*rad)
        # Dot2 = Dot(radius=0.1,color="BLUE").shift(LEFT*rad)
        # Dot3 = Dot(radius=0.1,color="BLUE").shift(UP*rad)
        # Dot4 = Dot(radius=0.1,color="BLUE").shift(DOWN*rad)
        # self.play(self.camera.frame.animate.set(height=Circ1.height))
        # self.play(
            # Write(Circ1),
            # Create(VGroup(*[Dot1,Dot2,Dot3,Dot4]))
        # )
        self.play(
            MoveAlongPath(L,Circ1), 
            rate_func=linear,
           run_time=3 
        )
        self.wait(3)
