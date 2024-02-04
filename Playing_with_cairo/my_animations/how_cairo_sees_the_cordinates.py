from manim import *

#only -ps
class Cairo_sees(Scene):
    def construct(self):
        code = '''cr.rectangle(x,y,w,h)'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace",color="#282822").shift(UP*3,LEFT*4).scale(0.75)
        global_x, global_y = DOWN*1, RIGHT*2
        local_x, local_y = global_x+ DOWN*0.5, global_y+RIGHT*0.75
        rect = Rectangle(height=6,width=10).shift(global_x, global_y)
        rect1 = Rectangle(height=2,width=3,color="RED", fill_opacity=1).shift(local_x, local_y)
        # arr1 = Arrow(start=(rect.get_center()-[rect.width/2,0,0]),end=rect.get_center(), buff=0)
        # arr2 = Arrow(start=(rect.get_center()+[0,rect.height/2,0]),end=rect.get_center(), buff=0)
        arrx = Arrow(start=(rect.get_center()-[rect.width/2,0,0]-(global_x-local_x)),end=(rect1.get_center()-[rect1.width/2,0,0]), buff=0)
        arry = Arrow(start=(rect.get_center()+[0,rect.height/2,0]-(global_y-local_y)),end=(rect1.get_center()+[0,rect1.height/2,0]), buff=0)
        text_x = Text("x").next_to(arrx, DOWN)
        text_y = Text("y").next_to(arry, RIGHT)
        bracket_w = Brace(rect1)
        text_w = Text("w", font="Monospace").next_to(bracket_w, DOWN)
        bracket_h = Brace(rect1,direction=[1,0,0])
        text_h = Text("h", font="Monospace").next_to(bracket_h, RIGHT)
        allobjects = VGroup(bracket_w, text_w, bracket_h,text_h)
        self.add(rendered_code, allobjects)
        