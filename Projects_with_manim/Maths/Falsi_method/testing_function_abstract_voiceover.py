from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import math

class testing_func(MovingCameraScene,VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            GTTSService()
        )
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
        text2 = Text(f"(b1,f(b1))").scale(0.5).next_to(Dot2,DOWN*1)
        Dot3 = Dot(ax.coords_to_point(cp1,func(cp1)))
        text3 = Text(f"(a1,f(a1))").scale(0.5).next_to(Dot3,UP*1)
        Dot4 = Dot(ax.coords_to_point(dp1,func(dp1)))
        text4 = Text(f"({dp1},{round(func(dp1),4)})").scale(0.5).next_to(Dot4,UP*1)

        def func(x):
            return (4*((2.71828)**(-x))*math.sin(x)-1)
        graph = ax.plot(func, color=MAROON)
        with self.voiceover(text="Let us consider a function and plot its graph") as tracker:
            time = 1
            self.play(
                Write(
                    VGroup(graph,ax,labels)
                ),run_time=tracker.duration/time
            )
        
        with self.voiceover(text="let us choose some points,"):
            pass

        # with self.voiceover(text=f"point A(a1,f(a1))")as tracker:
        #     self.play(
        #         Write(VGroup(Dot1,text1)),
        #         run_time=tracker.duration
        #     )


        with self.voiceover(text=f"point Capital A(a1,f(a1))")as tracker:
            self.play(
                Write(VGroup(Dot3,text3)),
                run_time=tracker.duration
            )

        with self.voiceover(text=f"point Capital B(b1,f(b1))")as tracker:
            self.play(
                Write(VGroup(Dot2,text2)),
                run_time=tracker.duration
            )

        # with self.voiceover(text=f"point D({dp1},{round(func(dp1),4)})")as tracker:
        #     self.play(
        #         Write(VGroup(Dot4,text4)),
        #         run_time=tracker.duration
        #     )
        self.wait()

        with self.voiceover(text="As we can see point 1")as tracker:
            self.play(
                Dot3.animate.set_color(RED),
                run_time=tracker.duration
            )

        with self.voiceover(text="and 2")as tracker:
            self.play(
                Dot2.animate.set_color(GREEN),
                run_time=tracker.duration
            )

        linebtw = DoubleArrow(Dot3.get_center(),ax.coords_to_point(b1,func(cp1),0))
        linefraxestodot3 = ax.get_vertical_line(ax.input_to_graph_point(cp1, graph), color=RED)
        # print("Dot2.get_center",Dot2.get_center())
        # print("Dot2.get_y",Dot2.get_y())
        # print("Dot2.get_y",ax.coords_to_point(Dot2.get_y()))
        linefraxestodot2 = ax.get_vertical_line(ax.coords_to_point(b1,func(cp1),0), color=GREEN)
        # print("with raw",[b1,-func(b1)+func(cp1),0])
        # print("with raw with coodinates",ax.coords_to_point(b1,-func(b1)+func(cp1),0))
        # print("with raw with coodinates with ",ax.coords_to_point(b1,func(cp1),0))
        with self.voiceover(text="are closer to each other")as tracker:
            time = 3
            self.play(
                Create(VGroup(linefraxestodot2,linefraxestodot3)),
                run_time=tracker.duration/time
            )
            self.play(
                Create(linebtw),
                run_time=tracker.duration/time
            )
            self.play(
                FadeOut(VGroup(linefraxestodot2,linefraxestodot3,linebtw)),
                run_time=tracker.duration/time
            )

        rectop = Rectangle(color=BLUE,height=config.frame_height/2,width=config.frame_width).set_opacity(0.5).next_to(ax.coords_to_point(0.5,0,0),UP*0.1)
        recbottom = Rectangle(color=RED,height=config.frame_height/1.5,width=config.frame_width).set_opacity(0.5).next_to(ax.coords_to_point(0.5,0,0),DOWN*0.1)
        with self.voiceover(text="and they are on different sides of x-axis")as tracker:
            time = 4
            self.play(
                Create(rectop),
                run_time=tracker.duration/time
            )
            self.play(
                Uncreate(rectop),
                run_time=tracker.duration/time
            )
            self.play(
                Create(recbottom),
                run_time=tracker.duration/time
            )
            self.play(
                Uncreate(recbottom),
                run_time=tracker.duration/time
            )
        line1 = Line(Dot3.get_center(),Dot2.get_center())
        x = 0.3707
        xdot = Dot(ax.coords_to_point(x,0))
        xtext = Text(f"(x,0)").scale(0.5).next_to(xdot,UP*1)

        with self.voiceover(text="As we can see, the root is at point captial X")as tracker:
            self.play(
                Write(VGroup(xdot,xtext)),
                run_time=tracker.duration
            )

        with self.voiceover(text="we dont have any direct formula to compute and find the answer") as tracker:
            pass

        with self.voiceover(text="But Mathematician, got an idea") as tracker:
            pass

        with self.voiceover(text="He has drawn a line segment connecting point A and B") as tracker:
            self.play(
                Create(line1),
                run_time=tracker.duration
            )

        c1 = reg_falsi(cp1,b1)
        Dot5 = Dot(ax.coords_to_point(c1,0))
        text5 = MathTex("(x_1,0)").scale(0.5).next_to(Dot5,DOWN*1)
        with self.voiceover(text="then selected the point which intersects between chord and x-axis") as tracker:
            self.play(
                self.camera.frame.animate.scale(0.5).move_to(Dot5),
                Create(VGroup(Dot5,text5)),
                run_time=tracker.duration
            )

        ax1 = Axes(
            x_range=[0, 0.5, 0.1], 
            y_range=[-0.7, 0.20, 0.1],
            x_axis_config={"numbers_to_include":np.arange(0,0.5,0.1)},
            y_axis_config={"numbers_to_include":np.arange(-0.7,0.20,0.1)},
            axis_config={"include_tip": False}
        )
        graph1 = ax1.plot(func, color=YELLOW)
        Dot21 = Dot(ax1.coords_to_point(b1,func(b1)))
        text21 = Text(f"(b1,f(b1))").scale(0.5).next_to(Dot21,DOWN*1)
        Dot31 = Dot(ax1.coords_to_point(cp1,func(cp1)))
        text31 = Text(f"(a1,f(a1))").scale(0.5).next_to(Dot31,UP*1)
        xdot1 = Dot(ax1.coords_to_point(x,0))
        xtext1 = Text(f"(x,0)").scale(0.5).next_to(xdot1,UP*1)
        line11 = Line(Dot31.get_center(),Dot21.get_center())
        # line21 = Line(Dot31.get_center(),xdot1.get_center())
        Dot51 = Dot(ax1.coords_to_point(c1,0))
        text51 = MathTex("(x_1,0)").scale(0.5).next_to(Dot51,DOWN*1)
        self.play(
            FadeOut(VGroup(Dot1,text1,Dot4,text4)),
            ReplacementTransform(ax,ax1),
            ReplacementTransform(graph,graph1),
            ReplacementTransform(Dot2,Dot21),
            ReplacementTransform(text2,text21),
            ReplacementTransform(Dot3,Dot31),
            ReplacementTransform(text3,text31),
            ReplacementTransform(xdot,xdot1),
            ReplacementTransform(xtext,xtext1),
            ReplacementTransform(line1,line11),
            # Transform(line2,line21),
            ReplacementTransform(Dot5,Dot51),
            ReplacementTransform(text5,text51),
        )
        self.play(
            Restore(self.camera.frame)
        )

        line_1 = ax1.get_vertical_line(ax.input_to_graph_point(c1, graph1), color=YELLOW)
        self.play(
            Create(line_1)
        )

        Dot6 = Dot(ax1.coords_to_point(c1,func(round(c1,2))))
        text6 = MathTex("(x_1,y_1)").scale(0.5).next_to(Dot6,UP*1)
        with self.voiceover(text="then plotted it on the graph") as tracker:
            self.play(
                ReplacementTransform(Dot5, Dot6),
                ReplacementTransform(text5, text6),
                run_time=tracker.duration
            )

        with self.voiceover(text="as we can see point Capital x prime is ") as tracker:
            self.play(
                Uncreate(line_1),
                FadeOut(line11,Dot51,text51)
           ) 
        
        with self.voiceover(text="then he repeated this process")as tracker:
            pass

        with self.voiceover(text="took Capital x prime as point B")as tracker:
            self.play(
                text21.animate.next_to(Dot6,UP*1),
                # Transform(text2,text6),
                FadeOut(VGroup(text6,Dot21))
                # Transform(text6,text7),
            ) 
        linebtwa1c1 = Line(Dot3.get_center(),Dot6.get_center()) 
        self.play(
            Create(linebtwa1c1)
        )
        x2 = reg_falsi(c1,cp1)
        xp2 = func(x2)
        xp2dot = Dot(ax1.coords_to_point(x2,0))
        xp2text = MathTex("(x_2,0)").scale(0.5).next_to(xp2dot,UP*1)
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(xp2dot),
            Create(VGroup(xp2dot,xp2text)),
        )

        ax2 = Axes(
            x_range=[0.1, c1, 0.1], 
            y_range=[-0.7, func(c1)+0.1, 0.1],
            x_axis_config={"numbers_to_include":np.arange(0.1,c1,0.1)},
            y_axis_config={"numbers_to_include":np.arange(-0.7,func(c1)+0.1,0.1)},
            axis_config={"include_tip": False}
        )
        graph2 = ax2.plot(func, color=GREEN)
        Dot22 = Dot(ax2.coords_to_point(c1,func(c1)))
        text22 = Text(f"(b1,f(b1))").scale(0.5).next_to(Dot22,UP*1)
        Dot32 = Dot(ax2.coords_to_point(cp1,func(cp1)))
        text32 = Text(f"(a1,f(a1))").scale(0.5).next_to(Dot32,UP*1)
        linebtwa1c1upd = Line(Dot32.get_center(),Dot22.get_center())
        xdot2 = Dot(ax2.coords_to_point(x,0))
        xtext2 = MathTex("(x,0)").scale(0.5).next_to(xdot2,UP*1)
        xp2dotupd = Dot(ax2.coords_to_point(x2,0))
        xp2textupd = MathTex("(x_2,0)").scale(0.5).next_to(xp2dotupd,DOWN*1)
        self.play(
            Uncreate(VGroup(Dot1,text1,Dot4,text4)),
            ReplacementTransform(ax1,ax2),
            ReplacementTransform(graph1,graph2),
            ReplacementTransform(Dot6,Dot22),
            ReplacementTransform(text21,text22),
            ReplacementTransform(Dot31,Dot32),
            ReplacementTransform(text31,text32),
            ReplacementTransform(linebtwa1c1,linebtwa1c1upd),
            ReplacementTransform(xdot1,xdot2),
            ReplacementTransform(xtext1,xtext2),
            ReplacementTransform(xp2dot,xp2dotupd),
            ReplacementTransform(xp2text,xp2textupd),
        )
        self.play(
            Restore(self.camera.frame)
        )
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(xp2dotupd),
            Create(VGroup(xp2dot,xp2text)),
        )

        line_2 = ax2.get_vertical_line(ax.input_to_graph_point(x2, graph2), color=YELLOW)
        self.play(
            Create(line_2)
        )

        xp2dotupdfin = Dot(ax2.coords_to_point(x2,func(round(x2,2))))
        xp2textupdfin = MathTex("(x_2,y_2)").scale(0.5).next_to(xp2dotupdfin,UP*1)
        with self.voiceover(text="then plotted it on the graph") as tracker:
            self.play(
                ReplacementTransform(xp2dotupd, xp2dotupdfin),
                ReplacementTransform(xp2textupd, xp2textupdfin),
                run_time=tracker.duration
            )

            self.play(
                Uncreate(line_2),
                FadeOut(VGroup(linebtwa1c1upd,xp2dot,xp2text,xp2dotupd,xp2textupd))
            ) 

            self.play(
                text22.animate.next_to(xp2dotupdfin,UP*1),
                FadeOut(VGroup(xp2textupdfin,Dot22))
            )
        linebtwa1c2 = Line(Dot3.get_center(),xp2dotupdfin.get_center()) 
        self.play(
            Create(linebtwa1c2)
        )
        x3 = reg_falsi(cp1,x2)
        xp3 = func(x3)
        xp3dot = Dot(ax2.coords_to_point(x3,0))
        xp3text = MathTex("(x_3,0)").scale(0.5).next_to(xp3dot,UP*1)
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(xp3dot),
            Create(VGroup(xp3dot,xp3text)),
        )

        ax3 = Axes(
            x_range=[0.3, x2, 0.1], 
            y_range=[-0.7, func(x2)+0.1, 0.1],
            x_axis_config={"numbers_to_include":np.arange(0.2,x2,0.1)},
            y_axis_config={"numbers_to_include":np.arange(-0.7,func(x2)+0.1,0.1)},
            axis_config={"include_tip": False}
        )
        graph3 = ax3.plot(func, color=RED)
        Dot23 = Dot(ax3.coords_to_point(x2,func(x2)))
        text23 = Text(f"(b1,f(b1))").scale(0.5).next_to(Dot23,UP*1)
        Dot33 = Dot(ax3.coords_to_point(cp1,func(cp1)))
        text33 = Text(f"(a1,f(a1))").scale(0.5).next_to(Dot33,UP*1)
        linebtwa1c2upd = Line(Dot33.get_center(),Dot23.get_center())
        xdot3 = Dot(ax3.coords_to_point(x,0))
        xtext3 = MathTex("(x,0)").scale(0.5).next_to(xdot3,UP*1)
        xp3dotupd = Dot(ax3.coords_to_point(x3,0))
        xp3textupd = MathTex("(x_3,0)").scale(0.5).next_to(xp3dotupd,DOWN*1)
        self.play(
            Uncreate(VGroup(Dot1,text1,Dot4,text4)),
            ReplacementTransform(ax2,ax3),
            ReplacementTransform(graph2,graph3),
            ReplacementTransform(xp2dotupdfin,Dot23),
            ReplacementTransform(text22,text23),
            ReplacementTransform(Dot32,Dot33),
            ReplacementTransform(text32,text33),
            ReplacementTransform(linebtwa1c2,linebtwa1c2upd),
            ReplacementTransform(xdot2,xdot3),
            ReplacementTransform(xtext2,xtext3),
            ReplacementTransform(xp3dot,xp3dotupd),
            ReplacementTransform(xp3text,xp3textupd),
        )
        self.play(
            Restore(self.camera.frame)
        )

        slopeform = MathTex("m = \\frac{y_{2} - y_{1} }{ x_{2} - x_{1} }").move_to(DOWN*2+RIGHT*1)
        self.play(
            Write(slopeform)
        )
        self.wait()