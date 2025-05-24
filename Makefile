.SILENT:

dist: cs analyze test
cs: analyze/ruff-format
analyze: analyze/pyright
test: test/pytest

render/4k:
	poetry run manim example.py -pqm -r 3840,2160
render/hd:
	poetry run manim example.py -pqm -r 1920,1080
render/hd-30fps:
	poetry run manim example.py -pqm -r 1920,1080 --fps 30

analyze/ruff-check:
	poetry run ruff check
analyze/ruff-format:
	poetry run ruff format

analyze/pyright:
	poetry run pyright

test/pytest:
	poetry run pytest
