from manim import *

class CodeExample(Scene):
    def construct(self):
        code = Code(
            code_file=__file__,
            background="window",
            formatter_style="monokai",
        )
        self.play(Write(code), run_time=1)
        self.wait(3)
