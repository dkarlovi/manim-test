.SILENT:

dist: cs analyze test
cs: analyze/ruff-format
analyze: analyze/pyright
test: test/pytest

render: render/hd-30fps
render/4k:
	poetry run manim example.py --renderer opengl -p -r 3840,2160 --fps 60
render/hd:
	poetry run manim example.py --renderer opengl -p -r 1920,1080 --fps 60
render/hd-30fps:
	poetry run manim example.py --renderer opengl -p -r 1920,1080 --fps 30

analyze/ruff-check:
	poetry run ruff check
analyze/ruff-format:
	poetry run ruff format

analyze/pyright:
	poetry run pyright

test/pytest:
	poetry run pytest
