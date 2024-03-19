from manim import *
import math 

class FlasiMethodAnime(Scene):
    def construct(self):
        def func(x):
            return (4*((2.71828)**(-x))*math.sin(x)-1)
        
        def reg_falsi(a,b):
            print("x",(a*func(b) - b*func(a))/(func(b)-func(a)))
            return (a*func(b) - b*func(a))/(func(b)-func(a))
        
        ax1 = Axes(
            x_range=[0.39,0.51,0.01],
            y_range=[-0.1,0.2,0.01],
            axis_config={
                "color": GREEN
            },
            x_axis_config={
                "numbers_to_include":np.arange(0.4,0.5,0.01)
            },
            y_axis_config={
                "numbers_to_include":np.arange(-0.1,0.2,0.01)
            }
        )

        ax2 = Axes(
            x_range=[0.37,0.51,0.01],
            y_range=[-1.0,0.17,0.01],
            axis_config={
                "color": GREEN
            },
            x_axis_config={
                "numbers_to_include":np.arange(0.37,0.5,0.01)
            },
            y_axis_config={
                "numbers_to_include":np.arange(-1.0,0.17,0.01),
                "font_size" : 24
            },
            tips=False
        ).add_coordinates()

        a1 = 0
        b1 = 0.5
        fa1 = func(a1)
        print(fa1)
        fb1 = func(b1)
        print(fb1)
        dot1 = Dot(ax2.coords_to_point(a1, fa1),color=YELLOW_A)
        dot2 = Dot(ax2.coords_to_point(b1, fb1),color=YELLOW_B)
        self.play(Create(VGroup(dot1,dot2)))

        c1 = reg_falsi(a1,b1)
        fc1 = func(c1)
        dot3 = Dot(ax2.coords_to_point(c1, fc1),color=YELLOW_C)
        self.play(Create(dot3))

        a2 = 0 
        b2 = c1
        fa2 = func(a2)
        print(fa2)
        fb2 = func(b2)
        print(fb2)
        dot4 = Dot(ax2.coords_to_point(a2, fa2),color=GREEN_A)
        dot5 = Dot(ax2.coords_to_point(b2, fb2),color=GREEN_B)
        self.play(Create(VGroup(dot4,dot5)))

        c2 = reg_falsi(a2,b2)
        fc2 = func(c2)
        dot6 = Dot(ax2.coords_to_point(c2, fc2),color=GREEN_C)
        self.play(Create(dot6))

        a3 = 0 
        b3 = c2
        fa3 = func(a3)
        print(fa3)
        fb3 = func(b3)
        print(fb3)
        dot7 = Dot(ax2.coords_to_point(a3, fa3),color=RED_A)
        dot8 = Dot(ax2.coords_to_point(b3, fb3),color=RED_B)
        self.play(Create(VGroup(dot7,dot8)))

        c3 = reg_falsi(a3,b3)
        fc3 = func(c3)
        dot9 = Dot(ax2.coords_to_point(c3, fc3),color=RED_C)
        self.play(Create(dot9))

        numbplane = NumberPlane()
        # self.add(numbplane)
        self.play(Write(ax2))