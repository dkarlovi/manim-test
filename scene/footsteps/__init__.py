from manim import *

config.background_color = "#f0f0f0"  # Set a light background color


class Footsteps(Scene):
    def construct(self):
        text = Text("O", font_size=100, color="#000000", font="Sans")
        start_y = -config.frame_height / 2 + text.height / 2
        end_y = (config.frame_height / 2 - text.height / 2) + text.height
        step_size = text.height
        step_width = text.width / 2

        y = start_y
        footsteps = []
        offset = -1
        while y <= end_y:
            t = text.copy().move_to([0 + offset * step_width, y, 0])
            footsteps.append(t)
            y += step_size
            offset = -offset

        for i, t in enumerate(footsteps):
            if i > 0:
                self.add(footsteps[i - 1])
            self.add(t)
            self.wait(0.2)
