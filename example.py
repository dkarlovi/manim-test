from manim import (
    Circle,
    Square,
    Scene,
    Create,
    Transform,
    RIGHT,
    TAU,
    PINK,
    GREY_A,
    PURE_BLUE,
    config,
)

config.background_opacity = 0
config.background_color = GREY_A


class SquareToCircle(Scene):
    def construct(self):
        square = Square(color=PURE_BLUE)
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        target_circle = Circle(color=PURE_BLUE)
        target_circle.set_fill(PINK, opacity=0)

        self.play(Create(square))
        self.play(Transform(square, target_circle, path_arc=9))
