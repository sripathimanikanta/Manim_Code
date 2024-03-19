from manim import *
import math

class HorizontalFalsiMethod(Scene):
    def construct(self):
        def func(x):
            print(4*((2.71828)**(-x))*math.sin(x)-1)
            return (4*((2.71828)**(-x))*math.sin(x)-1)

        def reg_falsi(a,b):
            print("x",(a*func(b) - b*func(a))/(func(b)-func(a)))
            return (a*func(b) - b*func(a))/(func(b)-func(a))

        ax1 = NumberLine(
            x_range=[-0.01,0.51,0.1],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        ).move_to(UP*2)
        ax2 = NumberLine(
            x_range=[-1,0.17,0.1],
            length=10,
            color=RED,
            include_numbers=True,
            label_direction=UP,
        ).move_to(DOWN*2)
        function = MathTex("4e^{-x}\sin(x)-1")
        reg_falsi_func = MathTex("{{a}} {{f(b)}}-{{b}}{{f(a)}} {{\over}} {{f(b)}}-{{f(a)}}").move_to(UP*3)

        pa1,pa2 = 0,0.5
        pa3 = reg_falsi(pa1,pa2)
        a1 = Dot(ax1.number_to_point(pa1),color=RED_C)
        laba1 = DecimalNumber(pa1).scale(0.8).next_to(a1, DOWN*1)
        b1 = Dot(ax1.number_to_point(pa2),color=RED_C)
        labb1 = DecimalNumber(pa2).scale(0.8).next_to(b1, DOWN*1)
        c1 = Dot(ax1.number_to_point(pa3),color=YELLOW_C)
        labc1 = DecimalNumber(pa3,num_decimal_places=4).scale(0.8).next_to(c1, DOWN*1)

        pfa1 = func(pa1)
        pfb1 = func(pa2)
        pfc1 = func(pa3)
        fa1 = Dot(ax2.number_to_point(pfa1),color=BLUE_A)
        labfa1 = DecimalNumber(pfa1).scale(0.8).next_to(fa1, DOWN*1)
        fb1 = Dot(ax2.number_to_point(func(0.5)),color=BLUE_B)
        labfb1 = DecimalNumber(pfb1).scale(0.8).next_to(fb1, DOWN*1)
        fc1 = Dot(ax2.number_to_point(func(reg_falsi(0,0.5))),color=BLUE_C)
        labfc1 = DecimalNumber(pfc1).scale(0.8).next_to(fc1, DOWN*1)
        
        arrow1 = Arrow(a1,fa1)
        arrow2 = Arrow(b1,fb1)
        arrow3 = Arrow(c1,fc1)
        self.play(
            Write(ax1),
            Write(ax2)
            )
        self.play(
            Write(VGroup(a1, laba1))
        )
        self.play(
            Write(function),
        )
        self.play(
            Create(arrow1)
        )
        self.play(
            Write(VGroup(fa1, labfa1 ))
        )
        self.play(
            Write(reg_falsi_func)
        )

        self.play(
            Write(VGroup(b1, labb1 ))
        )
        self.play(
            Create(arrow2)
        )
        self.play(
            Write(VGroup(fb1, labfb1 ))
        )
        
        self.play(
            Write(VGroup(c1, labc1 ))
        )
        self.play(
            Create(arrow3)
        )
        self.play(
            Write(VGroup(fc1, labfc1 ))
        )
        self.play(
            Write(VGroup(fa1, fb1, fc1))
        )