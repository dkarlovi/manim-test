from os.path import dirname
from manim import Scene, ImageMobject


class ReproImage(Scene):
    def construct(self):
        foot_left = ImageMobject(dirname(__file__) + "/foot-left.png")

        self.add(foot_left)
        self.wait(2)
