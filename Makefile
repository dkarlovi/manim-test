render/4k:
	poetry run manim example.py -pqm -r 3840,2160

render/hd:
	poetry run manim example.py -pqm -r 1920,1080

render/hd-30fps:
	poetry run manim example.py -pqm -r 1920,1080 --fps 30

cs:
	poetry run ruff check --fix .
