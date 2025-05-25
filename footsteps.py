from manim import *

config.background_color = "#f0f0f0"  # Set a light background color

class Footsteps(Scene):
    def construct(self):
        text = Text(
            "f",
            font_size=80,
            color="#000000",  # Set a dark color for contrast
            font="Sans"
        )
        # Start at the bottom of the screen
        start_y = -config.frame_height / 2 + text.height / 2
        end_y = config.frame_height / 2 - text.height / 2
        step_size = text.height * 1.2  # Slight overlap for aesthetics

        y = start_y
        footsteps = []
        while y <= end_y:
            t = text.copy().move_to([0, y, 0])
            footsteps.append(t)
            y += step_size

        for i, t in enumerate(footsteps):
            if i > 0:
                self.add(footsteps[i-1])
            self.add(t)
            self.wait(0.2)

