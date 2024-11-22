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
        rad=25
        Circ1 = Circle(radius=rad,color="RED",stroke_width=30)
        L = Line(start=[-5,0,0],end=[5,0,0],color=WHITE,stroke_width=10)
        self.camera.frame.set(height=Circ1.height+10)
        ball = Ball(point=[10,0,0])
        self.play(
            Create(ball),
        )
        self.play(
            GrowFromCenter(Circ1)
        )
        l=TangentLine(vmob=Circ1,alpha=0.8,color="WHITE")
        l.scale(20/l.get_length())
        Dot1 = Dot(l.get_center(),radius=1,color="BLUE",stroke_width=10)
        self.play(
            Create(l),
            Write(Dot1)
            )
        self.wait()
