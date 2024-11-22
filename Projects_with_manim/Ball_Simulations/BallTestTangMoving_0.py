from manim import *
import math
config.frame_width = 16 
config.frame_height =9 
config.pixel_width = 1920
config.pixel_height = 1080

class Ball(Dot):
    def __init__(self,point=ORIGIN,color=WHITE,radius=1,**kwargs):
        Dot.__init__(self, point=point,color=color,radius=radius,**kwargs)
        self.direction = 1
        
class Lin(Line):
    def __init__(self,start=LEFT,end=RIGHT,color=BLUE,stroke_width=5,**kwargs):
        Line.__init__(self, start=start,end=end,color=color,stroke_width=stroke_width,**kwargs)
        self.cir = VMobject() 

class TL(TangentLine):
    def __init__(self,vm,al=0.25,leng=1,s_w=5,**kwargs):
        TangentLine.__init__(self,vmob=vm,alpha=al,length=leng,stroke_width=s_w,**kwargs)
        self.t=0

class BallTestEasyTangMoving(MovingCameraScene):
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

        def TangentLineUpdater(m,dt):
            # print(dt)
            if m.t < 1:
                m.t=m.t+(dt*0.1)
                m.become(TL(vm=Circ1,al=m.t,leng=20,s_w=30))
            else:
                m.t = 0
                # m.become(TL(vm=Circ1,al=m.t,leng=20,s_w=30))

        rad=25
        Circ1 = Circle(radius=rad,color="RED",stroke_width=30)
        self.camera.frame.set(height=Circ1.height+10)
        # L = Lin(start=[-5,0,0],end=[5,0,0],color=WHITE,stroke_width=10)
        # L.cir= Circ1
        # Tline = TL(vm=Circ1,al=0.25,leng=20,s_w=30)
        # Dot0 = Dot(radius=0.1,color="WHITE").shift(UP*0)
        ball = Ball(point=[10,0,0])
        self.add(Circ1,ball)
        ball.add_updater(BallUpdater)
        # self.add(L)
        # L.add_updater(TangentUpdater)
        # self.add(Tline)
        # Tline.add_updater(TangentLineUpdater)

        # def doubt(m,dt):
        #         m = m.become(Line(start=Dot1.get_center(),end=Dot2.get_center(),stroke_width=20))
        #         m.scale(20/m.get_length())
                # self.play(m.animate.shift(Circ1.point_from_proportion(prop1+dt)) )

        prop1=0.85
        prop2 = 0.95
        prop3=0.9
        Dot3= Dot(Circ1.point_from_proportion(prop3),color="GREEN",radius=1)
        self.play(Create(Dot3))
        l=TL(vm=Circ1,al=prop3,color="WHITE")
        l.scale(20/l.get_length())
        l.t=prop3
        l.add_updater(TangentLineUpdater)
        Dot3.add_updater(lambda m: m.next_to(l,UP*0))
        self.add(l)
        # self.play(Create(l))
        # lt = TangentLine(vmob=Circ1,alpha=Circ1.proportion_from_point([ball.get_center()[0],math.sqrt(rad**2-ball.get_center()[0]**2),0]))
        # self.add(lt)
        # self.play(
        #     MoveAlongPath(Dot3,Circ1)
        # )

        # x= Circ1.point_from_proportion(prop1)
        # y=Circ1.point_from_proportion(prop2)
        # l=Line(x,y,stroke_width=5)
        # l.scale(20/l.get_length())
        # l.add_updater(doubt)
        # Dot1 = Dot(radius=1,color="BLUE").shift(x)
        # Dot2 = Dot(radius=1,color="RED").shift(y)
        # self.add(Dot1,Dot2,l)
        # animations=[]
        # animations2=[]
        # for x in np.arange(0,1,0.0001):
        #     prop= prop1+x
        #     prop4= prop2-x
        #     # print("x",x)
        #     # print("prop1",prop1)
        #     # x = x/500
        #     # print("after: x",x)
        #     # print("prop1+x",prop)
        #     # print("pfp",Circ1.point_from_proportion(prop1+x))
        #     # print("prop1",prop1)
        #     if prop < prop3:
        #         animations.append(Dot1.animate.move_to(Circ1.point_from_proportion(prop)))
        #     if prop4 > prop3:
        #         animations2.append(Dot2.animate.move_to(Circ1.point_from_proportion(prop4)))
        # self.play(
        #     AnimationGroup(*[animations]),
        #     AnimationGroup(*[animations2]),
        #     lag_ratio=0.2,
        #     run_time=5,
        #     rate_func=linear
        # )
        # # self.play(MoveAlongPath(Dot1,Circ1))
        # # Dot1 = Dot(radius=1,color="BLUE").shift(RIGHT*rad)


        # # self.play(
        #     # Create()
        # # )
        # # Dot2 = Dot(radius=1,color="BLUE").shift(LEFT*rad)
        # # y=Circ1.point_from_proportion(0.2)
        # # Dot3 = Dot(radius=0.1,color="BLUE").shift(UP*rad)
        # # Dot4 = Dot(radius=0.1,color="BLUE").shift(DOWN*rad)
        # # self.play(self.camera.frame.animate.set(height=Circ1.height))
        # # self.play(
        # #     Write(Circ1),
        # #     Create(VGroup(*[Dot1,Dot2,Dot3,Dot4,l]))
        # # )
        # # self.play(Create(Dot1))
        # # self.play(Create(Dot2))
        # # self.play(Create(l))
        # self.play(
        #     MoveAlongPath(l,Circ1), 
        #     rate_func=linear,
        #    run_time=3 
        # )
        self.wait(9)
