.SILENT:

dist: cs analyze test
cs: analyze/ruff-format
analyze: analyze/pyright
test: test/pytest

preview:
	poetry run manim render example.py --renderer opengl --preview
render/4k:
	poetry run manim render example.py --resolution 3840,2160 --fps 60
render/hd:
	poetry run manim render example.py --resolution 1920,1080 --fps 60
render/hd-30fps:
	poetry run manim render example.py --resolution 1920,1080 --fps 30

analyze/ruff-check:
	poetry run ruff check
analyze/ruff-format:
	poetry run ruff format

analyze/pyright:
	poetry run pyright

test/pytest:
	poetry run pytest
