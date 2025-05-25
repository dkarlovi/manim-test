.SILENT:

dist: cs analyze test
cs: analyze/ruff-format
analyze: analyze/pyright
test: test/pytest

preview/%: %
	poetry run manim render $< --renderer opengl --preview
4k@60fps/%: %
	poetry run manim render $< --resolution 3840,2160 --fps 60
4k@30fps/%: %
	poetry run manim render $< --resolution 3840,2160 --fps 30
hd@60fps/%: %
	poetry run manim render $< --resolution 1920,1080 --fps 60
hd@30fps/%: %
	poetry run manim render $< --resolution 1920,1080 --fps 30

analyze/ruff-check:
	poetry run ruff check
analyze/ruff-format:
	poetry run ruff format

analyze/pyright:
	poetry run pyright

test/pytest:
	poetry run pytest
