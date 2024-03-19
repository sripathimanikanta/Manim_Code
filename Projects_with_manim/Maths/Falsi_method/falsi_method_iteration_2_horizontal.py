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
        function = MathTex("{{4e^}}{{-x}}{{\sin(}}{{x}}{{)-1}}")
        reg_falsi_func = MathTex("{{a}}{{f(b)}}-{{b}}{{f(a)}}{{\over}}{{f(b)}}-{{f(a)}}").scale(1.2).move_to(UP*3)
        print("reg", reg_falsi_func)
        print("reg_inside", reg_falsi_func[1])

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
        fa1 = Dot(ax2.number_to_point(pfa1),color=BLUE_C)
        labfa1 = DecimalNumber(pfa1).scale(0.8).next_to(fa1, DOWN*1)
        fb1 = Dot(ax2.number_to_point(func(0.5)),color=BLUE_C)
        labfb1 = DecimalNumber(pfb1,num_decimal_places=4).scale(0.6).next_to(fb1, DOWN*1,aligned_edge=[-1,0,0])
        fc1 = Dot(ax2.number_to_point(func(reg_falsi(0,0.5))),color=GREEN_C)
        labfc1 = DecimalNumber(pfc1,num_decimal_places=4).scale(0.6).next_to(fc1, DOWN*1, aligned_edge=[1,0,0])
        
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
        a11 = laba1.copy().scale(0.7)
        a12 = laba1.copy().scale(0.7)
        self.play(
            Uncreate(function[1]),
            Uncreate(function[3]),
            a11.animate.next_to(function[1].get_center(),DOWN*0),
            a12.animate.next_to(function[3].get_center(),DOWN*0),
        )

        af11 = Text(f"={round(pfa1,4)}").scale(0.8).next_to(function, RIGHT*1)
        self.play(
            Write(af11)
        )
        self.play(
            Transform(af11, labfa1),
            Uncreate(a11),
            Uncreate(a12)
        )
        afunction = MathTex("-x").next_to(function[1].get_center(), DOWN*0)
        a1function = MathTex("x").next_to(function[3].get_center(), DOWN*0)
        self.play(
            Create(afunction),
            Create(a1function)
        )
        self.play(
            Create(arrow1)
        )
        self.play(
            Write(reg_falsi_func)
        )
        self.play(
            Write(VGroup(fa1, labfa1 ))
        )
        reg_falsi_func_a1 = laba1.copy().scale(0.7)
        reg_falsi_func_fa1 = labfa1.copy().scale(0.7)
        reg_falsi_func_fa11 = labfa1.copy().scale(0.7)
        self.play(
            Uncreate(reg_falsi_func[0]),
            Uncreate(reg_falsi_func[4]),
            Uncreate(reg_falsi_func[8]),
            reg_falsi_func_a1.animate.next_to(reg_falsi_func[0], DOWN*0),
            reg_falsi_func_fa1.animate.next_to(reg_falsi_func[4], DOWN*0),
            reg_falsi_func_fa11.animate.next_to(reg_falsi_func[8], DOWN*0),
        )
        
        # console.log()
        self.play(
            Write(VGroup(b1, labb1 ))
        )
        b11 = labb1.copy().scale(0.7)
        b12 = labb1.copy().scale(0.7)
        self.play(
            Uncreate(afunction),
            Uncreate(a1function),
            b11.animate.next_to(function[1].get_center(),DOWN*0),
            b12.animate.next_to(function[3].get_center(),DOWN*0),
        )

        bf11 = Text(f"={round(pfb1,4)}").scale(0.8).next_to(function, RIGHT*1)
        self.play(
            Write(bf11)
        )
        self.play(
            Transform(bf11, labfb1),
            Uncreate(b11),
            Uncreate(b12),
        )
        bfunction = MathTex("-x").next_to(function[1].get_center(), DOWN*0)
        b1function = MathTex("x").next_to(function[3].get_center(), DOWN*0)
        self.play(
            Create(bfunction),
            Create(b1function)
        )
        self.play(
            Create(arrow2)
        )
        self.play(
            Write(VGroup(fb1, labfb1 ))
        )
        reg_falsi_func_b1 = labb1.copy().scale(0.7)
        reg_falsi_func_fb1 = labfb1.copy().scale(0.7)
        reg_falsi_func_fb11 = labfb1.copy().scale(0.7)
        self.play(
            Uncreate(reg_falsi_func[1]),
            Uncreate(reg_falsi_func[3]),
            Uncreate(reg_falsi_func[6]),
            reg_falsi_func_b1.animate.next_to(reg_falsi_func[3], DOWN*0),
            reg_falsi_func_fb1.animate.next_to(reg_falsi_func[1], DOWN*0),
            reg_falsi_func_fb11.animate.next_to(reg_falsi_func[6], DOWN*0)
        )
        
        c11 = Text(f"={round(pa3,4)}").scale(0.8).next_to(reg_falsi_func, RIGHT*1)
        self.play(
            Write(c11)
        )
        self.play(
            Transform(c11, c1),
            Uncreate(bfunction),
            Uncreate(b1function),
        )
        self.play(
            Write(VGroup(c1, labc1 ))
        )
        c11 = labc1.copy().scale(0.7)
        c12 = labc1.copy().scale(0.7)
        self.play(
            c11.animate.next_to(function[1].get_center(),DOWN*0),
            c12.animate.next_to(function[3].get_center(),DOWN*0),
        )
        cf11 = Text(f"={round(pfc1,4)}").scale(0.8).next_to(function, RIGHT*1)
        self.play(
            Write(cf11)
        )
        self.play(
            Transform(cf11, labfc1),
            Uncreate(c11),
            Uncreate(c12)
        )
        cfunction = MathTex("-x").next_to(function[1].get_center(), DOWN*0)
        c1function = MathTex("x").next_to(function[3].get_center(), DOWN*0)
        self.play(
            Create(cfunction),
            Create(c1function),
        )
        self.play(
            Create(arrow3)
        )
        self.play(
            Write(VGroup(fc1, labfc1 ))
        )