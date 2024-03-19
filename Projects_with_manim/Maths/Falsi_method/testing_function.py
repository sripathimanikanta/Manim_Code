from manim import *
import math

class testing_func(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        def func(x):
            print(4*((2.71828)**(-x))*math.sin(x)-1)
            return (4*((2.71828)**(-x))*math.sin(x)-1)

        def reg_falsi(a,b):
            print("x",(a*func(b) - b*func(a))/(func(b)-func(a)))
            return (a*func(b) - b*func(a))/(func(b)-func(a))

        ax = Axes(
            x_range=[0, 1.01, 0.1], 
            y_range=[-1.01, 0.40, 0.1],
            x_axis_config={"numbers_to_include":np.arange(0,1.1,0.1)},
            y_axis_config={"numbers_to_include":np.arange(-1.01,0.40,0.1)},
            axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(0)
        a1= 0
        b1 = 0.5
        cp1 = 0.1
        dp1 = 0.6
        Dot1 = Dot(ax.coords_to_point(a1,func(a1)))
        text1 = Text(f"({a1},{round(func(a1),4)})").scale(0.5).next_to(Dot1,DOWN*1)
        Dot2 = Dot(ax.coords_to_point(b1,func(b1)))
        text2 = Text(f"({b1},{round(func(b1),4)})").scale(0.5).next_to(Dot2,DOWN*1)
        Dot3 = Dot(ax.coords_to_point(cp1,func(cp1)))
        text3 = Text(f"({cp1},{round(func(cp1),4)})").scale(0.5).next_to(Dot3,UP*1)
        Dot4 = Dot(ax.coords_to_point(dp1,func(dp1)))
        text4 = Text(f"({dp1},{round(func(dp1),4)})").scale(0.5).next_to(Dot4,UP*1)

        def func(x):
            return (4*((2.71828)**(-x))*math.sin(x)-1)
        graph = ax.plot(func, color=MAROON)
        self.play(
            Write(
                VGroup(graph,ax,labels)
            )
        )
        self.play(
            Write(VGroup(Dot1,text1))
        )
        self.play(
            Write(VGroup(Dot2,text2))
        )
        self.play(
            Write(VGroup(Dot3,text3))
        )
        self.play(
            Write(VGroup(Dot4,text4))
        )
        self.wait()

        line1 = Line(Dot3.get_center(),Dot2.get_center())
        self.play(
            Create(line1)
        )

        x = 0.3707
        xdot = Dot(ax.coords_to_point(x,0))
        xtext = Text(f"(x,0)").scale(0.5).next_to(xdot,UP*1)
        self.play(
            Write(VGroup(xdot,xtext))
        )
        line2 = Line(Dot3.get_center(),xdot.get_center())
        self.play(
            Create(line2)
        )

        c1 = reg_falsi(cp1,b1)
        Dot5 = Dot(ax.coords_to_point(c1,0))
        text5 = Text(f"({round(c1,4)},0)").scale(0.5).next_to(Dot5,DOWN*1)
        self.play(
            Create(VGroup(Dot5,text5))
        )
        # self.play(
        #     self.camera.frame.animate.scale(0.5).move_to(Dot5)
        # )
        ax1 = Axes(
            x_range=[0, 0.5, 0.1], 
            y_range=[-0.7, 0.20, 0.1],
            x_axis_config={"numbers_to_include":np.arange(0,0.5,0.1)},
            y_axis_config={"numbers_to_include":np.arange(-0.7,0.20,0.1)},
            axis_config={"include_tip": False}
        )
        graph1 = ax1.plot(func, color=YELLOW)
        Dot21 = Dot(ax1.coords_to_point(b1,func(b1)))
        text21 = Text(f"({b1},{round(func(b1),4)})").scale(0.5).next_to(Dot21,DOWN*1)
        Dot31 = Dot(ax1.coords_to_point(cp1,func(cp1)))
        text31 = Text(f"({round(cp1,4)},{round(func(cp1),4)})").scale(0.5).next_to(Dot31,UP*1)
        xdot1 = Dot(ax1.coords_to_point(x,0))
        xtext1 = Text(f"(x,0)").scale(0.5).next_to(xdot1,UP*1)
        line11 = Line(Dot31.get_center(),Dot21.get_center())
        line21 = Line(Dot31.get_center(),xdot1.get_center())
        Dot51 = Dot(ax1.coords_to_point(c1,0))
        text51 = Text(f"({round(c1,4)},0)").scale(0.5).next_to(Dot51,DOWN*1)
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(Dot5),
            FadeOut(VGroup(Dot1,text1,Dot4,text4)),
            Transform(ax,ax1),
            Transform(graph,graph1),
            Transform(Dot2,Dot21),
            Transform(text2,text21),
            Transform(Dot3,Dot31),
            Transform(text3,text31),
            Transform(xdot,xdot1),
            Transform(xtext,xtext1),
            Transform(line1,line11),
            Transform(line2,line21),
            Transform(Dot5,Dot51),
            Transform(text5,text51),
        )
        self.play(
            Restore(self.camera.frame)
        )
        line_1 = ax.get_vertical_line(ax.input_to_graph_point(c1, graph1), color=YELLOW)
        self.play(
            Create(line_1)
        )
        Dot6 = Dot(ax1.coords_to_point(round(c1,2),func(round(c1,2))))
        text6 = Text(f"({round(c1,4)},{round(func(c1),4)})").scale(0.5).next_to(Dot6,UP*1)
        self.play(
            Transform(Dot5, Dot6),
            Transform(text5, text6)
        )

        # self.play(
        #     Transform(line1.copy(),line2),
        #     Transform(Dot2.copy(),xdot)
        # )

        # self.play(
        #     Transform(line2,line1),
        #     Transform(xdot,Dot2)
        # )

        slopeform = MathTex("m = \\frac{y_{2} - y_{1} }{ x_{2} - x_{1} }").move_to(DOWN*2+RIGHT*1)
        self.play(
            Write(slopeform)
        )
        self.wait()