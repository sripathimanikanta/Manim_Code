from manim import *
# config.background_color = BLUE
config.frame_width = 16 
config.frame_height =9 
config.pixel_width = 1920
config.pixel_height = 1080

class BallTest(MovingCameraScene):
    def construct(self):
        rad = 25

        Circ1 = Circle(radius=rad,color="RED",stroke_width=30)
        ball = Dot(radius=1,color="WHITE").shift(UP*0)
        self.camera.frame.set(height=Circ1.height+10)
        self.play(
            Create(ball),
        )
        self.play(
            GrowFromCenter(Circ1)
        )
        self.wait()