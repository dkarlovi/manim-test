from os.path import dirname

from manim import *


class CodeTransform(Scene):
    def construct(self):
        code = self._code("seq1.js")
        self.play(Write(code))

        # TODO: read the files from a directory instead of hardcoding them
        files = ["seq2.js", "seq3.js", "seq4.js"]
        for file in files:
            new_code = self._code(file)
            self.play(
                Transform(code, new_code, replace_mobject_with_target_in_scene=True)
            )
            self.pause(2)
            code = new_code
        self.remove(code)
        self.wait(2)

    @staticmethod
    def _code(name):
        return Code(
            code_file=dirname(__file__) + f"/{name}",
            language="javascript",
            add_line_numbers=False,
        )
