from os.path import dirname

from manim import config, Scene, Text, ImageMobject

config.background_color = "#f0f0f0"  # Set a light background color


class Footsteps(Scene):
    def construct(self):
        foot_left = ImageMobject(dirname(__file__) + "/foot-left.png")
        foot_right = ImageMobject(dirname(__file__) + "/foot-right.png")
        foot_left.set_color("#000000")
        foot_right.set_color("#FF0000")

        if foot_left.width != foot_right.width:
            raise ValueError("Foot images must have the same width")
        if foot_left.height != foot_right.height:
            raise ValueError("Foot images must have the same height")

        start_y = -config.frame_height / 2 + foot_left.height / 2
        end_y = (config.frame_height / 2 - foot_left.height / 2) + foot_left.height
        step_size = foot_left.height
        step_width = foot_left.width / 2

        y = start_y
        footsteps = []
        offset = -1
        while y <= end_y:
            if offset < 0:
                step = foot_left
            else:
                step = foot_right
            t = step.copy().move_to((offset * step_width, y, 0))
            footsteps.append(t)
            y += step_size
            offset = -offset

        for i, t in enumerate(footsteps):
            if i > 0:
                self.add(footsteps[i - 1])
            self.add(t)
            self.wait(0.2)
