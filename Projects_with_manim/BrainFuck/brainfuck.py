from manim import *

class Brainfuck(Scene):
    def construct(self):
        text0 = Text("This is Brainf**k Programming language code").shift(UP*3)
        text1 = Text("+++++++++[>++++++++<-]>. \n>++++++++++[>++++++++++<-]>+. \n+++++++. \n. \n+++. \n>++++++[>+++++++<-]>++. \n------------. \n<<---------. \n>>++++++++++. \n. \n<<+++++. \n>>----------. \n<<++++++++++.").scale(0.5).next_to(text0, DOWN)

        text2 = Text("decipher it!! n comment it!!").next_to(text1, DOWN)
        self.add(text0,text1,text2 )