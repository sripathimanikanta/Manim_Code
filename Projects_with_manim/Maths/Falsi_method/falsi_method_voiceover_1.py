import math
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService
# config.background_color = "#00aad4" 
# config.frame_width = 9 
# config.frame_height = 16
# config.pixel_width = 1080 
# config.pixel_height = 1920

class falsi_method(VoiceoverScene):
    def construct(self):
        def func(x):
            print(4*((2.71828)**(-x))*math.sin(x)-1)
            return (4*((2.71828)**(-x))*math.sin(x)-1)

        def reg_falsi(a,b):
            print("x",(a*func(b) - b*func(a))/(func(b)-func(a)))
            return (a*func(b) - b*func(a))/(func(b)-func(a))
        self.set_speech_service(
           GTTSService()
        ) 
        tcolor= WHITE 
        with self.voiceover(text="""if we want to find a root to a function,which is not polynomial but instead
                           it has trigonometry or exponential function.""") as tracker:
            time = 2
            # text1 = Text("Root for \nnot Algebraic \ninstead \nTrigonometric and Exponential",t2c={"Root for":tcolor,"instead":tcolor,"and":tcolor,"not":RED,"Algebraic":RED_D,"Trigonometric":GREEN_D, "Exponential":GREEN_D})
            text1 = MarkupText(f'Roots  \r <span strikethrough="true" strikethrough_color="red" foreground="red">Polynomial</span> \r \r <span foreground="green">Trigonometry</span> and <span foreground="green">Exponential</span> ') 
            # line = Line(text1[14].get_center(),text1[23].get_center())
            self.play(
                # Write(line),
                Write(text1),
                run_time=tracker.duration/time
            )
            self.play(
                FadeOut(text1),
                run_time=tracker.duration/time
            )
            
        with self.voiceover(text="for example 4 into e to the power minus x multiplied to sine x minus one") as tracker:
            time = 3
            mathtex1 = MathTex("4{{e^{-x} }}{{sin(x)}}-1").set_color(tcolor)
            self.play(
                Write(mathtex1),
                run_time=tracker.duration/time
            )

        with self.voiceover(text="Here, e to the power minus x is Exponential function") as tracker:
            time =1 
            text2 = Text('Exponential',color=RED).scale(0.7).next_to(mathtex1, UP*3)
            line1 = Arrow(mathtex1[1].get_center(),text2.get_center()).set_color(RED)
            self.play(
                mathtex1[1].animate.set_color(RED),
                Write(
                    VGroup(
                        line1, text2
                    )
                ),
                run_time=tracker.duration/time
            )

        with self.voiceover(text="Here, sine x is Trigonometry function") as tracker:
            time =1 
            text3 = Text('Trigonometry',color=GREEN).scale(0.7).next_to(mathtex1,DOWN*3)
            line2 = Arrow(mathtex1[2].get_center(),text3.get_center()).set_color(GREEN)
            self.play(
                mathtex1[2].animate.set_color(GREEN),
                Write(
                    VGroup(
                        line2, text3
                    )
                ),
                run_time=tracker.duration/time
            )

        with self.voiceover(text="There is no exact formula to find roots for this kind of equations") as tracker:
           time = 2
           text4 = Text("*atleast to my knowledge").set_color(ORANGE).next_to(text2,UP*1)
           self.play(
               Write(text4),
               run_time=tracker.duration/time
           )
           self.play(
               FadeOut(text4),
               run_time=tracker.duration/time
           )

        with self.voiceover(text="But Mathematicians are one of smartest people, so they figured out different ways to solve this problem") as tracker:
            self.play(
                FadeOut(
                    VGroup(
                        mathtex1,line1,line2,text2,text3
                    )
                    ),
                run_time=tracker.duration/2
            )

        with self.voiceover(text="""They are 
                            1 Bisection method 
                            2 Iteration Method 
                            3 Falsi Position Method
                            4 Newton Raphson method
                            5 Muller method""") as tracker:
            time = 1
            btext = BulletedList("1 Bisection method", "2 Iteration method", "3 Falsi Position method","4 Newton-Raphson method", "5 Muller method",height=4,width=4).set_color(tcolor)
            self.play(
                Write(
                    btext
                ),
                run_time = tracker.duration/time
            )

        with self.voiceover(text="So today we going to discuss about falsi position method") as tracker:
            self.play(
               btext.animate.set_color_by_tex("3 Falsi Position method", RED_D),
               run_time=tracker.duration/time
            )

        self.play(
            FadeOut(
                btext
            ),
            run_time=0.5
        )

        with self.voiceover(text="Lets consider a numberline for plotting input, it is represented in BLUE color") as tracker:
            NumInp = NumberLine(
                x_range=[-0.01,0.51,0.1],
                length=10,
                include_numbers=True,
                label_direction=UP,
                color=BLUE
                )
            self.play(
                Write(NumInp)
            )
        
        a1 = 0
        b1 = 0.5
        pa1 = Dot(NumInp.number_to_point(a1),color=BLUE_E)
        pb1 = Dot(NumInp.number_to_point(b1),color=BLUE_E)
        texta1 = Text(f"a = {a1}").scale(0.5).next_to(pa1,DOWN*1)
        textb1 = Text(f"b = {b1}").scale(0.5).next_to(pb1,DOWN*1)

        with self.voiceover(text="now lets consider 0 as first input that is a, 0.5 as second input call it b") as tracker:
            time = 2
            self.play(
                Create(pa1),
                Create(texta1),
                run_time=tracker.duration/time
            ) 
            self.play(
                Create(pb1),
                Create(textb1),
                run_time=tracker.duration/time
            ) 
        self.play(
            FadeOut(pa1),
            FadeOut(texta1),
            FadeOut(pb1),
            FadeOut(textb1),
            FadeOut(NumInp)
        ) 
        
        with self.voiceover(text="If we consider,") as tracker:
            pass

        with self.voiceover(text="Lets consider a numberline for plotting output, it is represented in RED color") as tracker:
            NumOut = NumberLine(
                x_range=[-1.01,0.20,0.1],
                length=10,
                include_numbers=True,
                label_direction=UP,
                color=RED
                )
            self.play(
                Write(NumOut)
            )
        
        fa1 = func(0)
        fb1 = func(0.5)
        pfa1 = Dot(NumOut.number_to_point(fa1),color=RED_E)
        pfb1 = Dot(NumOut.number_to_point(fb1),color=RED_E)
        textfa1 = Text(f"a = {round(fa1,ndigits=4)}").scale(0.5).next_to(pfa1,DOWN*1)
        textfb1 = Text(f"b = {round(fb1,ndigits=4)}").scale(0.5).next_to(pfb1,DOWN*1)

        with self.voiceover(text="now lets consider -1 as first output that is f of a, 0.1631 as second output call it f of b") as tracker:
            time = 2
            self.play(
                Create(pfa1),
                Create(textfa1),
                run_time=tracker.duration/time
            ) 
            self.play(
                Create(pfb1),
                Create(textfb1),
                run_time=tracker.duration/time
            ) 
        self.play(
            FadeOut(pfa1),
            FadeOut(textfa1),
            FadeOut(pfb1),
            FadeOut(textfb1),
            FadeOut(NumOut)
        ) 