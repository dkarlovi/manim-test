import pytest
from manim import tempconfig
from example import SquareToCircle


def test_square_to_circle_scene_runs(tmp_path):
    # Use a temporary directory for output
    with tempconfig({"media_dir": str(tmp_path)}):
        scene = SquareToCircle()
        # Should not raise during construction
        scene.render()
        # Check that at least one mobject (the transformed square/circle) is present
        assert len(scene.mobjects) > 0
