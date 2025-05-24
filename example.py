from manim import Circle, Square, Scene, Create, Transform, FadeOut, config, RIGHT, TAU, PINK

config.frame_rate = 60
config.pixel_width = 3840
config.pixel_height = 2160

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
