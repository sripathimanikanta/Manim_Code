from manim import *
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
        
class BallTest1(MovingCameraScene):
    def construct(self):
        # def BallUpdater(m,dt):
        # #    m.fvel = m.direction*5*dt
        #    m.shift(m.direction*DOWN*5*(dt**dt))
        #    if m.get_center()[1]-m.radius <=  -rad or m.get_center()[1]+m.radius >= rad:
        #        m.direction = -m.direction
        rad=25
        Circ1 = Circle(radius=rad,color="RED",stroke_width=30)
        self.camera.frame.set(height=Circ1.height+10)
        ball = Ball()
        self.add(ball)
        # ball.add_updater(BallUpdater)
        self.play(
            Write(Circ1),
        )
        for _ in range(0,2):
                self.play(
                    ball.animate.move_to([0,-rad,0]),
                    rate_func=linear
                )
                self.play(
                    ball.animate.move_to([0,rad,0]),
                    rate_func=linear
                )

        self.wait(3)
