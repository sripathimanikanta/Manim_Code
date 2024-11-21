from manim import *
config.frame_width = 16
config.frame_height =9 
config.pixel_width = 1920 
config.pixel_height = 1080

class BallTest11(MovingCameraScene):
    def construct(self):
        rad = 25
        x = []
        y = []
        d = -1 
        def reverser1(mobject,dt):
            a = (dt**dt)*0.5
            mobject.shift(UP*a)

        def reverser(mobject,dt):
            # t=0.0
            # v=0
            # dts = 0.000001
            # a  = (t**t)*0.5
            # if v==0:
            #     print("HELLO V", v)
            #     direc = DOWN
            # elif v!=0:
            #     print("! V")
            #     if mobject.get_center()[1] <= -3:
            #         direc= UP
            # # print(direc)
            # print(mobject.get_center()[1],t,a)
            # direction = direc 
            a = (dt**dt)*0.5
            mobject.shift(DOWN*a)
            if mobject.get_center()[1] <= -3:
                mobject.shift(*a)
            # t = t+ dts
            # v = v+0.5*t
            # if mobject.get_center()[1] <=  -3 and v!=0:
            #     direction = UP
            #     mobject.shift(direction*a)
            # elif mobject.get_center()[1] > -3 and v!=0:
            #     direction = UP
            #     mobject.shift(direction*a)
            # elif mobject.get_center()[1] > -3 and v==0:
            #     direction = DOWN
            #     mobject.shift(direction*a)
            # if mobject.get_center()[1]!= 0 and u != 0:
            # if mobject.get_center()[1] < -rad and mobject.get_center()[1]!=0:
            #     direction = UP 
            # mobject.shift(direction*a)
                # x.append([mobject.get_center()[1]])

        Circ1 = Circle(radius=rad,color="RED",stroke_width=30)
        Dot0 = Dot(radius=1,color="WHITE").shift(UP*0)
        self.camera.frame.set(height=Circ1.height+10)
        # self.play( Create(Dot0))
        self.add(Dot0,Circ1)
        self.play(
            Dot0.animate.shift(DOWN*(rad+5))
        )
        self.wait(3)