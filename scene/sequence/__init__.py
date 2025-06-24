from manim import Scene, Text, Write, Circle, LEFT, RIGHT, UP, DOWN, rate_functions, AnimationGroup, Succession

class Sequence(Scene):
    def construct(self):
        self.play(self._title("AnimationGroup, lag_ratio=1.0"))
        self.wait(1)
        anim_up = self._circle(UP, duration=1)
        anim_center = self._circle(0, duration=0.5)
        anim_down = self._circle(DOWN, duration=2)
        self.play(
            AnimationGroup(anim_up, anim_center, anim_down, lag_ratio=1.0)
        )
        self.wait(1)
        self.clear()

        self.play(self._title("AnimationGroup, lag_ratio=0.0"))
        self.wait(1)
        anim_up = self._circle(UP, duration=1)
        anim_center = self._circle(0, duration=0.5)
        anim_down = self._circle(DOWN, duration=2)
        self.play(
            AnimationGroup(anim_up, anim_center, anim_down, lag_ratio=0.0)
        )
        self.wait(1)
        self.clear()

        self.play(self._title("Succession"))
        self.wait(1)
        anim_up = self._circle(UP, duration=1)
        anim_center = self._circle(0, duration=0.5)
        anim_down = self._circle(DOWN, duration=2)
        self.play(
            Succession(anim_up, anim_center, anim_down)
        )
        self.wait(1)
        self.clear()

        self.wait(2)
        

    @staticmethod
    def _title(text):
        title = Text(text, font_size=48)
        title.set_color("#FFFFFF")
        title.move_to(UP * 3.5)
        
        return Write(title)
    
    @staticmethod
    def _circle(pos, duration):
        circle = Circle(radius=1, color="#FF0000", fill_color="#FF0000", fill_opacity=0.5)
        circle.move_to(LEFT + pos * 2)
        anim = circle.animate(rate_func=rate_functions.ease_out_bounce, run_time=duration).move_to(RIGHT + pos * 2)
        
        return anim
