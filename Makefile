.SILENT:

dist: cs analyze test
cs: analyze/ruff-format
analyze: analyze/pyright
test: test/pytest

preview/%: %
	poetry run manim render $</__init__.py --renderer opengl --preview
debug/%: %
	poetry run manim render $</__init__.py --renderer opengl --preview --enable_wireframe
render/%/4k@60: %
	poetry run manim render $</__init__.py --resolution 3840,2160 --fps 60 --preview
render/%/4k@30: %
	poetry run manim render $</__init__.py --resolution 3840,2160 --fps 30 --preview
render/%/hd@60: %
	poetry run manim render $</__init__.py --resolution 1920,1080 --fps 60 --preview
render/%/hd@30: %
	poetry run manim render $</__init__.py --resolution 1920,1080 --fps 30 --preview

analyze/ruff-check:
	poetry run ruff check
analyze/ruff-format:
	poetry run ruff format

analyze/pyright:
	poetry run pyright

test/pytest:
	poetry run pytest
